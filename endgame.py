import itertools
from itertools import product

# Function to count the minimum number of color required
def minimumColors(verticeNumber, edgeNumber, vertices, edges):

    # Create array of vectors to make adjacency list
    adj = [[] for i in range(verticeNumber)]

    # Initialise colors array to 1
    # and count array to 0
    count = [0] * verticeNumber
    colors = [1] * (verticeNumber)

    # Create adjacency list of
    # a graph
    for i in range(verticeNumber):
        adj[edges[i] - 1].append(vertices[i] - 1)
        count[vertices[i] - 1] += 1

    print(adj)

# Driver function
N = 5
E = 6
U = [1, 2, 3, 1, 2, 3]
V = [3, 3, 4, 4, 5, 5]

minimumColors(N, E, U, V)