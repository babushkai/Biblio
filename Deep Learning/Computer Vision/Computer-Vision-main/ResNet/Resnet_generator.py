import tensorflow as tf
from tensorflow.keras.layers import ZeroPadding2D, Conv2D, ReLU, MaxPool2D, MaxPooling2D, BatchNormalization, Activation, Add, GlobalAveragePooling2D, Dense

from keras.initializers import glorot_uniform

weight_init = tf.keras.initializers.VarianceScaling()
weight_regularizer = tf.keras.regularizers.l2(l=0.0001)

is_channel_fist = False


class BaseModel:
    def __init__(self, input_shape=(224, 224, 3),factor=1, ):
        inputs = tf.keras.layers.Input(shape=input_shape)
        print(inputs)
        self.x = inputs
        self.deploy()
        self.factor = factor
        self.model = tf.keras.Model(inputs, self.x)
        
    


class ResNet(BaseModel):
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.label_dim = 10

  def get_residual_layer(self):
    n_to_residual = {
        10: [1, 1, 1, 1],
        12: [1, 1, 2, 1],
        14: [1, 2, 2, 1],
        16: [2, 2, 2, 1],
        18: [2, 2, 2, 2],
        20: [2, 2, 3, 2],
        22: [2, 3, 3, 2],
        24: [2, 3, 4, 2],
        26: [2, 3, 5, 2],
        28: [2, 3, 6, 2],
        30: [2, 4, 6, 2],
        32: [3, 4, 6, 2],
        34: [3, 4, 6, 3],
        50: [3, 4, 6, 3],
        101: [3, 4, 23, 3],
        152: [3, 8, 36, 3],
    }
    return n_to_residual[self.res_n]

  def deploy(self):
    if is_channel_fist:
      self.x = tf.transpose(self.x, [0, 3, 1, 2])
      tf.keras.backend.set_image_data_format('channels_first')

    if self.res_n < 50:
      residual_block = self.resblock
    else:
      residual_block = self.bottle_resblock
    residual_list = self.get_residual_layer()
    ch = 64
    
    # block 0
    #kernel_initializer= glorot_uniform
    self.x = Conv2D(int(ch), kernel_size=(7,7), strides=(2,2), kernel_initializer=glorot_uniform(seed=42), kernel_regularizer=weight_regularizer, padding="valid", name='conv_initial')(self.x)
    self.x = BatchNormalization(axis=3, name= "norm")(self.x)
    self.shortcut = Activation('relu', name="shortcut")(self.x)
    self.shortcut = MaxPooling2D((3,3), (2,2))(self.shortcut)
    
    # block 1
    residual_block(channels=int(ch), downsample=False, block=f'Stage1_0')
    for i in range(1, residual_list[0]):
      residual_block(channels=int(ch), downsample=False, block=f'Stage1_{i}')
    
    # block 2
    residual_block(channels=int(ch) * 2, downsample=True, block='Stage2_0')
    for i in range(1, residual_list[1]):
      residual_block(channels=int(ch) * 2, downsample=False, block=f'Stage2_{i}')
    
    # block 3
    residual_block(channels=int(ch) * 4, downsample=True, block='Stage3_0')
    for i in range(1, residual_list[2]):
      residual_block(channels=int(ch) * 4, downsample=False, block=f'Stage3_{i}')
    
    # block 4
    residual_block(channels=int(ch) * 8, downsample=True, block='Stage4_0')
    for i in range(1, residual_list[3]):
      residual_block(channels=int(ch) * 8, downsample=False, block=f'Stage4_{i}')
    
    # block 5
    channels=int(ch) * 8
    self.x = Conv2D(channels * 4, 1, 1, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=True, name="conv")(self.shortcut)
    self.x = Add(name="add")([self.x, self.shortcut])
    self.x = BatchNormalization(name='batch_norm_last')(self.x)
    self.x = Activation('relu', name='relu_last')(self.x)
    self.x = GlobalAveragePooling2D()(self.x) # For avoid overfitting
    self.x = Dense(10, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer, use_bias=True,  name='logit')(self.x)

  def bottle_resblock(self, channels, use_bias=True, downsample=False, block='Stage'):
    self.x = Conv2D(channels, 1, 1, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=use_bias, name=block+ "/conv_a")(self.shortcut)
    self.x = BatchNormalization(name=block + "/norm_a")(self.x)
    self.x = Activation('relu', name=block + "/act_a")(self.x)

    self.x = Conv2D(channels, 3, 1, 'same', kernel_initializer=weight_init,
                             kernel_regularizer=weight_regularizer, use_bias=use_bias, name=block+"/conv_b")(self.x)
    self.x = BatchNormalization(name=block+"/norm_b")(self.x)
    self.x = Activation('relu', name=block+"/act_b")(self.x)
    
    self.x = Conv2D(channels * 4, 1, 1, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=use_bias, name=block+"/convc")(self.x)   
    self.x = BatchNormalization(name=block + "/normc")(self.x)

    if downsample:
      self.shortcut = Conv2D(channels * 4, 1, 2, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                               use_bias=use_bias, name=block+"/shortcut")(self.shortcut)        
      self.shortcut = BatchNormalization(name=block + '/snorm')(self.shortcut)
    
    self.x = Add(name=block+"/add")([self.x, self.shortcut])
    self.shortcut = Activation('relu', name=block + "/act")(self.x)

  def resblock(self, channels, use_bias=True, downsample=False, block='Stage'):
    x_init = self.x
    self.x =BatchNormalization(name=block_name + '/batch_norm_0')(self.x)
    self.x = Activation('relu', name=block_name + '/relu_0')(self.x)
    if downsample:
      self.x = Conv2D(channels, 3, 2, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                             use_bias=use_bias, padding='same')(self.x)
      x_init = Conv2D(channels, 1, 2, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                             use_bias=use_bias, padding='same')(x_init)
    else:
      self.x = Conv2D(channels, 3, 1, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                             use_bias=use_bias, padding='same')(self.x)
    self.x = BatchNormalization(name=block_name + '/batch_norm_1')(self.x)
    self.x = Activation('relu', name=block_name + '/relu_1')(self.x)
    self.x = Conv2D(channels, 3, 1, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=use_bias, padding='same')(self.x)
    self.x = Add()([self.x, x_init])

class ResNet50(ResNet):
  def __init__(self, *args, **kwargs):
    self.res_n = 50
    super().__init__(*args, **kwargs)
    
    
class ResNet101(ResNet):
  def __init__(self, *args, **kwargs):
    self.res_n = 101
    super().__init__(*args, **kwargs)
    

