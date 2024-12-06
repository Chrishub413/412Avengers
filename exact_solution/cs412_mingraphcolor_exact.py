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
        print("Error: Incomplete input", file=sys.stderr)
        sys.exit(1)
    except ValueError:
        print("Error: Invalid input format", file=sys.stderr)
        sys.exit(1)

def is_valid_coloring(graph, coloring):
    #Check if a given coloring is valid for the graph.
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                return False
    return True

def getMincolor(graph):
    #Find the color number
    n = len(graph)
    nodes = list(graph.keys())

    # Try all possible numbers of colors (1 to n)
    for num_colors in range(1, n + 1):
        # Generate all possible color assignments
        for coloring in itertools.product(range(num_colors), repeat=n):
            if is_valid_coloring(graph, dict(zip(nodes, coloring))):
                return num_colors, coloring  # Return color number and valid coloring
    return None

def main():
    # Read graph from stdin
    graph = read_graph_from_stdin()
    
    if not graph:
        print("Error: Graph is empty or invalid.")
        return

    # Compute the minimum coloring
    start_time = time.time()
    minColor, coloring = getMincolor(graph)
    runtime = time.time() - start_time

    if minColor is None:
        print("Error: No valid coloring found.")
    else:
        print(f"Number of colors: {minColor}")
        print(f"Coloring: {list(coloring)}")
        print(f"Runtime: {runtime:.2f} seconds")

if __name__ == "__main__":
    main()
