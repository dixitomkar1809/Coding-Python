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
            return  True
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
    
    def checkRoute(self, source, destination):
        if len(self.getEdges())==0:
            return "Empty Graph"
        visited = []
        if source not in self.edges or destination not in self.edges:
            return "Not in the Graph"
        queue = []
        queue.append(source)
        visited.append(source)
        while queue:
            s = queue.pop(0)
            for v in self.getToVertices(s):
                if v not in visited:
                    queue.append(v)
                    visited.append(v)
                    if v==destination:
                        return True
        return False
        
    def topologicalSort(self):
        visited={} 
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