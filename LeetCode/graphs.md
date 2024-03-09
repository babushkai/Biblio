# Graphs

## Explanation

Graphs are data structures that consist of a set of nodes (vertices) and edges connecting them. They are used to represent networks, which can include paths in a city, relationships in a social network, or connections between components in a circuit.

## Example Problems

- **Graph Traversal:** Perform depth-first search (DFS) or breadth-first search (BFS) to visit all nodes in a graph.
- **Shortest Path:** Find the shortest path between two nodes, commonly solved using Dijkstra's algorithm or the A* search algorithm.
- **Cycle Detection:** Determine whether a graph contains a cycle, which can be done using DFS with backtracking or Union-Find for undirected graphs.

## Time Complexity

- The time complexity for traversing a graph is O(V + E), where V is the number of vertices and E is the number of edges.
- For Dijkstra's algorithm, the time complexity is O(V^2) for a basic version but can be reduced to O(E + V log V) with a priority queue.

## Space Complexity

- The space complexity for representing a graph using an adjacency list is O(V + E), and for an adjacency matrix, it is O(V^2).
- Graph traversal typically requires O(V) space due to the stack (DFS) or queue (BFS).

## Implementation

```python
# Python implementation for Graph Traversal (DFS)

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_edge(self, u, v):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append(v)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        for neighbor in self.adjacency_list.get(vertex, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
