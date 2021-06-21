"""
Application of DFS Algorithm:
    - For finding the path
    - To test if the graph is bipartite
    - For finding the strongly connected components of a graph
    - For detecting cycles in a graph

Time complexity: O(V + E), V is the number of nodes and E is the number of edges
Space complexity: O(V)
"""


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for following in graph[start] - visited:
        dfs(graph, following, visited)
    return visited


if __name__ == "__main__":
    graph = {
        "0": set(["1", "2"]),
        "1": set(["0", "3", "4"]),
        "2": set(["0"]),
        "3": set(["1"]),
        "4": set(["2", "3"])
    }
    dfs(graph, "0")
