import numpy as np

def tsp_bb(distances):
    n = len(distances)
    stack = []
    best_path = None
    best_dist = np.inf
    visited = np.zeros(n, dtype=bool)
    visited[0] = True
    stack.append((0, visited, [0], 0))

    while stack:
        current_node, current_visited, current_path, current_dist = stack.pop()

        if current_dist >= best_dist:
            continue

        if np.all(current_visited):
            current_dist += distances[current_node, 0]
            if current_dist < best_dist:
                best_path = current_path + [0]
                best_dist = current_dist
        else:
            for next_node in range(n):
                if not current_visited[next_node]:
                    next_visited = current_visited.copy()
                    next_visited[next_node] = True
                    next_path = current_path + [next_node]
                    next_dist = current_dist + distances[current_node, next_node]
                    stack.append((next_node, next_visited, next_path, next_dist))

    return best_path, best_dist


path = open('test_data.csv')
dist_matrix = np.loadtxt(path, delimiter=",")

print(dist_matrix)

import time
start = time.time()

print(tsp_bb(dist_matrix))

end = time.time()
print(end-start)

