"""
BFS Algorithm Applications:
    - To build index by search index
    - For GPS navigation
    - Path finding algorithms
    - In Ford-Fulkerson algorithms to find maximum flow in a network
    - Cycle detection in an undirected graph
    - In minimum spanning tree

Time complexity: O(V + E) where V is the number of nodes and E is the number of edges
Space complexity: O(V)
"""
from collections import deque


def bfs(graph, root):
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [2],
        2: [3],
        3: [1, 2]
    }
    print("Following in Breadth First Traversal: ")
    bfs(graph, 0)
