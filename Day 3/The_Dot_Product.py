# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 16:28:42 2021

@author: Eben Emmanuel
"""

# Here we will try to simplify the code that was previously used and make it more dynamic.

inputs = [1, 2, 3, 2.5]  

## Three Weight Vectors with Four Unique Values
weights = [[0.2, 0.8, -0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]


### Creating a loop.
layer_outputs = []      ## Output of current layer
for neuron_weights, neuron_bias in zip(weights, biases):    ## zip combines two lists into a list of list element wise.
    neuron_output = 0       ## Output of given neuron
    for n_input, weight in zip(inputs, neuron_weights):
        neuron_output += n_input*weight
    neuron_output += neuron_bias
    layer_outputs.append(neuron_output)
    
print(layer_outputs)



# Quick Notes.
import numpy as np

## A list in python is an array with numpy. If it a simple list {eg. l=[1,2,3]} then it is a 1D array or a Vector.     
l = [1, 2, 4, 5]
np.shape(l)
## Consider a situation where there are two lists in a list. This is a list of list {eg. lol = [[1,2,3,4], [5,6,7,8]]}. 
### In numpy, this is a 2D array or a Matrix (rectangular array).
### Here we need to understand that arrays have to be Homologous. --> each dimension must have the same size.
lol = [[1, 2, 3, 4],
       [6, 7, 8, 9]]
np.shape(lol)

## In case of a 3D Array
lolol = [[[1, 2, 3, 4],
          [6, 7, 8, 9]],
         [[11, 12, 13, 14],
          [16, 17, 18, 19]],
         [[21, 22, 23, 24],
          [26, 27, 28, 29]]]

np.shape(lolol)
    
## For all the above shape the logic is that it checks for how many elements there are in each list.
### tensor -> An object that can be represented as an array. 





## Using Numpy -> We now have an input which is a vector, a bias which is again a vector and weights which is a matrix.
## Dot product of a Single neurons
inputs = [1, 2, 3, 2.5]  
weights = [0.2, 0.8, -0.5, 1]
bias = 2

output = np.dot(weights, inputs) + bias
print(output)


## Dot product of a Layer of Neurons
inputs = [1, 2, 3, 2.5]  
weights = [[0.2, 0.8, -0.5, 1], 
           [0.5, -0.91, 0.26, -0.5], 
           [-0.26, -0.27, 0.17, 0.87]]

biases = [2, 3, 0.5]

output1 = np.dot(weights, inputs) + biases      
print(output1)

## Here weights come first mainly because the dot product iterates through each weight and that is then 
## multiplied with the input. 
### --> To be more clear np.dot(weights, inputs) == [np.dot(weights[0], inputs), np.dot(weights[1], inputs), np.dot(weights[2], inputs)]
## If it was the other way round then there will be an error as we have 4 inputs and only 3 weights.