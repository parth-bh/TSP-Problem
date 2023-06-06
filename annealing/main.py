import numpy as np
import random
import math

def get_distance(tour, dist_matrix):
    """
    Calculates the total distance of a given tour using the given distance matrix.

    Arguments:
    tour -- list representing the order in which the cities are visited
    dist_matrix -- 2D numpy array representing the distance between each pair of cities

    Returns:
    total_distance -- float representing the total distance of the tour
    """
    total_distance = 0.0
    for i in range(len(tour)):
        j = (i + 1) % len(tour)
        city_i, city_j = tour[i], tour[j]
        total_distance += dist_matrix[city_i][city_j]
    return total_distance

def simulated_annealing(dist_matrix, start_temp=10000, end_temp=1, alpha=0.995, stopping_iter=1000):
    """
    Solves the Traveling Salesman Problem using the Simulated Annealing algorithm.

    Arguments:
    dist_matrix -- 2D numpy array representing the distance between each pair of cities
    start_temp -- float representing the starting temperature (default: 10000)
    end_temp -- float representing the ending temperature (default: 1)
    alpha -- float representing the cooling rate (default: 0.995)
    stopping_iter -- int representing the number of iterations with no improvement to stop at (default: 1000)

    Returns:
    best_tour -- list representing the best tour found
    best_distance -- float representing the total distance of the best tour found
    """
    num_cities = len(dist_matrix)
    curr_tour = list(range(num_cities))
    random.shuffle(curr_tour)
    best_tour = curr_tour.copy()
    best_distance = get_distance(curr_tour, dist_matrix)
    temp = start_temp
    no_improvement = 0
    while temp >= end_temp and no_improvement < stopping_iter:
        i, j = sorted(random.sample(range(num_cities), 2))
        new_tour = curr_tour[:i] + curr_tour[j:j+1] + curr_tour[i+1:j] + curr_tour[i:i+1] + curr_tour[j+1:]
        new_distance = get_distance(new_tour, dist_matrix)
        if math.exp((best_distance - new_distance) / temp) > random.random():
            curr_tour = new_tour.copy()
            curr_distance = new_distance
            if curr_distance < best_distance:
                best_tour = curr_tour.copy()
                best_distance = curr_distance
                no_improvement = 0
            else:
                no_improvement += 1
        else:
            no_improvement += 1
        temp *= alpha
    return best_tour, best_distance




euclidian = input()
N = int(input())
cord = []

for _ in range(N):
    x1, y1 = input().split(" ")
    cord.append((float(x1), float(y1)))

dist_matrix = []

for _ in range(N):
    dist = input().split(" ")
    dist = [float(i) for i in dist]
    dist_matrix.append(dist)

dist_matrix = np.array(dist_matrix)


#import time
#start = time.time()


best_path, best_dist = simulated_annealing(dist_matrix)


#print(best_path, best_dist)

result = best_path[0]
for i in range(1, N):
    result = str(result) + " "
    result = result + str(best_path[i])
print(result)



#end = time.time()
#print(end-start)







