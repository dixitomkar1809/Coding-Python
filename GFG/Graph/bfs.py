# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a directed graph. The task is to do Breadth First Search of this graph.
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
    def bfs(self):
        if len(self.getEdges()) == 0:
            return "Empty Graph"
        visitied = {}
        stack = []
        for u in self.getEdges():
            visitied[u] = False
        source = list(self.getEdges().keys())[0]
        queue = [source]
        visitied[source] = True
        stack = []
        while queue:
            s = queue.pop(0)
            stack.append(s)
            for v in self.getToVertices(s):
                if not visitied[v]:
                    queue.append(v)
                    visitied[v] = True
        return stack

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
    graph.addEdge(two, four)
    print(graph.bfs())

