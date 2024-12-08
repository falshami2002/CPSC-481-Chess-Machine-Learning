import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.preprocessing.image import ImageDataGenerator

# Load the dataset
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
        'C:\\Users\\Firas\\Documents\\GitHub\\chess-ai\\chess-recognition\\board-data\\testing',
        target_size=(64, 64),
        batch_size=32,
        class_mode='categorical')

# Load model
model = keras.models.load_model('boardModel.h5')

# Test
loss, accuracy = model.evaluate(test_generator)

# Print loss and accuracy
print(loss, accuracy)
