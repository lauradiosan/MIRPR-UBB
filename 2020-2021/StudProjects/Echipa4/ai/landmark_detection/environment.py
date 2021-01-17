from pathlib import Path
import pandas as pd

# DELF
DELF_HUB_MODULE_URL = 'https://tfhub.dev/google/delf/1'
DELF_IMAGE_SCALES = [0.25, 0.3536, 0.5, 0.7071, 1.0, 1.4142, 2.0]
DELF_SCORE_THRESHOLD = 100.0
DELF_MAX_FEATURE_NUMBER = 100
DELF_IMG_QUERY_SIZE = [255, 255]
LOCATION_DISCRETE_VALUE_GROUP = pd.interval_range(0.0, 255.0, freq=0.33, closed='left')  # [0, 0.33), [0.33, 0.66) ...
DESCRIPTORS_DISCRETE_VALUE_GROUP = pd.interval_range(-1.0, 1.0, freq=0.001,
                                                     closed='left')  # [0.000, 0.001), [0.001, 0.002) ...

# DATABASE
DB_PATH = Path(__file__).parent.joinpath('db2_lite.db').absolute()

# PICKLE
DELF_PICKLE_PATH = Path(__file__).parent.joinpath('delf_pickle.p').absolute()

# DATASET
DATASET_FOLDER = 'dataset'
INDEX_FILE = 'index.csv'
INDEX_IMAGE_TO_LANDMARK_FILE = 'index_image_to_landmark.csv'
INDEX_LABEL_TO_CATEGORY_FILE = 'index_label_to_category.csv'
DATA_FOLDER = 'data'

if __name__ == '__main__':
    print(DB_PATH)
