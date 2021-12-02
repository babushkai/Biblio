import numpy as np
import tensorflow as tf
from keras.layers import Input, Add, Dense, Activation, ZeroPadding2D, BatchNormalization, Flatten, Conv2D, AveragePooling2D, MaxPooling2D
from keras.models import Model, load_model
from keras.initializers import glorot_uniform
from keras.datasets import cifar10

(X_train, y_train), (X_test, y_test) = cifar10.load_data()

mean = np.mean(X_train)
std = np.mean(X_train)
X_train = (X_train - mean)/(std+1e-7)
X_test = (X_test - mean)/(std+1e-7)


from keras.utils import np_utils

num_classes = 10
y_train = np_utils.to_categorical(y_train, num_classes)
y_test = np_utils.to_categorical(y_test, num_classes)

w,h = 32,32
input_shape = (w,h, 3)

# from resnet import ResNet50
# res = ResNet50(input_shape, num_classes)

from keras import Sequential
nn = Sequential()
nn.add(Conv2D(32, 2, input_shape=(32,32,3), activation="relu"))
nn.add(MaxPooling2D())
nn.add(Conv2D(64, 2, activation="relu"))
nn.add(MaxPooling2D())
nn.add(Flatten())
nn.add(Dense(256))
nn.add(Dense(10, activation="sigmoid"))
nn.compile(optimizer="adam", metrics="accuracy", loss="categorical_crossentropy")
nn.fit(X_train, y_train, epochs=5)

nn.predict(X_test)

predictions = nn.predict(X_test)
classes = np.argmax(predictions, axis=1)

import matplotlib.pyplot as plt
plt.figure(figsize=(40, 40))
for index, (image, label) in enumerate(zip(X_test[:10], classes)):
    plt.subplot(len(X_test[:10])/2,len(X_test[:10])/2, index+1)
    plt.imshow(np.reshape(image,(32,32,3)), cmap=plt.cm.gray)
    plt.title('Training: {}\n'.format(label), fontsize = 100)
    plt.tight_layout()