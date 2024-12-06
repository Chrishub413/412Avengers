import itertools
import sys


def read_graph(input_file):
    """Reads graph from file instead of stdin for testing"""
    with open(input_file, 'r') as file:
        lines = file.readlines()
        num_edges = int(lines[0].strip())

        adjacency_list = {}
        for line in lines[1:num_edges + 1]:
            u, v = line.strip().split()

            if u not in adjacency_list:
                adjacency_list[u] = set()
            if v not in adjacency_list:
                adjacency_list[v] = set()

            adjacency_list[u].add(v)
            adjacency_list[v].add(u)

        return adjacency_list


def is_valid_coloring(graph, coloring):
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if coloring[node] == coloring[neighbor]:
                return False
    return True


def getMincolor(graph):
    n = len(graph)
    nodes = list(graph.keys())

    for num_colors in range(1, n + 1):
        for coloring in itertools.product(range(num_colors), repeat=n):
            coloring_dict = dict(zip(nodes, coloring))
            if is_valid_coloring(graph, coloring_dict):
                return num_colors, coloring_dict
    return None


def main(input_file):
    graph = read_graph(input_file)

    if not graph:
        print("Error: Graph is empty or invalid.")
        return

    result = getMincolor(graph)

    if result is None:
        print("Error: No valid coloring found.")
    else:
        min_colors, coloring = result
        print(min_colors)
        for vertex in sorted(coloring.keys()):
            print(f"{vertex} {coloring[vertex]}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python cs412_mingraphcolor_exact_file.py <input_file>")
        sys.exit(1)
    main(sys.argv[1])