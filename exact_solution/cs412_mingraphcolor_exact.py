import time
import itertools

def load_graph(file_name):
   
    #Load a graph from a file.
    with open(file_name, "r") as file:
        edges_count = int(file.readline().strip())
        graph = {}
        for _ in range(edges_count):
            u, v = map(int, file.readline().strip().split())
            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)
    return graph

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

    # Try all possible numbers
    for num_colors in range(1, n + 1):
        # Generate all possible color assignments
        for coloring in itertools.product(range(num_colors), repeat=n):
            if is_valid_coloring(graph, dict(zip(nodes, coloring))):
                return num_colors, coloring  # Return color number and valid coloring
    return None

def main():
    # Test generated graph files
    test_files = ["test_cases/graph_small.txt", "test_cases/graph_medium.txt", "test_cases/graph_large.txt"]

    for file_name in test_files:
        try:
            print(f"Testing graph from {file_name}...")
            graph = load_graph(file_name)

            if not graph:
                print(f"Error: Graph in {file_name} is empty or invalid.")
                continue

            start_time = time.time()
            minColor, coloring = getMincolor(graph)
            runtime = time.time() - start_time

            if minColor is None:
                print(f"Error: No valid coloring found for {file_name}.")
            else:
                print(f"number of colors: {minColor}")
                print(f"Coloring: {list(coloring)}")
                print(f"Runtime: {runtime:.2f} seconds\n")
        except Exception as e:
            print(f"An error occurred while testing {file_name}: {e}\n")


if __name__ == "__main__":
    main()
