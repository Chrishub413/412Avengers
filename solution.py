
def is_independent_set(graph, vertex_set):

    for vertex in vertex_set:
        for neighbor in graph[vertex]:
            if neighbor in vertex_set:
                return False
    return True

def main():
    vert = int(input())
    
    adjacency_list = {}
    for vertex in range(vert):
        adjacency_list[vertex] = {n for n in map(int, input().split()) if n != vertex}


    
    independent = set(map(int, input().split()))
    
    print(adjacency_list)
    print(independent)
    
    if is_independent_set(adjacency_list, independent):
        print("TRUE")
    else:
        print("FALSE")

if __name__ == "__main__":
    main()
    