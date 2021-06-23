"""
Applications of finding Arrival and Departure Time:
    - Topological sortin in a DAG(Directed Acyclic Graph).
    - Finding 2/3 - (edge or vertex) - connected components.
    - Finding bridges in graphs.
    - Finding biconnectivity in graphs.
    - Detecing cycle in directed graphs.
    - Tarjan's algorithm to find strongly connected components, and many more.

Time complexity: O(V + E) where V and E the total number of vertices and edges
"""


class Graph:

    def __init__(self, edges, N):
        self.adjecent = [[] for _ in range(N)]
        for source, destination in edges:
            self.adjecent[source].append(destination)


def dfs(graph, vertex, discovered, arrival, departure, time):
    time += + 1
    arrival[vertex] = time
    discovered[vertex] = True

    for i in graph.adjecent[vertex]:
        if not discovered[i]:
            time = dfs(graph, i, discovered, arrival, departure, time)

    time += 1
    departure[vertex] = time
    return time


if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (2, 3), (2, 4), (3, 1), (3, 5), (4, 5), (6, 7)]
    N = 8
    graph = Graph(edges, N)
    arrival = [None] * N
    departure = [None] * N
    discovered = [False] * N
    time = -1

    for i in range(N):
        if not discovered[i]:
            time = dfs(graph, i, discovered, arrival, departure, time)

    for i in range(N):
        print("Vertex", i, (arrival[i], departure[i]))
