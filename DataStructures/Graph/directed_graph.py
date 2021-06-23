"""
Implementation of a directed graph using an adjacency list
"""


class Edge:

    def __init__(self, data, destination):
        self.data = data
        self.destination = destination


class Graph:

    def __init__(self, edges, N):
        self.adjecent = [[] for _ in range(N)]

        for current in edges:
            self.adjecent[current.data].append(current.destination)


def print_graph(graph):
    for data in range(len(graph.adjecent)):
        for destination in graph.adjecent[data]:
            print(F"({data} -> {destination})", end=" ")
        print()


if __name__ == "__main__":
    edges = [Edge(0, 1), Edge(1, 2), Edge(2, 0), Edge(2, 1),
             Edge(3, 2), Edge(4, 5), Edge(5, 4)]
    N = 6
    graph = Graph(edges, N)
    print_graph(graph)
