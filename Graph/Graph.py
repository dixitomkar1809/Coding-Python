# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Contains
# Graph Class
# DFS
# BFS
# Topological Sort
# Connected Components
# DAG Shortest Path

import sys

class Vertex:
    def __init__(self, value):
        self.name = value
        self.seen = False
        self.distance = 0
        self.parent = None

    def getName(self):
        return self.name

    def setDistance(self, distance):
        self.distance = distance
        return

    def getDistance(self):
        return self.distance

    def setSeen(self, seen):
        self.seen = seen
        return

    def getSeen(self):
        return self.seen

    def setParent(self, parent):
        self.parent = parent
        return

    def getParent(self):
        return self.parent

"""
Graph Class
    directed: Boolean, tells if the graph is directed or not
    edges: Adjacency list of vertices(Source to Destination)
"""
class Graph:
    def __init__(self, directed, weighted):
        self.directed = directed
        self.weighted = weighted
        self.edges = {}
        self.components = 0

    # Returns list of destination vertices from a source with weight,
    # Weight will be None if the graph/edges is/are not weighted
    def getToVertices(self, source):
        if not self.weighted:
            return [toVertex[0] for toVertex in self.edges[source]]
        else:
            return self.edges[source]

    # Adds a new edge to the graph
    # If directed then it adds a edge  from fromVertex to toVertex
    # Else it adds fromVertex to toVertex and toVertex to fromVertex
    # Returns True if the edge is added
    # Returns False if the edge is not added
    def addEdge(self, fromVertex, toVertex, weight=None):
        if not self.directed:
            if fromVertex not in self.edges or toVertex not in self.edges:
                return False
            self.edges[fromVertex].append([toVertex, weight])
            self.edges[toVertex].append([fromVertex, weight])
            return True
        else:
            if fromVertex not in self.edges or toVertex not in self.edges:
                return False
            self.edges[fromVertex].append([toVertex, weight])
            return True

    # Returns all edges
    def getEdges(self):
        return self.edges

    # Returns list of vertices in the graph
    def getVertices(self):
        return [vertex for vertex in self.edges]

    # Creates vertex and adds it to the graph
    # Return the vertex
    def addVertex(self, value):
        vertex = Vertex(value)
        self.edges[vertex] = []
        return vertex

    def printGraph(self):
        for u in self.getEdges():
            print(u.getName(), [(v.getName(), w) for v, w in self.getToVertices(u)])

    # Returns the name of the vertex
    def getVertexName(self, vertex):
        return vertex.getName()

    # Performs Depth First Search
    # Returns a list of vertices in the way they were traversed
    def depthFirstSearch(self):
        if len(self.getEdges()) == 0:
            return "Empty Graph"
        stack = []
        for u in self.getVertices():
            u.setSeen(False)
        for u in self.getVertices():
            if not u.getSeen():
                self.components+=1
                self.__dfsVisit(u, stack)
        return stack

    # Helper function for the DFS
    def __dfsVisit(self, u, stack):
        u.setSeen(True)
        stack.append(u)
        if self.weighted:
            for v, w in self.getToVertices(u):
                if not v.getSeen():
                    self.__dfsVisit(v, stack)
        else:
            for v in self.getToVertices(u):
                if not v.getSeen():
                    self.__dfsVisit(v, stack)
        return

    # Performs Breadth First Search
    # Returns a list of vertices in the way they were traversed
    def breadthFirstSearch(self, source):
        if len(self.getEdges()) == 0:
            return "Empty Graph"
        for u in self.getVertices():
            u.setSeen(False)
        queue = [source]
        source.setSeen(True)
        stack = []
        while queue:
            s = queue.pop(0)
            stack.append(s)
            for v, w in self.getToVertices(s):
                if not v.getSeen():
                    queue.append(v)
                    v.setSeen(True)
        return stack

    # Checks if a route exist between the give source and destination vertex
    # Returns True if path exists
    # Returns False if not
    def checkRoute(self, source, destination):
        if len(self.getEdges()) == 0:
            return "Empty Graph"
        if source not in self.getVertices() or destination not in self.getVertices():
            return "Not in the Graph"
        queue = []
        queue.append(source)
        source.setSeen(True)
        while queue:
            s = queue.pop(0)
            for v, w in self.getToVertices(s):
                if not v.getSeen():
                    queue.append(v)
                    v.setSeen(True)
                    if v == destination:
                        return True
        return False

    # Performs Topological Sort on the graph
    # Returns a list of topologically sorted vertices of the graph
    def topologicalSort(self):
        visited = {}
        stack = []
        for vertex in self.getVertices():
            visited[vertex] = False
        for u in self.getVertices():
            if not visited[u]:
                self.__topologicalSortUtil(visited, u, stack)
        return stack

    # Helper function for Topological Sort
    def __topologicalSortUtil(self, visited, u, stack):
        visited[u] = True
        for v, w in self.edges[u]:
            if not visited[v]:
                self.__topologicalSortUtil(visited, v, stack)
        stack.insert(0, u)

    # Finds the shortest path for a Directed Acyclic Graph
    def dagShortestPath(self):
        if not self.directed:
            return False
        topologicalSortList = g.topologicalSort()
        for u in topologicalSortList:
            u.setDistance(float("inf"))
            u.setParent(None)
        topologicalSortList[0].setDistance(0)
        for u in topologicalSortList:
            for v, w in self.getToVertices(u):
                if u.getDistance() != float("inf") and v.getDistance() > u.getDistance() + w:
                    v.setDistance(u.getDistance() + w)
                    v.setParent(u)
        return

    # Returns number of connected components in the graph
    def getConnectedComponents(self):
        self.components = 0
        self.depthFirstSearch()
        return self.components

if __name__=="__main__":
    g = Graph(True, True)
    vertexZero = g.addVertex(0)
    vertexOne = g.addVertex(1)
    vertexTwo = g.addVertex(2)
    vertexThree = g.addVertex(3)
    vertexFour = g.addVertex(4)
    vertexFive = g.addVertex(5)
    vertexSix = g.addVertex(6)
    vertexSeven = g.addVertex(7)
    g.addEdge(vertexZero, vertexSix, 2)
    g.addEdge(vertexOne, vertexSix, 8)
    g.addEdge(vertexOne, vertexFour, 1)
    g.addEdge(vertexOne, vertexTwo, -4)
    g.addEdge(vertexThree, vertexZero, 3)
    g.addEdge(vertexThree, vertexFour, 5)
    g.addEdge(vertexFive, vertexOne, 2)
    g.addEdge(vertexSeven, vertexFive, -4)
    g.addEdge(vertexSeven, vertexOne, -1)
    g.addEdge(vertexSeven, vertexZero, 6)
    g.addEdge(vertexSeven, vertexThree, 5)
    print(g.checkRoute(vertexFour, vertexSeven))