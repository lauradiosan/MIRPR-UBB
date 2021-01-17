import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pathlib as pl
import os

from ai.landscape_detection.environment import MODEL_PATH, PREDICT_PATH
from ai.landscape_detection.make_model import create_model, IMG_HEIGHT, IMG_WIDTH, CLASS_NAMES


def load_model(model_path: str = os.path.join(pl.Path(__file__).parent.absolute(), MODEL_PATH)):
    model = create_model()
    model.load_weights(model_path)
    return model


if __name__ == '__main__':
    model = load_model()
    predict_path = os.path.join(os.getcwd(), PREDICT_PATH, '420.jpg')
    img = tf.keras.preprocessing.image.load_img(
        predict_path,
        target_size=(IMG_HEIGHT, IMG_WIDTH)
    )
    img = tf.keras.preprocessing.image.img_to_array(img)
    img = tf.expand_dims(img, 0)
    predictions = model.predict(img)
    score = tf.nn.softmax(predictions[0])
    result = CLASS_NAMES[np.argmax(score)]
    print(np.max(score))
    print(result)
