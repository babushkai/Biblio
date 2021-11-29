import  tensorflow as tf

#Binary Class Classification
#Cross Entropy
#Loss = ytrue(-log(ypred)) + (1 - ytrue)(-log(1 - ypred))

y_true = [0, 1, 0, 0]
y_pred = [0.6, 0.3, 0.2, 0.8] 
bce = tf.keras.losses.BinaryCrossentropy(from_logits=False)
bce(y_true, y_pred).numpy()

#Multi Class Classification
#Softmax Classification(Categorical Cross Entropy)
#It forces to have one best class
#Loss = \Sum_{i=1}^n ytrue(-log(ypred)) + (1 - ytrue)(-log(1 - ypred))

#Multi Label Classification
#Sum of Sigmoid Activation Function
# Add sigmoid to every output node to predict the unique probability of each class
x = tf.constant([-20, -1.0, 0.0, 1.0, 20], dtype = tf.float32)
tf.keras.activations.sigmoid(x).numpy().sum()