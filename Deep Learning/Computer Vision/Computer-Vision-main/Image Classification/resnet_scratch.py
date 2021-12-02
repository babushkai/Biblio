import keras
from keras import Model
from keras.layers import Conv2D, Dense, Flatten, MaxPool2D, BatchNormalization, Activation, Input, Add

import tensorflow as tf
x = tf.random.uniform((224,224,3))

def ResNet(input_shape):
    x_input = Input(input_shape)
    x = Conv2D(64, 7)(x_input)
    x = BatchNormalization(axis=3, name='bn_conv1')(x)
    x = Activation('relu')(x)
    x = MaxPool2D((3, 3), strides=(2, 2))(x)
    x_shortcut = x
    x = Conv2D(64, 3, padding="same")(x_shortcut)
    x = BatchNormalization(axis=3)(x_shortcut)
    x = Activation("relu")(x)
    x = Conv2D(64, 3,padding="same")(x)
    x = BatchNormalization(axis=3)(x)
    x = Activation("relu")(x)
    x = Conv2D(64, 3, padding="same")(x)
    x = BatchNormalization(axis=3)(x)
    x = Activation("relu")(x)
    x = Add()([x, x_shortcut])        
    x = Activation("relu")(x)
    return Model(x_input, x, "resnet")
        
