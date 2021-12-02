import tensorflow as tf
from model import BaseModel
from tensorflow.keras.layers import ZeroPadding2D, Conv2D, ReLU, MaxPool2D, MaxPooling2D, BatchNormalization, Activation, Add, GlobalAveragePooling2D, Dense

weight_init = tf.keras.initializers.VarianceScaling()
weight_regularizer = tf.keras.regularizers.l2(l=0.0001)

is_channel_fist = False


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
    self.x = Conv2D(int(ch), 7, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer, padding="same", name='conv')(self.x)
    self.x = MaxPooling2D(pool_size=3, strides=2)(self.x)
    for i in range(residual_list[0]):
      residual_block(channels=int(ch), downsample=False, block_name='resblock0_' + str(i))
    # block 1
    residual_block(channels=int(ch) * 2, downsample=True, block_name='resblock1_0')
    for i in range(1, residual_list[1]):
      residual_block(channels=int(ch) * 2, downsample=False, block_name='resblock1_' + str(i))
    # block 2
    residual_block(channels=int(ch) * 4, downsample=True, block_name='resblock2_0')
    for i in range(1, residual_list[2]):
      residual_block(channels=int(ch) * 4, downsample=False, block_name='resblock2_' + str(i))
    # block 3
    residual_block(channels=int(ch) * 8, downsample=True, block_name='resblock_3_0')
    for i in range(1, residual_list[3]):
      residual_block(channels=int(ch) * 8, downsample=False, block_name='resblock_3_' + str(i))
    # block 4
    self.x = BatchNormalization(name='batch_norm_last')(self.x)
    self.x = Activation('relu', name='relu_last')(self.x)
    self.x = GlobalAveragePooling2D()(self.x)
    self.x = Dense(10, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer, use_bias=True,  name='logit')(self.x)

  def resblock(self, channels, use_bias=True, downsample=False, block_name='resblock'):
    x_init = self.x
    self.x =BatchNormalization(name=block_name + '/batch_norm_0')(self.x)
    self.x = Activation('relu', name=block_name + '/relu_0')(self.x)
    if downsample:
      self.x = Conv2D(channels, 3, 2, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                             use_bias=use_bias, padding='same', name=block_name + '/conv_0')(self.x)
      x_init = Conv2D(channels, 1, 2, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                             use_bias=use_bias, padding='same', name=block_name + '/conv_init')(x_init)
    else:
      self.x = Conv2D(channels, 3, 1, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                             use_bias=use_bias, padding='same', name=block_name + '/conv_0')(self.x)
    self.x = BatchNormalization(name=block_name + '/batch_norm_1')(self.x)
    self.x = Activation('relu', name=block_name + '/relu_1')(self.x)
    self.x = Conv2D(channels, 3, 1, kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=use_bias, padding='same', name=block_name + '/conv_1')(self.x)
    self.x = Add()([self.x, x_init])

  def bottle_resblock(self, channels, use_bias=True, downsample=False, block_name='bottle_resblock'):
    
    self.x = BatchNormalization(name=block_name + '/batch_norm_1x1_front')(self.x)
    shortcut = Activation('relu', name=block_name + '/relu_1x1_front')(self.x)
    self.x = Conv2D(channels, 1, 1, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=use_bias, name=block_name + '/conv_1x1_front')(shortcut)
    self.x = BatchNormalization(name=block_name + '/batch_norm_3x3')(self.x)
    self.x = Activation('relu', name=block_name + '/relu_3x3')(self.x)
    if downsample:
      self.x = Conv2D(channels, 3, 2, 'same', kernel_initializer=weight_init,
                             kernel_regularizer=weight_regularizer, use_bias=use_bias, name=block_name + '/conv_0')(self.x)
      shortcut = Conv2D(channels * 4, 1, 2, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                               use_bias=use_bias, name=block_name + '/conv_init')(shortcut)
    else:
      self.x = Conv2D(channels, 3, 1, 'same', kernel_initializer=weight_init,
                             kernel_regularizer=weight_regularizer, use_bias=use_bias, name=block_name + '/conv_0')(self.x)
      shortcut = Conv2D(channels * 4, 1, 1, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                               use_bias=use_bias, name=block_name + '/conv_init')(shortcut)
    self.x = BatchNormalization(name=block_name + '/batch_norm_1x1_back')(self.x)
    self.x = Activation('relu', name=block_name + '/relu_1x1_back')(self.x)
    self.x = Conv2D(channels * 4, 1, 1, 'same', kernel_initializer=weight_init, kernel_regularizer=weight_regularizer,
                           use_bias=use_bias, name=block_name + '/conv_1x1_back')(self.x)
    self.x = Add()([self.x, shortcut])



class ResNet50(ResNet):
  def __init__(self, *args, **kwargs):
    self.res_n = 50
    super().__init__(*args, **kwargs)
    
    
class ResNet101(ResNet):
  def __init__(self, *args, **kwargs):
    self.res_n = 101
    super().__init__(*args, **kwargs)
    

