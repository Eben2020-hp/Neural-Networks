# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 13:45:05 2021

@author: Eben Emmanuel
"""

# Single Neuron with Four Inputs
## Lets consider this to be a Hidden Layer
inputs = [1, 2, 3, 2.5]  ## Unique inputs. 
weights = [0.2, 0.8, -0.5, 1]   ## Unique Weight.

## This is the Bias of the Output Neuron
bias = 2    ## Unique Bias.

## Why only one Bias?

#### In the above example though we have three inputs and three weights, there is only one Bias. 
#### This is because there is only one neuron. Every Neuron have only one Bias.


#### Output -> Input*Weight + Bias
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + inputs[3]*weights[3] + bias
print('Single Neuron with Four Inputs: \n', output)



print()



# Three Neurons with Four Inputs
## Here when we say three neurons we are talking about the Output Layer.
inputs = [1, 2, 3, 2.5]  

## Three Weight Vectors with Four Unique Values
weights1 = [0.2, 0.8, -0.5, 1]   
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

## Since we have Three Neurons --> Three Bias
bias1 = 2
bias2 = 3
bias3 = 0.5

#### Output1 -> Input*Weight(i) + Bias(i)
output1 = [inputs[0]*weights1[0] + inputs[1]*weights1[1] + inputs[2]*weights1[2] + inputs[3]*weights1[3] + bias1,
          inputs[0]*weights2[0] + inputs[1]*weights2[1] + inputs[2]*weights2[2] + inputs[3]*weights2[3] + bias2,
          inputs[0]*weights3[0] + inputs[1]*weights3[1] + inputs[2]*weights3[2] + inputs[3]*weights3[3] + bias3]
print('Three Neurons with Four Inputs: \n', output1)


### The inputs can't be changed as they are information from other neurons. So in-order to tweek them we can mess with
### the weights and bias. This is the only solution.