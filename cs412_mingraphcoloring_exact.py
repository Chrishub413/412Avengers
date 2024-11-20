"""
Example:
Code

Input:
6
0 1
0 2
0 3
1 2
1 3
2 3

Output:
Minimum colors: 4
Color assignment: [0, 1, 2, 3]
"""

def main():
    E = int(input())
    graph = {}

    # paths a-list
    for _ in range(E):
        v1, v2 = input().strip().split()

        # use set for edges {'hburg': {'jmu'}, 'jmu':{'hburg', 'cville'}}
        graph.setdefault(v1, set()).add(v2)
        graph.setdefault(v2, set()).add(v1)

    print(graph)

if __name__ == "__main__":
    main()

