import random
import sys


def generate_graph(num_vertices, num_edges, output_file="fully-connected-large.txt"):
    """
    Generate an undirected graph with the specified number of vertices and edges.

    Args:
        num_vertices (int): Number of vertices in the graph.
        num_edges (int): Number of edges in the graph.
        output_file (str): Output file name for the graph.
    """
    if num_edges > num_vertices * (num_vertices - 1) // 2:
        raise ValueError("Too many edges for the given number of vertices.")

    edges = set()
    while len(edges) < num_edges:
        u = random.randint(0, num_vertices - 1)
        v = random.randint(0, num_vertices - 1)
        if u != v:
            edges.add(tuple(sorted((u, v))))  # Ensure no duplicates

    with open(output_file, "w") as file:
        file.write(f"{len(edges)}\n")
        for u, v in edges:
            file.write(f"{u} {v}\n")
    print(f"Graph with {num_vertices} vertices and {num_edges} edges saved to {output_file}.")


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) < 3:
        print("Usage: python generate_graph.py <num_vertices> <num_edges> [output_file]")
        sys.exit(1)

    # Parse command-line arguments
    try:
        num_vertices = int(sys.argv[1])
        num_edges = int(sys.argv[2])
        output_file = sys.argv[3] if len(sys.argv) > 3 else "fully-connected-large.txt"

        generate_graph(num_vertices, num_edges, output_file)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
