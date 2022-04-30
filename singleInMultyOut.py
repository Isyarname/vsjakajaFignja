import numpy as np 


weights = [0.3, 0.2, 0.9]
wincoeff = [0.65, 0.8, 0.8, 0.9]
input = wincoeff[0]

def neuralNetwork(input, weight):
	prediction = eleMul(input, weight)
	return prediction

def eleMul(number, vector):
	output = [0,0,0]
	assert(len(output) == len(vector))
	for i in range(len(vector)):
		output[i] = number * vector[i]
	return output
print(neuralNetwork(input, weights))