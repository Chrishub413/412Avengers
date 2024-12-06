import time
import itertools
import sys


def load_graph(file_name):
    """Load a graph from a file."""
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
    """Check if a given coloring is valid for the graph."""
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                return False
    return True


def getMincolor(graph):
    """Find the color number of the graph using brute force with itertools."""
    n = len(graph)
    nodes = list(graph.keys())

    # Try all possible numbers of colors (1 to n)
    for num_colors in range(1, n + 1):
        # Generate all possible color assignments
        for coloring in itertools.product(range(num_colors), repeat=n):
            color_dict = dict(zip(nodes, coloring))
            if is_valid_coloring(graph, color_dict):
                return num_colors, color_dict  # Return color number and valid coloring


def main():
    # Check if input file is provided
    if len(sys.argv) != 2:
        print("Usage: python exact.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        # Load and process the graph
        graph = load_graph(input_file)

        if not graph:
            print(f"Error: Graph in {input_file} is empty or invalid.")
            sys.exit(1)

        # Get the coloring
        minColor, coloring = getMincolor(graph)

        # Print required output format
        if minColor is not None:
            print(minColor)  # First line: number of colors
            for vertex, color in coloring.items():  # Following lines: vertex color pairs
                print(f"{vertex} {color}")
        else:
            print("Error: No valid coloring found.")
            sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()