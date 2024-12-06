import time
import itertools
import sys

def read_graph_from_stdin():
    try:
        num_edges = int(input().strip())
        
        adjacency_list = {}
        for _ in range(num_edges):
            u, v = input().strip().split()
            
            if u not in adjacency_list:
                adjacency_list[u] = set()
            if v not in adjacency_list:
                adjacency_list[v] = set()
                
            adjacency_list[u].add(v)
            adjacency_list[v].add(u)
            
        return adjacency_list
    except EOFError:
        sys.exit(1)
    except ValueError:
        sys.exit(1)

def is_valid_coloring(graph, coloring):
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                return False
    return True

def getMincolor(graph):
    n = len(graph)
    nodes = list(graph.keys())

    # Try all possible numbers of colors (1 to n)
    for num_colors in range(1, n + 1):
        # Generate all possible color assignments
        for coloring in itertools.product(range(num_colors), repeat=n):
            coloring_dict = dict(zip(nodes, coloring))
            if is_valid_coloring(graph, coloring_dict):
                return num_colors, coloring_dict  # Return color number and valid coloring as dict
    return None

def main():
    # Read graph from stdin
    graph = read_graph_from_stdin()
    
    if not graph:
        print("Error: Graph is empty or invalid.")
        return

    # Compute the minimum coloring
    result = getMincolor(graph)

    if result is None:
        print("Error: No valid coloring found.")
    else:
        min_colors, coloring = result
        # Print number of colors
        print(min_colors)
        # Print vertex colorings
        for vertex in sorted(coloring.keys()):
            print(f"{vertex} {coloring[vertex]}")

if __name__ == "__main__":
    main()