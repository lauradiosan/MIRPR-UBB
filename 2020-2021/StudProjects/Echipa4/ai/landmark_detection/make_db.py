import os
import pandas as pd
import numpy as np

from ai.landmark_detection.domain.Descriptor import Descriptor
from ai.landmark_detection.domain.Entity import sqlite_db
from ai.landmark_detection.domain.Landmark import Landmark
from ai.landmark_detection.domain.Location import Location
from ai.landmark_detection.environment import DATASET_FOLDER, DATA_FOLDER, INDEX_IMAGE_TO_LANDMARK_FILE, INDEX_LABEL_TO_CATEGORY_FILE, \
    LOCATION_DISCRETE_VALUE_GROUP, DESCRIPTORS_DISCRETE_VALUE_GROUP
from ai.landmark_detection.delf_querier import DELFQuerier
from PIL import Image
from io import BytesIO

NO_PROCESSES = 4


def to_discrete_value(value, interval_range):
    value_intervals = np.array(interval_range.contains(value))
    index = np.argwhere(value_intervals == True)[0][0]
    interval = interval_range[index]
    return interval.left


def work(worker_index, landmark_category_df, index_landmark_file):
    querier = DELFQuerier()

    # DFs
    index_landmark_df = pd.read_csv(index_landmark_file)

    no_landmarks = len(landmark_category_df.index)
    index = 1
    # Work
    for landmark_id, landmark_link in zip(landmark_category_df['landmark_id'], landmark_category_df['category']):
        landmark_link = landmark_link.strip('"')
        landmark_name = landmark_link.split('Category:')[1]
        descriptor_ids = []
        location_ids = []
        for image_id in index_landmark_df[index_landmark_df['landmark_id'].isin([landmark_id])]['id']:
            # Find img
            img_path = os.path.join(
                os.getcwd(), DATASET_FOLDER, DATA_FOLDER, image_id[0], image_id[1], image_id[2], f'{image_id}.jpg')

            # Convert img to bytes
            img_byte_arr = BytesIO()
            with Image.open(img_path) as img:
                img.save(img_byte_arr, format=img.format)

            # Convert img to tensor
            img = querier.prepare_image(img_byte_arr.getvalue())

            # Query Delf
            delf_output = querier.query(img)
            locations = []
            descriptors = []
            for (x, y) in delf_output['locations']:
                x_ = to_discrete_value(x, LOCATION_DISCRETE_VALUE_GROUP)
                y_ = to_discrete_value(y, LOCATION_DISCRETE_VALUE_GROUP)
                locations.append({'y': y_, 'x': x_, 'yx_pair': f"{x_},{y_}"})

            for feature40 in delf_output['descriptors']:
                features = []
                for feature in feature40:
                    feature_ = to_discrete_value(feature, DESCRIPTORS_DISCRETE_VALUE_GROUP)
                    features.append(str(feature_))

                features_ = ','.join(features)
                descriptors.append({'feature40': features_})

            with sqlite_db.atomic():
                for location_dict in locations:
                    location = Location.get_or_create(**location_dict)[0]
                    location_ids.append(str(location.location_id))

                for descriptor_dict in descriptors:
                    descriptor = Descriptor.get_or_create(**descriptor_dict)[0]
                    descriptor_ids.append(str(descriptor.descriptor_id))

            break  # Only take 1 image for each landmark. Memory :(

        location_ids = ','.join(location_ids)
        descriptor_ids = ','.join(descriptor_ids)
        Landmark.create(name=landmark_name, wiki_link=landmark_link, location_ids=location_ids,
                        descriptor_ids=descriptor_ids)

        if index % 100 == 0:
            print(f'Worker {worker_index}> Landmark: {index}/{no_landmarks}.')

        index += 1


if __name__ == '__main__':
    # PATHS
    index_landmark_file = os.path.join(
        os.getcwd(), DATASET_FOLDER, INDEX_IMAGE_TO_LANDMARK_FILE)
    landmark_category_file = os.path.join(
        os.getcwd(), DATASET_FOLDER, INDEX_LABEL_TO_CATEGORY_FILE)

    landmark_category_df = pd.read_csv(landmark_category_file)
    batches = np.array_split(landmark_category_df, NO_PROCESSES)
    sqlite_db.connect()

    for i in range(NO_PROCESSES):
        work(i, batches[i], index_landmark_file)
    # with concurrent.futures.ProcessPoolExecutor(max_workers=NO_PROCESSES) as executor:
    #     for i in range(NO_PROCESSES):
    #         executor.submit(work, i, batches[i], index_landmark_file)
