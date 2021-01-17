import base64
import concurrent.futures
from typing import List

import numpy as np
import tensorflow as tf
import pickle
from itertools import accumulate
from pathlib import Path

from scipy.spatial.ckdtree import cKDTree
from skimage.measure import ransac
from skimage.transform import AffineTransform

from ai.landmark_detection.delf_querier import DELFQuerier
from ai.landmark_detection.domain.Descriptor import Descriptor
from ai.landmark_detection.domain.Entity import sqlite_db
from ai.landmark_detection.domain.Landmark import Landmark
from ai.landmark_detection.domain.Location import Location

from ai.landmark_detection.environment import DELF_IMG_QUERY_SIZE, DELF_PICKLE_PATH, LOCATION_DISCRETE_VALUE_GROUP, \
    DESCRIPTORS_DISCRETE_VALUE_GROUP
from ai.landmark_detection.make_db import to_discrete_value

DISTANCE_THRESHOLD = 0.8
K = 10
NO_PROCESSES = 4


class QueryLandmark:
    def __init__(self, name, link, locations: np.ndarray, descriptors: np.ndarray):
        self.__name = name
        self.__link = link
        self.__locations = locations
        self.__descriptors = descriptors

    @property
    def name(self) -> str:
        return self.__name

    @property
    def link(self) -> str:
        return self.__link

    @property
    def locations(self) -> np.ndarray:
        return self.__locations

    @property
    def descriptors(self) -> np.ndarray:
        return self.__descriptors

    def to_dict(self):
        return {
            'name': self.__name,
            'link': self.__link,
            'locations': self.__locations.tolist(),
            'descriptors': self.__descriptors.tolist()
        }


def load_from_db(landmarks: List[Landmark]) -> List[QueryLandmark]:
    query_landmarks: List[QueryLandmark] = []
    for landmark in landmarks:
        locations = []
        for location_id in landmark.location_ids.split(','):
            for location in Location.select().where(Location.location_id == int(location_id)):
                if location is not None:
                    locations.append([float(location.y), float(location.x)])
                    break

        descriptor_features = []
        for descriptor_id in landmark.descriptor_ids.split(','):
            for descriptor in Descriptor.select().where(Descriptor.descriptor_id == int(descriptor_id)):
                if descriptor is not None:
                    descriptor_features.append([float(feature) for feature in descriptor.feature40.split(',')])
                    break

        query_landmarks.append(
            QueryLandmark(
                landmark.name,
                landmark.wiki_link,
                np.array(locations),
                np.array(descriptor_features)
            ))

    return query_landmarks


