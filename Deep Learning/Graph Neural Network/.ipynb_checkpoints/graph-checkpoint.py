import tensorflow as tf
import tensorflow_gnn as tfgnn
# https://github.com/tensorflow/gnn

# Model hyper-parameters:
h_dims = {'user': 256, 'movie': 64, 'genre': 128}

# Model builder initialization:
gnn = tfgnn.keras.ConvGNNBuilder(
  lambda edge_set_name: WeightedSumConvolution(),
  lambda node_set_name: tfgnn.keras.layers.NextStateFromConcat(
     tf.keras.layers.Dense(h_dims[node_set_name]))
)

# Two rounds of message passing to target node sets:
model = tf.keras.models.Sequential([
    gnn.Convolve({'genre'}),  # sends messages from movie to genre
    gnn.Convolve({'user'}),  # sends messages from movie and genre to users
    tfgnn.keras.layers.Readout(node_set_name="user"),
    tf.keras.layers.Dense(1)
])