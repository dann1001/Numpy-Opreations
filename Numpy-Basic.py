import numpy as np 

x = np.array([1 , 2 , 3])

print(np.exp(x))

x= np.array([1 , 2 , 3])
print(x + 3)

"""First training for implementing Sigmoid function"""

import numpy as np

def sigmoid(x) : 
  s = 1/(np.exp(-x) + 1)

  return s

x = np.array([1 , 2 , 3])
sigmoid(x)

"""
# ***Sigmoid Gradient***"""

def sigmoid_dertitavies(x) : 

  s = sigmoid(x)
  ds = s * (1-s) 

  return ds

x = np.array([1 , 2 , 3])
print('Gradient is' + str(sigmoid_dertitavies(x)))

import numpy as np


def imageShape(image) :

  v = image.reshape(image.shape[0] * image.shape[1] * image.shape[2] , 1) 

  return v

image = np.array([[[0.67826139,  0.29380381],
        [ 0.90714982,  0.52835647],
        [ 0.4215251 ,  0.45017551]],

       [[ 0.92814219,  0.96677647],
        [ 0.85304703,  0.52351845],
        [ 0.19981397,  0.27417313]],

       [[ 0.60659855,  0.00533165],
        [ 0.10820313,  0.49978937],
        [ 0.34144279,  0.94630077]]])

print(str(imageShape(image)))

"""Normalization"""

def normalizeRows(x) : 
  x_norm = np.linalg.norm(x, axis= 1 , keepdims=True)

  x = x/ x_norm

  return x

x = np.array([
    [0, 3, 4],
    [1, 6, 4]
])
print('Normalize Data is :'+ str(normalizeRows(x)))

"""Loss Function"""

def L1(yhat , y): 
  loss= sum(abs(yhat - y))

  return loss

yhat = np.array([1.9 , 0.2 , 0.1 , 1.4 , .9])
y = np.array([1,0,0,1,1])
print('L1 is : '+ str(L1(yhat , y)))

def L2(yhat , y) : 
  x = yhat - y 
  loss = np.dot(x,x)

  return loss

yhat = np.array([1.9 , 0.2 , 0.1 , 1.4 , .9])
y = np.array([1,0,0,1,1])
print('L1 is : '+ str(L2(yhat , y)))
