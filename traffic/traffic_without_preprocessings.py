import cv2
import sys
import numpy as np
import os
import tensorflow as tf
from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4

def main():
    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )
    print(x_train.shape)

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data with a batch size of 32
    model.fit(x_train, y_train, epochs=EPOCHS, batch_size=32)

    # Evaluate neural network performance
    model.evaluate(x_test, y_test, verbose=2, batch_size=32)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")

def load_data(data_dir):
    images, labels = [], []
    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    for i in range(len(folders)):
        label = int(folders[i])
        new_data_dir = os.path.join(data_dir, folders[i])
        files = [f for f in os.listdir(new_data_dir) if os.path.isfile(os.path.join(new_data_dir, f))]
        for j in range(len(files)):
            file_path = os.path.join(new_data_dir, files[j])
            image = cv2.imread(file_path)
            resized_image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            images.append(resized_image)
            labels.append(label)
    return (images, labels)

def get_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation="relu", kernel_initializer='he_normal', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation="relu", kernel_initializer='he_normal'),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu", kernel_initializer='he_normal'),
        tf.keras.layers.Dropout(0.3),  # Reduced dropout
        tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])
    model.compile(
        optimizer="nadam",  # Changed optimizer to Adam
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model

if __name__ == "__main__":
    main()