# noinspection PyMethodMayBeStatic
class LandmarkService:

    def __init__(self, delf_querier=DELFQuerier()):
        self.__delf_querier = delf_querier
        self.__landmarks: List[QueryLandmark] = []
        self.__locations_concatenated = np.array([])
        self.__descriptors_concatenated = np.array([])
        self.__accumulated_index_boundaries = np.array([])

        if Path(DELF_PICKLE_PATH).exists():
            self.__load_pickle()
        else:
            if sqlite_db.is_closed():
                sqlite_db.connect()
            self.__load_from_db_wrapper()
            self.__write_pickle()

        self.__concatenate_data()
        self.__cKDTree = cKDTree(self.__descriptors_concatenated)

    def __load_pickle(self):
        pickle_object = pickle.load(open(DELF_PICKLE_PATH, "rb"))
        for query_landmark in pickle_object['query_landmarks']:
            self.__landmarks.append(QueryLandmark(
                name=query_landmark['name'],
                link=query_landmark['link'],
                locations=np.array(query_landmark['locations']),
                descriptors=np.array(query_landmark['descriptors'])
            ))

    def __write_pickle(self):
        pickle_object = {'query_landmarks': []}
        for landmark in self.__landmarks:
            pickle_object['query_landmarks'].append(landmark.to_dict())

        pickle.dump(pickle_object, open(DELF_PICKLE_PATH, 'wb'))

    def __load_from_db_wrapper(self):
        landmarks = [landmark for landmark in Landmark.select()]
        batch_size = len(landmarks) // NO_PROCESSES
        with concurrent.futures.ProcessPoolExecutor(max_workers=NO_PROCESSES) as executor:
            futures = []
            for process_index in range(0, NO_PROCESSES):
                upper_bound = process_index + 1
                if upper_bound * batch_size > len(landmarks):
                    upper_bound = len(landmarks)

                futures.append(
                    executor.submit(load_from_db, landmarks[process_index * batch_size:upper_bound * batch_size]))

            for feature in concurrent.futures.as_completed(futures):
                self.__landmarks.extend(feature.result())

    def __concatenate_data(self):
        self.__locations_concatenated = np.concatenate([landmark.locations for landmark in self.__landmarks])
        self.__descriptors_concatenated = np.concatenate([landmark.descriptors for landmark in self.__landmarks])
        self.__accumulated_index_boundaries = list(
            accumulate([landmark.locations.shape[0] for landmark in self.__landmarks]))

    @property
    def landmarks(self):
        return self.__landmarks

    def __decode_img(self, img: str):
        tf_img = base64.decodebytes(img.encode('utf-8'))
        tf_img = tf.io.decode_image(tf_img, channels=3)
        tf_img = tf.image.resize(tf_img, DELF_IMG_QUERY_SIZE)
        return tf_img

    def __get_interval_space(self, index):
        if index > len(self.__accumulated_index_boundaries) - 1:
            return None

        if index == 0:
            index_start = 0
        else:
            index_start = self.__accumulated_index_boundaries[index - 1]

        index_finish = self.__accumulated_index_boundaries[index]
        return np.arange(index_start, index_finish)

    def __get_source_n_destination_coordinates(self, index, k_nearest_indexes, delf_locations):
        interval_space = self.__get_interval_space(index)
        local = []
        query = []
        for i, row in enumerate(k_nearest_indexes):
            for k_nearest_index in row:
                if k_nearest_index in interval_space:
                    local.append(self.__locations_concatenated[k_nearest_index])
                    query.append(delf_locations[i])

        return np.array(local), np.array(query)

    def __locations_to_discrete(self, locations):
        discrete_locations = []
        for (x, y) in locations:
            x_ = to_discrete_value(x, LOCATION_DISCRETE_VALUE_GROUP)
            y_ = to_discrete_value(y, LOCATION_DISCRETE_VALUE_GROUP)
            discrete_locations.append((y_, x_))  # Swapped them when building db

        return np.array(discrete_locations)

    def __descriptors_to_discrete(self, descriptors):
        discrete_descriptors = []
        for feature40 in descriptors:
            feature40_ = []
            for feature in feature40:
                feature40_.append(to_discrete_value(feature, DESCRIPTORS_DISCRETE_VALUE_GROUP))

            discrete_descriptors.append(feature40_)

        return np.array(discrete_descriptors)

    def predict(self, image: str) -> QueryLandmark:
        img = self.__decode_img(image)  # Prepare image for querying
        delf_output = self.__delf_querier.query(img)  # Call DELF
        locations = self.__locations_to_discrete(delf_output['locations'])
        descriptors = self.__descriptors_to_discrete(delf_output['descriptors'])
        distances, indexes = self.__cKDTree.query(descriptors, distance_upper_bound=DISTANCE_THRESHOLD,
                                                  k=K, n_jobs=-1)  # Query cKDTree using all processors

        unique_indexes = np.array(list(set(indexes.flatten())))
        unique_indexes.sort()  # Unique & Flatten the K, indexes
        if unique_indexes[-1] == self.__descriptors_concatenated.shape[0]:
            unique_indexes = unique_indexes[:-1]

        unique_candidate_indexes = np.array(list(set(
            [np.argmax([np.array(self.__accumulated_index_boundaries) > index]) for index in
             unique_indexes])))  # Get candidate indexes

        best_index = 0
        best_no_inliers = float('-inf')
        for candidate_index in unique_candidate_indexes:
            # source & destination coordinates
            local, query = self.__get_source_n_destination_coordinates(candidate_index, indexes, locations)
            if len(local) < 9 or len(query) < 9:
                continue

            _, inliers = ransac(
                (local, query),
                AffineTransform,
                min_samples=3,
                residual_threshold=20,
                max_trials=1000
            )

            if inliers is None or len(inliers) == 0:  # no inliers found
                continue

            no_inliers = sum(inliers)
            if no_inliers > best_no_inliers:
                best_no_inliers = no_inliers
                best_index = candidate_index

        return self.__landmarks[best_index]
