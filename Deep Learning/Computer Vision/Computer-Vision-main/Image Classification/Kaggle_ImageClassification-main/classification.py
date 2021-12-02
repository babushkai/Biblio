import os
import sys
import requests
import glob2
from PIL import Image
import cv2
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import tensorflow as tf
import keras

from resnet import ResNet50
from imageReader import Folder

# device_name=tf.test.gpu_device_name()
# if device_name!="/device:GPU:0":
#     raise SystemError("GPU device not found")
# print('Found GPU at: {}'.format(device_name))
# tf.config.list_physical_devices('GPU')

train="C:/Users/daisu/OneDrive/Desktop/Kaggle/Image Classification/archive/seg_train/"
test="C:/Users/daisu/OneDrive/Desktop/Kaggle/Image Classification/archive/seg_test/"
pred="C:/Users/daisu/OneDrive/Desktop/Kaggle/Image Classification/archive/seg_pred/"
# Check the image folders
for folder in os.listdir(train):
    print(folder)


    
image_resize=100
code={"buildings":0,"forest":1,"glacier":2,"mountain":3,"sea":4,"street":5}
def place(n):
    for item in code:
        if n == code[item]:
            return item
        
# Generate train data        
X_train=[]
y_train=[]
for folder in os.listdir(train+"seg_train"):
    files = glob2.glob(pathname=str(train+"seg_train//"+ folder +"/*.jpg"))
    for file in files: 
        train_image=plt.imread(file)
        image_size=cv2.resize(train_image,(image_resize,image_resize))
        X_train.append(list(image_size))
        y_train.append(code[folder])

plt.figure(figsize=(20,20))
for n, i in enumerate ((np.random.randint(0,len(X_train),36))):
    plt.subplot(6,6,n+1)
    plt.imshow(X_train[i])
    plt.title(place(y_train[i]))
    plt.axis("off")        

# Generate test data
X_test=[]
y_test=[]
for folder in os.listdir(test+"seg_test"):
    files = glob2.glob(pathname=str(test+"seg_test//"+ folder +"/*.jpg"))
    for file in files: 
        test_image=plt.imread(file)
        image_size=cv2.resize(test_image,(image_resize,image_resize))
        X_test.append(list(image_size))
        y_test.append(code[folder])
        
print(len(X_test),len(y_test))

plt.figure(figsize=(20,20))
for n, i in enumerate (np.random.randint(0,len(X_test),36)):
    plt.subplot(6,6,n+1)
    plt.imshow(X_test[i])
    plt.axis("off")
    plt.title(place(y_test[i]))
    
# Generate orediction data
X_pred = []
files = glob2.glob(pathname= str(pred + 'seg_pred/*.jpg'))
for file in files: 
    pred_image = cv2.imread(file)
    new_pred_image = cv2.resize(pred_image, (image_resize,image_resize))
    X_pred.append(list(new_pred_image)) 
print(len(X_pred))    

plt.figure(figsize=(20,20))
for n,i in enumerate(np.random.randint(0,len(X_pred),36)):
    plt.subplot(6,6,n+1)
    plt.imshow(X_pred[i])
    plt.axis("off")

X_train=np.array(X_train)
y_train=np.array(y_train)
X_test=np.array(X_test)
y_test=np.array(y_test)
X_pred=np.array(X_pred)

print("The shape of xtrain",X_train.shape)
print("The shape of ytrain ",y_train.shape)
print("The shape of xtest ",X_test.shape)
print("The shape of ytest ",y_test.shape)
print("The shape of xpred",X_pred.shape)

resnet = ResNet50((100,100, 3), 6)


resnet.compile(optimizer="adam",
               loss="sparse_categorical_crossentropy", metrics=["accuracy"])

earlystopping=keras.callbacks.EarlyStopping(patience=10,restore_best_weights=True)
resnet.fit(X_train, y_train, epochs=10, batch_size=200, verbose=1, callbacks=[earlystopping])

loss, accuracy =resnet.evaluate(X_test, y_test)
print(loss, accuracy)
y_pred =resnet.predict(X_pred)

plt.figure(figsize=(20,20))
for n, i in enumerate (np.random.randint(0,len(X_pred),36)):
    plt.subplot(6,6,n+1)
    plt.imshow(X_pred[i])
    plt.axis("off")
    plt.title(place(np.argmax(y_pred[i])))
plt.savefig(os.getcwd()+"/prediction")