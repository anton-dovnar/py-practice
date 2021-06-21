"""
Adjacency List
"""


class Node:

    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:

    def __init__(self, num):
        self.v = num
        self.graph = [None] * self.v

    def add_edge(self, s, d):
        node = Node(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = Node(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def print_graph(self):
        for i in range(self.v):
            print(f"Vertex {i}:", end="")
            temp = self.graph[i]
            while temp:
                print(f" -> {temp.vertex}", end="")
                temp = temp.next
            print(" \n")


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)
    graph.print_graph()
