"""
Implementation of a directed graph using an adjacency list
"""

class Node:

    def __init__(self, data, destination):
        self.data = data
        self.destination = destination


class Graph:

    def __init__(self, nodes, N):
        self.adjecent = [[] for _ in range(N)]

        for current in nodes:
            self.adjecent[current.data].append(current.destination)


def print_graph(graph):
    for data in range(len(graph.adjecent)):
        for destination in graph.adjecent[data]:
            print(F"({data} -> {destination})", end=" ")
        print()


if __name__ == "__main__":
    nodes = [Node(0, 1), Node(1, 2), Node(2, 0), Node(2, 1),
             Node(3, 2), Node(4, 5), Node(5, 4)]
    N = 6
    graph = Graph(nodes, N)
    print_graph(graph)
