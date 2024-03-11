# Advanced Graphs

## Explanation

Advanced graph algorithms delve into more complex problems and solutions, including those that handle weighted graphs, directed graphs, and those that require specific properties like connectivity, shortest paths, or network flows.

## Example Problems

- **Dijkstra's Algorithm:** Find the shortest paths from a source vertex to all other vertices in a weighted graph.
- **Bellman-Ford Algorithm:** Compute shortest paths from a single source vertex to all other vertices in a weighted digraph, even with negative weights.
- **Floyd-Warshall Algorithm:** Find shortest paths between all pairs of vertices in a weighted graph.
- **Network Flow:** Maximize the flow in a network using the Ford-Fulkerson algorithm or its optimized version called Edmonds-Karp.

## Time Complexity

- **Dijkstra's Algorithm:** O(V^2), but with a min-priority queue, it can be reduced to O(V + E log V).
- **Bellman-Ford Algorithm:** O(V * E), which can be costly for dense graphs.
- **Floyd-Warshall Algorithm:** O(V^3), suitable for dense graphs where V is manageable.
- **Ford-Fulkerson Algorithm:** O(E * max_flow), where E is the number of edges.

## Space Complexity

- Space complexity for these algorithms is often O(V^2), especially for methods like Floyd-Warshall, which maintain a matrix of distances.

## Implementation

```python
# Python implementation for Dijkstra's Algorithm

import heapq

def dijkstra(graph, start_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start_vertex] = 0
    priority_queue = [(0, start_vertex)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances
    
# Example usage:
if __name__ == "__main__":
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    start_vertex = 'A'
    distances = dijkstra(graph, start_vertex)
    print(f"Shortest distances from {start_vertex}: {distances}")