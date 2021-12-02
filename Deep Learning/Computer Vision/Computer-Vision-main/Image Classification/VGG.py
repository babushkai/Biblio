import keras

class VGG16(keras.Model):
    def model(self):
        inputs = keras.Input(224, 224, 3)
        # Block 1
        self.x = self.layers().Conv2D(64//self.factor, (3,3), padding="same")(inputs)
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(64//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().MaxPooling((2,2), strides=(2,2))(self.x)
        
        # Block 2
        self.x = self.layers().Conv2D(128//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)        
        self.x = self.layers().Conv2D(128//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().MaxPooling((2,2), strides=(2,2))(self.x)
        
        # Block 3
        self.x = self.layers().Conv2D(256//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(256//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(256//self.factor, (3,3), padding="same")       
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().MaxPooling((2,2), strides=(2,2))(self.x)
        
        # Block 4
        self.x = self.layers().Conv2D(512//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(512//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(512//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().MaxPooling((2,2), strides=(2,2))(self.x)      
        
        # Block 5
        self.x = self.layers().Conv2D(512//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(512//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Conv2D(512//self.factor, (3,3), padding="same")
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().MaxPooling((2,2), strides=(2,2))(self.x)  
        
        # Classification block
        self.x = self.layers().Flatten()(self.x)
        self.x = self.layers().Dense(4096//self.factor)(self.x)
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Dense(4096//self.factor)(self.x)
        self.x = self.layers().Activation('relu')(self.x)
        self.x = self.layers().Dense(1000)(self.x)

vgg = VGG16()