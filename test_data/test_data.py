# create function that returns distance matrix of  size N and with some range max value.
import random
import numpy as np

def creating_data(N, maxsize):
	dist_matrix = np.zeros((N,N))
	for i in range(N):
		j=i
		while (j>=i) & (j<N):
			if (i!=j):
				number = round(maxsize*random.random(),0)
				dist_matrix[i][j] = number
				dist_matrix[j][i] = number
			j+=1
	return dist_matrix


N = int(input("Size or Number of cities (N): "))
maxsize = int(input("Maximum distance between cities (maxsize): "))

dist_matrix= creating_data(N, maxsize)

np.savetxt("test_data.csv", dist_matrix, delimiter=",")
