import sys


def read_graph(input_file):
    """
    Reads a graph from the input file.

    Args:
        input_file (str): Path to the input file.

    Returns:
        list: Adjacency list representation of the graph.
    """
    with open(input_file, "r") as file:
        lines = file.readlines()
        num_edges = int(lines[0].strip())
        edges = [tuple(line.strip().split()) for line in lines[1:]]

    # Create adjacency list
    adjacency_list = {}
    for u, v in edges:
        if u not in adjacency_list:
            adjacency_list[u] = set()
        if v not in adjacency_list:
            adjacency_list[v] = set()
        adjacency_list[u].add(v)
        adjacency_list[v].add(u)

    return adjacency_list


def verify_coloring(adjacency_list, vertex_colors):
    """
    Polynomial-time certifier for graph coloring solution.
    Runtime: O(V + E) where V is number of vertices and E is number of edges.

    This certifier verifies that:
    1. Every vertex has a color (completeness)
    2. No adjacent vertices share colors (correctness)

    These checks are sufficient to prove a valid graph coloring in polynomial time.

    Args:
        adjacency_list (dict): Adjacency list representation of the graph
        vertex_colors (dict): Mapping of vertices to their assigned colors

    Returns:
        tuple: (is_valid, message) where:
            - is_valid (bool): True if coloring is valid, False otherwise
            - message (str): Verification details and runtime analysis
    """
    # Step 1: Verify all vertices are colored - O(V) time
    for vertex in adjacency_list:
        if vertex not in vertex_colors:
            return False, f"Certificate Invalid: Missing color for vertex {vertex}"

    # Step 2: Verify no adjacent vertices share colors - O(E) time
    for vertex in adjacency_list:
        current_color = vertex_colors[vertex]
        for neighbor in adjacency_list[vertex]:
            if vertex_colors[neighbor] == current_color:
                return False, f"Certificate Invalid: Adjacent vertices {vertex} and {neighbor} share color {current_color}"

    # Certificate is valid - total runtime O(V + E)
    num_vertices = len(adjacency_list)
    num_edges = sum(len(neighbors) for neighbors in adjacency_list.values()) // 2
    return True, f"Certificate Valid! Verified {num_vertices} vertices and {num_edges} edges in O(V + E) time"


def greedy_coloring(adjacency_list):
    """
    Perform greedy coloring on the graph.

    Args:
        adjacency_list (dict): Adjacency list of the graph.

    Returns:
        dict: Mapping of vertices to colors.
    """
    vertex_colors = {}
    # Sort vertices by degree in descending order
    sorted_vertices = sorted(adjacency_list, key=lambda x: -len(adjacency_list[x]))

    for vertex in sorted_vertices:
        # Get all colors used by neighbors
        neighbor_colors = {vertex_colors[neighbor] for neighbor in adjacency_list[vertex] if neighbor in vertex_colors}
        # Assign the smallest available color
        for color in range(len(adjacency_list)):
            if color not in neighbor_colors:
                vertex_colors[vertex] = color
                break
    return vertex_colors


if __name__ == "__main__":
    # Check for correct number of arguments
    if len(sys.argv) < 2:
        print("Usage: python cs412_mingraphcolor_approx.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    adjacency_list = read_graph(input_file)
    vertex_colors = greedy_coloring(adjacency_list)

    # Output initial results required by problem specification
    num_colors = len(set(vertex_colors.values()))
    print(num_colors)
    for vertex, color in vertex_colors.items():
        print(f"{vertex} {color}")

    # Print divider line
    print("\n" + "=" * 50)

    # Verify the solution using polynomial-time certifier
    print("\nRunning Polynomial-Time Certificate Verification:")
    is_valid, message = verify_coloring(adjacency_list, vertex_colors)
    print(message)

    # Print vertex coloring
    print("\nDetailed vertex coloring:")
    for vertex in sorted(vertex_colors.keys()):
        print(f"Vertex {vertex}: Color {vertex_colors[vertex]}")

    # Print chromatic number at the very end
    print(f"\nChromatic Number: {num_colors}")

    # Exit with error if verification failed
    if not is_valid:
        sys.exit(1)