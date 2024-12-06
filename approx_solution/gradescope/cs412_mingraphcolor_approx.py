import sys

def read_graph():
    """
    Reads a graph from stdin.

    Returns:
        dict: Adjacency list representation of the graph.
    """
    lines = sys.stdin.readlines()
    num_edges = int(lines[0].strip())
    edges = [tuple(line.strip().split()) for line in lines[1:]]

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

    Args:
        adjacency_list (dict): Adjacency list representation of the graph
        vertex_colors (dict): Mapping of vertices to their assigned colors

    Returns:
        tuple: (is_valid, message) where is_valid is True if coloring is valid
    """
    # Verify all vertices are colored
    for vertex in adjacency_list:
        if vertex not in vertex_colors:
            return False, f"Invalid: Missing color for vertex {vertex}"

    # Verify no adjacent vertices share colors
    for vertex in adjacency_list:
        current_color = vertex_colors[vertex]
        for neighbor in adjacency_list[vertex]:
            if vertex_colors[neighbor] == current_color:
                return False, f"Invalid: Adjacent vertices {vertex} and {neighbor} share color {current_color}"

    return True, "Valid coloring"

def greedy_coloring(adjacency_list):
    """
    Perform greedy coloring on the graph.

    Args:
        adjacency_list (dict): Adjacency list of the graph.

    Returns:
        dict: Mapping of vertices to colors.
    """
    vertex_colors = {}
    # Sort vertices by degree in descending order for better approximation
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
    adjacency_list = read_graph()
    vertex_colors = greedy_coloring(adjacency_list)

    # Verify the solution
    is_valid, message = verify_coloring(adjacency_list, vertex_colors)
    if not is_valid:
        sys.exit(1)

    # Output according to project specification
    num_colors = len(set(vertex_colors.values()))
    print(num_colors)
    for vertex, color in sorted(vertex_colors.items()):
        print(f"{vertex} {color}")