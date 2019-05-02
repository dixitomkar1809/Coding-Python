# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Graph 

from collections import defaultdict

class Vertex:
    def __init__(self, value):
        self.name = value
        self.color = "white"
    
    def getName(self):
        return self.name

class Graph:
    def __init__(self):
        # List of Edges Source(vertex) to Destination(Vertex)
        self.edges = {}

    def getToVertices(self, source):
        return self.edges[source]
    
    def addEdge(self, fromVertex, toVertex):
        if fromVertex not in self.edges or toVertex not in self.edges:
            return False
        self.edges[fromVertex].append(toVertex)
        self.edges[toVertex].append(fromVertex)
        return  True
    
    def getEdges(self):
        return self.edges

    def addVertex(self, value):
        vertex = Vertex(value)
        self.edges[vertex] = []
        return vertex
    
    def getVertexName(self, vertex):
        return vertex.getName()
    
    def depthFirstSearch(self):
        if len(self.getEdges())==0:
            return "Empty Graph"
        visited = {}
        stack = []
        for vertex in self.getEdges():
            visited[vertex] = False
        for vertex in self.getEdges():
            if not visited[vertex]:
                self.__dfsVisit(visited, vertex, stack)
        return stack

    def __dfsVisit(self, visited, vertex, stack):
        visited[vertex] = True
        stack.append(vertex)
        for v in self.getToVertices(vertex):
            if not visited[v]:
                self.__dfsVisit(visited, v, stack)
        return 

    def breadthFirstSearch(self):
        if len(self.getEdges())==0:
            return "Empty Graph"
        visited = {}
        for vertex in self.getEdges():
            visited[vertex] = False
        source = list(self.getEdges().keys())[0]
        queue = [source]
        visited[source] = True
        stack = []
        while queue:
            s = queue.pop(0)
            stack.append(s)
            for v in self.getToVertices(s):
                if not visited[v]:
                    queue.append(v)
                    visited[v] = True
        return stack
        
