import numpy as np
import math
#from matplotlib import pyplot

weight 		= np.array([0.1, 0.2, 0])

#games 		= np.array([8.5, 9.5, 10, 9])
wincoeff 	= np.array([0.65, 0.8, 0.8, 0.9])
#fans 		= np.array([1.2, 1.3, 0.5, 1.0])

k = 3
input = np.array([games[k], wincoeff[k], fans[k]])

def neuralNetwork(input, weight):
	prediction = np.dot(input, weight)
	return prediction


print(neuralNetwork(input, weight))