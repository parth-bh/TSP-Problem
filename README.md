# TSP-Problem
Tried different algorithms to solve the TSP Problem, as it is a NP Hard Problem and not solvable with brute force algorithms.



Given a set of N cities and distance between every pair of cities, find the shortest possible route that starts from a city and visits every city exactly once and returns to the starting city.
Write a program to find the shortest tour of N cities.

This Problem Known as TSP that is Traveling Salesman Problem, involves finding the shortest possible route that a traveling salesman can take through a given set of cities, visiting each city exactly once and then returning to the starting city.

The TSP has applications in various fields, including logistics, transportation, manufacturing, and computer networking, among others.

The TSP is considered an NP-hard problem, which means that there is no known polynomial-time algorithm that can solve it.
There are various heuristics and approximation algorithms that can be used to find near-optimal solutions, but finding the exact solution to large instances of the TSP remains a challenging problem.

There are some algorithms that i know for solving the TSP, and gives the optimal solutions but  these work only for small number of cities.
- Brute Force Algorithm: This algorithm exhaustively enumerates all possible paths to find the optimal solution. It has a time complexity of O(n!) and is only work for small instances of the problem.

- Branch and Bound Algorithm: This algorithm uses a tree-based approach to eliminate partial solutions that are guaranteed to be suboptimal. It has a worst-case time complexity of O(n^2 2^n) and is more practical than the brute force algorithm for larger instances of the problem.

When i started to write the code for solving this mini project or problem statment, first i started with the branch and bound algorithm but it is taking more than expected time that is 300 seconds for solving N=25 cities, that is very few number of cities, Hence I decided to dropped this algorithm.

