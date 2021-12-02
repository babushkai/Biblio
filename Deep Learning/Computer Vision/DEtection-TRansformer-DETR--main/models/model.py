import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.layers import Input, Dense

class BaseModel:
    def __init__(self, input_shape=(224, 224, 3),factor=1, ):
        inputs = tf.keras.layers.Input(shape=input_shape)
        print(inputs)
        self.x = inputs
        self.deploy()
        self.factor = factor
        self.model = Model(inputs, self.x)
        
    
class Linear(tf.keras.layers.Layer):
    '''
    Use this custom layer instead of tf.keras.layers.Dense to allow
    loading converted PyTorch Dense weights that have shape (output_dim, input_dim)
    '''
    def __init__(self, output_dim, **kwargs):
        super().__init__(**kwargs)
        self.output_dim = output_dim


    def build(self, input_shape):
        self.kernel = self.add_weight(name='kernel',
                                      shape=[self.output_dim, input_shape[-1]],
                                      initializer='zeros', trainable=True)
        self.bias = self.add_weight(name='bias',
                                    shape=[self.output_dim],
                                    initializer='zeros', trainable=True)

    def call(self, x):
        return tf.matmul(x, self.kernel, transpose_b=True) + self.bias


    def compute_output_shape(self, input_shape):
        return input_shape.as_list()[:-1] + [self.output_dim]

