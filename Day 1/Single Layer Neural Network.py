# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 00:03:21 2021

@author: Eben Emmanuel
"""

### We will understand the foundations of neural networks. **Without the major Libraries**

## Single Layer Feed-Forward Neural Network.
inputs = [1.2, 5.1, 2.1]  ## Unique inputs. (The output of the previous layer is the input of this layer
weights = [3.1, 2.1, 8.7]   ## every Unique input has a unique Weight.
bias = 3    ## Every Unique Neuron has a unique Bias.


#### Output -> Input*Weight + Bias
output = inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] +bias
output
