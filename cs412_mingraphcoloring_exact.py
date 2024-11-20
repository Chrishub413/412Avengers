"""
Example:
Code

Input:
6
0 1
0 2
0 3
1 2
1 3
2 3

Output:
Minimum colors: 4
Color assignment: [0, 1, 2, 3]
"""

def greedy_coloring(G, V):
        # Initialize all vertices as unassigned

        result = [-1] *  V
        
        # Assign the first color to the first vertex
        result[0] = 0

        # A temporary array to store the colors of the adjacent vertices
        available = [False] * V

        print(G.keys())
        print(result)
        print(available)

        # # Assign colors to remaining V-1 vertices
        # for u in range(1, V):
        #     # Mark colors of adjacent vertices as unavailable
        #     for i in G.keys():
        #         if result[i] != -1:
        #             available[result[i]] = True

        #     # Find the first available color
        #     for color in range(V):
        #         if not available[color]:
        #             break

        #     result[u] = color

        #     # Reset the values back to false for the next iteration
        #     for i in G.keys():
        #         if result[i] != -1:
        #             available[result[i]] = False

        # # Print the result
        # for u in range(V):
        #     print(f"Vertex {u} --> Color {result[u]}")

def main():
    E = int(input())
    graph = {}

    # paths a-list
    for _ in range(E):
        v1, v2 = input().strip().split()

        # use set for edges {'a': {'b'}, 'b':{'a', 'c'}, 'c':{'b'}}
        graph.setdefault(v1, set()).add(v2)
        graph.setdefault(v2, set()).add(v1)

    V = len(graph)

    ## Do coloring method

    greedy_coloring(graph, V)

if __name__ == "__main__":
    main()

