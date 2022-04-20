#course_schedule:  https://leetcode.com/problems/course-schedule-ii/
# Depth First Search: https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/

test = [[3,1],[3,2]]

def findOrder(numCourses, prerequisites):
    indegree = [set() for _ in range(numCourses)]
    outdegree = [[] for _ in range(numCourses)]
    for p in prerequisites:
        indegree[p[0]].add(p[1])
        outdegree[p[1]].append(p[0])
    ret, start = [], [i for i in range(numCourses) if not indegree[i]]
    while start: # start contains courses without prerequisites
        newStart = [] 
        for i in start:
            ret.append(i)
            for j in outdegree[i]:
                indegree[j].remove(i)
                if not indegree[j]:
                    newStart.append(j)
        start = newStart # newStart contains new courses with no prerequisites
    return ret if len(ret) == numCourses else [] # can finish if ret contains all courses 



# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
#  The recursive algorithm  to perform DFS traversal on the graph on a graph
def DFS(graph, v, discovered):
 
    discovered[v] = True            # mark the current node as discovered
    print(v, end=' ')               # print the current node
 
    # do for every edge (v, u)
    for u in graph.adjList[v]:
        if not discovered[u]:       # if `u` is not yet discovered
            DFS(graph, u, discovered)
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # Perform DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            DFS(graph, i, discovered)



 
# Perform iterative DFS on graph starting from vertex `v`
from collections import deque
 
 
# A class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, edges, n):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(n)]
 
        # add edges to the undirected graph
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
 
 
# Perform iterative DFS on graph starting from vertex `v`
def iterativeDFS(graph, v, discovered):
 
    # create a stack used to do iterative DFS
    stack = deque()
 
    # push the source node into the stack
    stack.append(v)
 
    # loop till stack is empty
    while stack:
 
        # Pop a vertex from the stack
        v = stack.pop()
 
        # if the vertex is already discovered yet, ignore it
        if discovered[v]:
            continue
 
        # we will reach here if the popped vertex `v` is not discovered yet;
        # print `v` and process its undiscovered adjacent nodes into the stack
        discovered[v] = True
        print(v, end=' ')
 
        # do for every edge (v, u)
        adjList = graph.adjList[v]
        for i in reversed(range(len(adjList))):
            u = adjList[i]
            if not discovered[u]:
                stack.append(u)
 
 
if __name__ == '__main__':
 
    # List of graph edges as per the above diagram
    edges = [
        # Notice that node 0 is unconnected
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (8, 12), (9, 10), (9, 11)
        # (6, 9) introduces a cycle
    ]
 
    # total number of nodes in the graph (labelled from 0 to 12)
    n = 13
 
    # build a graph from the given edges
    graph = Graph(edges, n)
 
    # to keep track of whether a vertex is discovered or not
    discovered = [False] * n
 
    # Do iterative DFS traversal from all undiscovered nodes to
    # cover all connected components of a graph
    for i in range(n):
        if not discovered[i]:
            iterativeDFS(graph, i, discovered)