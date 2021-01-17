import tensorflow as tf
import tensorflow_hub as hub

from ai.landmark_detection.environment import DELF_HUB_MODULE_URL, DELF_IMAGE_SCALES, DELF_SCORE_THRESHOLD, \
    DELF_MAX_FEATURE_NUMBER, DELF_IMG_QUERY_SIZE


class DELFQuerier:
    def __init__(self):
        self.__delf_hub = hub.load(DELF_HUB_MODULE_URL)
        self.__image_scales = tf.constant(DELF_IMAGE_SCALES)
        self.__score_threshold = tf.constant(DELF_SCORE_THRESHOLD)
        self.__max_feature_num = tf.constant(DELF_MAX_FEATURE_NUMBER)

    def prepare_image(self, image: bytes):
        image = tf.image.decode_jpeg(image, channels=3)
        image = tf.image.convert_image_dtype(image, tf.float32)
        image = tf.image.resize(image, DELF_IMG_QUERY_SIZE, antialias=True)
        return image

    def query(self, image):
        delf_output = self.__delf_hub.signatures['default'](
            image=image,
            image_scales=self.__image_scales,
            score_threshold=self.__score_threshold,
            max_feature_num=self.__max_feature_num
        )

        return {
            'locations': delf_output['locations'].numpy(),
            'descriptors': delf_output['descriptors'].numpy()
        }
