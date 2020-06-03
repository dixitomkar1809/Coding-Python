# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a connected undirected graph. Perform a Depth First Traversal of the graph.
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
    def dfs(self):
        if len(self.getEdges()) == 0:
            return 'Empty Graph'
        visited = {}
        stack = []
        for u in self.getEdges():
            visited[u] = False
        for u in self.getEdges():
            if not visited[u]:
                self.dfsHelper(u, visited, stack)
        return stack
    
    def dfsHelper(self, u, visited, stack):
        visited[u] = True
        stack.append(u.name)
        for v in self.getToVertices(u):
            if not visited[v]:
                self.dfsHelper(v, visited, stack)
        return

if __name__=="__main__":
    graph = Graph(False)
    zero = Vertex(0)
    one = Vertex(1)
    two = Vertex(2)
    three = Vertex(3)
    four = Vertex(4)
    graph.addVertex(zero)
    graph.addVertex(one)
    graph.addVertex(two)
    graph.addVertex(three)
    graph.addVertex(four)
    graph.addEdge(zero, one)
    graph.addEdge(zero, two)
    graph.addEdge(zero, three)
    graph.addEdge(zero, four)
    print(graph.dfs())

