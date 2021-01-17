import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib as pl
import os

from ai.landscape_detection.environment import TRAIN_PATH, TEST_PATH, MODEL_PATH

BATCH_SIZE = 32
IMG_HEIGHT = 150
IMG_WIDTH = 150
AUTO_TUNE = tf.data.experimental.AUTOTUNE
SIZE = 100
EPOCHS = 10
CLASS_NAMES = ['buildings', 'forest', 'mountain', 'sea', 'street']
NO_CLASSES = 5


def create_model():
    return Sequential([
        layers.experimental.preprocessing.RandomFlip("horizontal", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        layers.experimental.preprocessing.RandomRotation(0.1),
        layers.experimental.preprocessing.RandomZoom(0.1),
        layers.experimental.preprocessing.Rescaling(1. / 255),
        layers.Conv2D(16, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D(pool_size=(2, 2)),
        layers.Dropout(0.2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(NO_CLASSES)
    ])


if __name__ == '__main__':
    train_path = os.path.join(os.getcwd(), TRAIN_PATH)
    train_dir = pl.Path(train_path)
    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        directory=train_dir,
        image_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE
    )

    test_path = os.path.join(os.getcwd(), TEST_PATH)
    test_dir = pl.Path(test_path)
    test_ds = tf.keras.preprocessing.image_dataset_from_directory(
        directory=test_dir,
        image_size=(IMG_HEIGHT, IMG_WIDTH),
        batch_size=BATCH_SIZE
    )

    train_ds = train_ds.cache().shuffle(SIZE).prefetch(buffer_size=AUTO_TUNE)
    test_ds = test_ds.cache().prefetch(buffer_size=AUTO_TUNE)

    model = create_model()
    model.compile(
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        optimizer='adam',
        metrics=['accuracy']
    )

    model.summary()

    history = model.fit(
        train_ds,
        validation_data=test_ds,
        epochs=EPOCHS
    )

    # PLOT
    accuracy = history.history['accuracy']
    validation_accuracy = history.history['val_accuracy']

    loss = history.history['loss']
    validation_loss = history.history['val_loss']

    epochs_range = range(EPOCHS)

    plt.figure(figsize=(8, 8))

    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, accuracy, label='Training Accuracy')
    plt.plot(epochs_range, validation_accuracy, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.title('Training and Validation Accuracy')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, loss, label='Training Loss')
    plt.plot(epochs_range, validation_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.title('Training and Validation Loss')
    plt.show()

    # Save model
    model.save_weights(os.path.join(os.getcwd(), MODEL_PATH))
