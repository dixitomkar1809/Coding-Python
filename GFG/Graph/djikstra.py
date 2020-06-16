# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a graph of V nodes represented in the form of the adjacency matrix. The task is to find the shortest distance of all the vertex's from the source vertex.
'''

import heapq

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
        self.pathHeap = []

    # Returns list of destination vertices from a source with weight,
    # Weight will be None if the graph/edges is/are not weighted
    def getToVertices(self, source):
        if not self.weighted:
            return [[toVertex[0], toVertex[1]] for toVertex in self.edges[source]]
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
    def getEdges(self, vertex = None):
        if not vertex:
            return self.edges
        else:
            return self.edges[vertex]

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

    def djikstra(self, sourceVertex):
        sourceVertex.setSeen(True)
        for toVertex, weight in self.getEdges(sourceVertex):
            entry = [weight, sourceVertex, toVertex]
            heapq.heappush(self.pathHeap, entry)
        while self.pathHeap:
            currWeight, fromV, toV = heapq.heappop(self.pathHeap)
            if not toV.getSeen():
                toV.setSeen(True)
                for toVertex, weight in self.getEdges(toV):
                    entry = [weight, toV, toVertex]
                    heapq.heappush(self.pathHeap, entry)
                print('From:',fromV.getName(), 'To:', toV.getName(), 'Weight:', currWeight)



if __name__=='__main__':
    graph = Graph(False, True)
    zero = graph.addVertex(0)
    one = graph.addVertex(1)
    two = graph.addVertex(2)
    three = graph.addVertex(3)
    four = graph.addVertex(4)
    five = graph.addVertex(5)
    six = graph.addVertex(6)
    seven = graph.addVertex(7)
    eight = graph.addVertex(8)
    graph.addEdge(zero, one, 4)
    graph.addEdge(zero, seven, 8)
    graph.addEdge(one, two, 8)
    graph.addEdge(one, seven, 11)
    graph.addEdge(two, three, 7)
    graph.addEdge(two, eight, 2)
    graph.addEdge(two, five, 4)
    graph.addEdge(three, four, 9)
    graph.addEdge(three, five, 14)
    graph.addEdge(four, five, 10)
    graph.addEdge(five, six, 2)
    graph.addEdge(six, seven, 1)
    graph.addEdge(six, eight, 6)
    graph.addEdge(seven, eight, 7)
    graph.djikstra(zero)