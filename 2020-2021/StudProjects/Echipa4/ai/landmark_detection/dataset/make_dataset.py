import os
import requests
import shutil
import hashlib
import tarfile
import pathlib as pl
import sys
import threading
from PIL import Image

# DATASET
INDEX = 'https://s3.amazonaws.com/google-landmark/metadata/index.csv'
INDEX_FILE = 'index.csv'
INDEX_IMAGE_TO_LANDMARK = 'https://s3.amazonaws.com/google-landmark/metadata/index_image_to_landmark.csv'
INDEX_IMAGE_TO_LANDMARK_FILE = 'index_image_to_landmark.csv'
INDEX_LABEL_TO_CATEGORY = 'https://s3.amazonaws.com/google-landmark/metadata/index_label_to_category.csv'
INDEX_LABEL_TO_CATEGORY_FILE = 'index_label_to_category.csv'

DATA_PREFIX = 'https://s3.amazonaws.com/google-landmark/index/'
DATA_SUFFIX = 'images_{:03d}.tar'
DATA_FOLDER = 'data'

# MD5
INDEX_MD5_PREFIX = 'https://s3.amazonaws.com/google-landmark/md5sum/index/md5.'
INDEX_MD5_SUFFIX = 'images_{:03d}.txt'

# NUMBER OF SETS
NO_SETS = 100

DELF_IMG_QUERY_SIZE = [255, 255]
NO_THREADS = 8


def __get_req_write_file(url, path):
    with requests.get(url, stream=True) as req:
        with open(path, 'wb') as fout:
            shutil.copyfileobj(req.raw, fout)


def __generate_md5_hash(path):
    hash_md5 = hashlib.md5()
    with open(path, 'rb') as fin:
        for chunk in iter(lambda: fin.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def __delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def fetch_csvs():
    for _set in [
        [INDEX, INDEX_FILE],
        [INDEX_IMAGE_TO_LANDMARK, INDEX_IMAGE_TO_LANDMARK_FILE],
        [INDEX_LABEL_TO_CATEGORY, INDEX_LABEL_TO_CATEGORY_FILE]
    ]:
        __get_req_write_file(_set[0], os.path.join(os.getcwd(), _set[1]))


def fetch_md5(index):
    suffix = INDEX_MD5_SUFFIX.format(index)
    path = os.path.join(os.getcwd(), suffix)
    __get_req_write_file(f"{INDEX_MD5_PREFIX}{suffix}", path)
    md5_hash = None
    with open(path, mode='r') as fin:
        md5_hash = fin.readline().strip().rstrip().split(' ')[0]

    __delete_file(path)
    return md5_hash


def __resize_jpgs():
    def process(paths):
        for img_path in paths:
            with Image.open(img_path) as img:
                if img.size != DELF_IMG_QUERY_SIZE:
                    img = img.resize(DELF_IMG_QUERY_SIZE)
                    img.save(img_path)

    data_dir_path = pl.Path(os.path.join(os.getcwd(), DATA_FOLDER))
    img_paths = list(data_dir_path.glob('**/*.jpg'))
    batch_size = len(img_paths) // NO_THREADS
    threads = []
    for i in range(NO_THREADS):
        start = i * batch_size
        end = (i + 1) * batch_size if i + 1 < NO_THREADS else len(img_paths)
        t = threading.Thread(target=process, args=[img_paths[start:end]])
        t.start()
        threads.append(t)

    for i in range(NO_THREADS):
        threads[i].join()


def fetch_imgs(offset=0):
    data_dir_path = os.path.join(os.getcwd(), DATA_FOLDER)
    if not os.path.exists(data_dir_path):
        os.mkdir(data_dir_path)

    for index in range(offset, NO_SETS):
        # Get
        suffix = DATA_SUFFIX.format(index)
        path = os.path.join(data_dir_path, suffix)
        __get_req_write_file(f"{DATA_PREFIX}{suffix}", path)

        # Hash
        remote_md5_hash = fetch_md5(index)

        # Gen hash
        local_md5_hash = __generate_md5_hash(path)
        if not remote_md5_hash:
            print(
                f"Couldn't fetch the remote hash for file {suffix}. Continuing...")
        elif remote_md5_hash != local_md5_hash:
            raise RuntimeError(f'{suffix} file is corrupted!')

        print(f"Hashes match for file {suffix}! Unzipping...")
        with tarfile.TarFile(path, 'r') as tar_ref:
            tar_ref.extractall(data_dir_path)

        __delete_file(path)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        __resize_jpgs()
        exit(0)

    offset = int(sys.argv[1])
    print(f'offset: {offset}')
    fetch_csvs()
    fetch_imgs(offset)
