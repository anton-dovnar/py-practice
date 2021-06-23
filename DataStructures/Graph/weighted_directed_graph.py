class Edge:

    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


class Node:

    def __init__(self, value, weight):
        self.value = value
        self.weight = weight


class Graph:

    def __init__(self, edges, N):
        self.adjecent = [[] for _ in range(N)]

        for edge in edges:
            node = Node(edge.destination, edge.weight)
            self.adjecent[edge.source].append(node)


def print_graph(graph):
    for source in range(len(graph.adjecent)):
        for edge in graph.adjecent[source]:
            print(f"({source} -> {edge.value}, {edge.weight})", end=" ")
        print()


if __name__ == "__main__":
    edges = [Edge(0, 1, 6), Edge(1, 2, 7), Edge(2, 0, 5), Edge(2, 1, 4),
             Edge(3, 2, 10), Edge(4, 5, 1), Edge(5, 4, 3)]
    N = 6
    graph = Graph(edges, N)
    print_graph(graph)
