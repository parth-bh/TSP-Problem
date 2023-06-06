import numpy as np
import random

# Set parameters
POPULATION_SIZE = 100
MUTATION_RATE = 0.1
GENERATIONS = 500

# Create a random population
def create_population(n):
    population = []
    for i in range(POPULATION_SIZE):
        individual = list(range(n))
        random.shuffle(individual)
        population.append(individual)
    return population

# Calculate the fitness of an individual
def fitness(individual, distances):
    total_distance = 0
    for i in range(len(individual)):
        total_distance += distances[individual[i-1], individual[i]]
    return 1/total_distance

# Perform crossover between two parents
def crossover(parent1, parent2):
    n = len(parent1)
    child = [-1] * n
    start = random.randint(0, n-1)
    end = random.randint(start+1, n)
    child[start:end] = parent1[start:end]
    for i in range(n):
        if parent2[i] not in child:
            for j in range(n):
                if child[j] == -1:
                    child[j] = parent2[i]
                    break
    return child

# Perform mutation on an individual
def mutate(individual):
    n = len(individual)
    if random.random() < MUTATION_RATE:
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        individual[i], individual[j] = individual[j], individual[i]
    return individual

# Select two parents from the population using tournament selection
def select_parents(population, distances):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    tournament_fitness = [fitness(individual, distances) for individual in tournament]
    max_index = np.argmax(tournament_fitness)
    parent1 = tournament[max_index]
    tournament[max_index] = None
    tournament_fitness[max_index] = -1
    max_index = np.argmax(tournament_fitness)
    parent2 = tournament[max_index]
    return parent1, parent2

# Create a new generation of individuals
def create_new_generation(population, distances):
    new_population = []
    for i in range(POPULATION_SIZE):
        parent1, parent2 = select_parents(population, distances)
        child = crossover(parent1, parent2)
        child = mutate(child)
        new_population.append(child)
    return new_population

# Solve the TSP using a Genetic Algorithm
def tsp_ga(distances):
    n = len(distances)
    population = create_population(n)
    best_path = None
    best_dist = -1
    for i in range(GENERATIONS):
        population_fitness = [fitness(individual, distances) for individual in population]
        max_index = np.argmax(population_fitness)
        max_fitness = population_fitness[max_index]
        max_individual = population[max_index]
        if max_fitness > best_dist:
            best_path = max_individual
            best_dist = max_fitness
        population = create_new_generation(population, distances)
    best_path.append(best_path[0])
    return best_path, 1/best_dist


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


best_path, best_dist = tsp_ga(dist_matrix)


result = best_path[0]
for i in range(1, N):
    result = str(result) + " "
    result = result + str(best_path[i])
print(result)

