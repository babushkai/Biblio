import  tensorflow as tf

#Binary Class Classification
#Activation: Sigmoid
#Loss: Cross Entropy 
#ytrue(-log(ypred)) + (1 - ytrue)(-log(1 - ypred))

y_true = [0, 1, 0, 0]
y_pred = [0.6, 0.3, 0.2, 0.8] 
bce = tf.keras.losses.BinaryCrossentropy(from_logits=False)
bce(y_true, y_pred).numpy()


#Multi Class Classification
#It forces to have one best class
#Activation: Softmax
#Loss: Categorical Cross Entropy
#\Sum_{i=1}^n ytrue(-log(ypred)) + (1 - ytrue)(-log(1 - ypred))

from scipy.special import softmax
data = [1,2,3,4,5]
softmax(data)

#Multi Label Classification
#Sum of Sigmoid Activation Function
# Add sigmoid to every output node to predict the unique probability of each class
x = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32)
tf.keras.activations.sigmoid(x).numpy().sum()

