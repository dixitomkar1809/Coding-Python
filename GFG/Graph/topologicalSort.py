# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Directed Graph. Find any Topological Sorting of that Graph.
'''

from collections import defaultdict


class Vertex:
    def __init__(self, value):
        self.name = value
        self.color = "white"

    def getName(self):
        return self.name


class Graph:
    def __init__(self, directed):
        self.directed = directed
        # List of Edges Source(vertex) to Destination(Vertex)
        self.edges = {}

    def getToVertices(self, source):
        return self.edges[source]

    def addEdge(self, fromVertex, toVertex):
        if not self.directed:
            if fromVertex not in self.edges or toVertex not in self.edges:
                return False
            self.edges[fromVertex].append(toVertex)
            self.edges[toVertex].append(fromVertex)
            return True
        else:
            if fromVertex not in self.edges or toVertex not in self.edges:
                return False
            self.edges[fromVertex].append(toVertex)

    def getEdges(self):
        return self.edges

    def getVertices(self):
        return [vertex for vertex in self.edges]

    def addVertex(self, value):
        vertex = Vertex(value)
        self.edges[vertex] = []
        return vertex

    def getVertexName(self, vertex):
        return vertex.getName()

    def topologicalSort(self):
        visited = {}
        stack = []
        for vertex in self.getVertices():
            visited[vertex] = False
        for u in self.getVertices():
            if not visited[u]:
                self.__topologicalSortUtil(visited, u, stack)
        return stack

    def __topologicalSortUtil(self, visited, u, stack):
        visited[u] = True
        for v in self.edges[u]:
            if not visited[v]:
                self.__topologicalSortUtil(visited, v, stack)
        stack.insert(0, self.getVertexName(u))
