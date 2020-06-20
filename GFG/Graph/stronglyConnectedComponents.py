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
        self.stack = []

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
            print(u.getName(),'->', [v.getName() for v in self.getToVertices(u)])

    # Returns the name of the vertex
    def getVertexName(self, vertex):
        return vertex.getName()

    def transposeGraph(self):
        edges = {}
        for vertex in self.getEdges():
            edges[vertex] = []
        for fromVertex in self.getEdges():
            for toVertex, weight in self.edges[fromVertex]:
                if not self.directed:
                    edges[fromVertex].append([toVertex, weight])
                    edges[toVertex].append([fromVertex, weight])
                else:
                    edges[toVertex].append([fromVertex, weight])
        self.edges = edges

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

    def dfsForSCC(self):
        for u in self.getEdges():
            u.setSeen(False)
        for u in self.getEdges():
            if not u.getSeen():
                self.dfsForSCCUtil(u)
    
    def dfsForSCCUtil(self, u):
        u.setSeen(True)
        for v in self.getToVertices(u):
            if not v.getSeen():
                self.dfsForSCCUtil(v)
        self.stack.append(u)

    def getStronglyConnectedComponents(self):
        self.dfsForSCC()
        self.transposeGraph()
        self.depthFirstSearch()
        print(self.components)
    

if __name__=="__main__":
    g = Graph(True, False)
    vertexZero = g.addVertex(0)
    vertexOne = g.addVertex(1)
    vertexTwo = g.addVertex(2)
    vertexThree = g.addVertex(3)
    vertexFour = g.addVertex(4)
    g.addEdge(vertexOne, vertexZero)
    g.addEdge(vertexZero, vertexTwo)
    g.addEdge(vertexTwo, vertexOne)
    g.addEdge(vertexZero, vertexThree)
    g.addEdge(vertexThree, vertexFour)
    g.getStronglyConnectedComponents()