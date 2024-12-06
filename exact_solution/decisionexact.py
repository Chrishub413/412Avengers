import time
import itertools

def load_graph(file_name):
    # Load a graph from a file.
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
    # Check if a given coloring is valid for the graph.
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                return False
    return True

def can_color_with_k(graph, k):
    # Decision version: Check if the graph can be colored with at most k colors
    n = len(graph)
    nodes = list(graph.keys())

    for coloring in itertools.product(range(k), repeat=n):
        if is_valid_coloring(graph, dict(zip(nodes, coloring))):
            return True  
    return False  

def main():
    # Test generated graph files
    test_files = ["graph_small.txt", "graph_medium.txt", "graph_large.txt"]
    k = 4  # Set the number of colors to test for

    for file_name in test_files:
        try:
            print(f"Testing graph from {file_name} with {k} colors...")

            # Load the graph from the file
            graph = load_graph(file_name)

            if not graph:
                print(f"Error: Graph in {file_name} is empty or invalid.")
                continue

            start_time = time.time()
            can_color = can_color_with_k(graph, k)
            runtime = time.time() - start_time

            if can_color:
                print(f"The graph can be colored with {k} or fewer colors.")
            else:
                print(f"The graph cannot be colored with {k} or fewer colors.")
            print(f"Runtime: {runtime:.2f} seconds\n")

        except Exception as e:
            print(f"An error occurred while testing {file_name}: {e}\n")

if __name__ == "__main__":
    main()
