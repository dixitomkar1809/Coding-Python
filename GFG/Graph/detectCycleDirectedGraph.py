# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Undirected Graph. Check whether it contains a cycle or not. 
'''

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
                print('here')
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

    # Time Complexity: O(V + E).
    def hasCycle(self):
        if len(self.getEdges()) == 0:
            return 'Empty Graph'
        visited = {}
        stack = {}
        for u in self.getEdges():
            visited[u] = False
            stack[u] = False
        for u in self.getEdges():
            if not visited[u]:
                if self.hasCycleHelper(u, visited, stack):
                    return True
        return False
    
    def hasCycleHelper(self, u, visited, stack):
        visited[u] = True
        stack[u] = True
        for v in self.getToVertices(u):
            if not visited[v]:
                if self.hasCycleHelper(v, visited, stack):
                    return True
            elif stack[v]:
                return True
        return False

if __name__=="__main__":
    graph = Graph(True)
    zero = graph.addVertex(0)
    one = graph.addVertex(1)
    two = graph.addVertex(2)
    three = graph.addVertex(3)
    four = graph.addVertex(4)
    graph.addEdge(zero, one)
    graph.addEdge(zero, two)
    graph.addEdge(zero, three)
    graph.addEdge(zero, four)
    # graph.addEdge(four, three)
    print(graph.hasCycle())

