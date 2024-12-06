import sys

def read_graph(input_file):
    with open(input_file, "r") as file:
        lines = file.readlines()
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

def compute_lower_bound(adjacency_list):
    """
    Computes lower bound using maximum clique size approximation.
    """
    max_clique_size = 1
    for vertex in adjacency_list:
        neighbors = adjacency_list[vertex]
        clique = {vertex}
        
        # Greedily build a clique
        for neighbor in neighbors:
            is_connected_to_all = all(n in adjacency_list[neighbor] for n in clique)
            if is_connected_to_all:
                clique.add(neighbor)
                
        max_clique_size = max(max_clique_size, len(clique))
    
    return max_clique_size

def compute_upper_bound(adjacency_list):
    """
    Returns maximum degree + 1 as an upper bound. Brooks' Theorem
    """
    max_degree = max(len(neighbors) for neighbors in adjacency_list.values())
    return max_degree + 1

def greedy_coloring(adjacency_list):
    vertex_colors = {}
    sorted_vertices = sorted(adjacency_list, key=lambda x: -len(adjacency_list[x]))

    for vertex in sorted_vertices:
        neighbor_colors = {vertex_colors[neighbor] for neighbor in adjacency_list[vertex] if neighbor in vertex_colors}
        for color in range(len(adjacency_list)):
            if color not in neighbor_colors:
                vertex_colors[vertex] = color
                break
    return vertex_colors

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python graph_coloring.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    adjacency_list = read_graph(input_file)
    
    # Compute bounds
    lower_bound = compute_lower_bound(adjacency_list)
    upper_bound = compute_upper_bound(adjacency_list)
    
    # Run approximation
    vertex_colors = greedy_coloring(adjacency_list)
    approx_colors = len(set(vertex_colors.values()))
    
    print(f"Lower bound: {lower_bound}")
    print(f"Upper bound: {upper_bound}")
    print(f"Approximation: {approx_colors}")
    print("\nVertex coloring:")
    for vertex, color in vertex_colors.items():
        print(f"{vertex} {color}")
    print("\n")