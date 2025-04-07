import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4
dropout_values=[i/10 for i in range(1,10)]
accuracies=[]
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
    
    # mean subtraction
    x_train_mean=np.mean(x_train,axis=0)
    x_train, x_test = x_train.astype(float), x_test.astype(float)
    x_train-=x_train_mean
    x_test-=x_train_mean

    #normaliztion
    std=np.std(x_train,axis=0)
    x_train/=std
    x_test/=std


    for i in range(len(dropout_values)):
    # Get a compiled neural network
        model = get_model(dropout_values[i])

        # Fit model on training data
        model.fit(x_train, y_train, epochs=EPOCHS,batch_size=32)

        # Evaluate neural network performance
        loss,accuracy=model.evaluate(x_test,  y_test, verbose=2,batch_size=32)
        accuracies.append(accuracy)
        
    plt.plot(dropout_values, accuracies)
    plt.xlabel("Dropout Rate")
    plt.ylabel("Accuracy")
    plt.title("Relation of dropout rate with accuracies")
    plt.show()
    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")

def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    images,labels=[],[]
    folders = [f for f in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, f))]
    for i in range(len(folders)):
        label=int(folders[i])
        new_data_dir=os.path.join(data_dir, folders[i])
        files = [f for f in os.listdir(new_data_dir) if os.path.isfile(os.path.join(new_data_dir, f))]
        for j in range(len(files)):
            file_path=os.path.join(new_data_dir,files[j])
            image = cv2.imread(file_path)
            resized_image = cv2.resize(image, (IMG_WIDTH, IMG_HEIGHT))
            images.append(resized_image)
            labels.append(label)
    return (images,labels)


def get_model(dropout_value):
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    model = tf.keras.models.Sequential([

    # Convolutional layer. Learn 32 filters using a 3x3 kernel
    tf.keras.layers.Conv2D(32,(3,3),activation="relu", kernel_initializer='he_normal', input_shape=(IMG_WIDTH, IMG_HEIGHT, 3)),

    # Max-pooling layer, using 2x2 pool size
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),
    tf.keras.layers.Conv2D(64, (3,3), activation="relu",kernel_initializer='he_normal'),

    # Flatten units
    tf.keras.layers.Flatten(),

    # Add a hidden layer with dropout
    tf.keras.layers.Dense(128, activation="relu",kernel_initializer='he_normal'),
    tf.keras.layers.Dropout(dropout_value),

    # Add an output layer with output units for all 10 digits
    tf.keras.layers.Dense(NUM_CATEGORIES, activation="softmax")
    ])
    model.compile(
        optimizer="nadam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )
    return model    

if __name__ == "__main__":
    main()