 
weights = 	[[0.1, 0.1, -0.3],
			 [0.1, 0.2, 0.0],
			 [0.0, 1.3, 0.1]]

games = [8.5, 9.5, 9.9, 9.0]
wincoeff = [0.65, 0.8, 0.8, 0.9]
fans = [1.2, 1.3, 0.5, 1.0]

input = [games[0], wincoeff[0], fans[0]]

def weightSum(a,b):
	assert(len(a) == len(b))
	output = 0
	for i in range(len(a)):
		output += (a[i] * b[i])
	return output

def vectorMatrixMul(vector, matrix):
	assert(len(vector) == len(matrix))
	output = [0,0,0]
	for i in range(len(vector)):
		output[i] = weightSum(vector, matrix[i])
	return output


def neuralNetwork(input, weights):
	prediction = vectorMatrixMul(input, weights)
	return prediction
print(neuralNetwork(input, weights))