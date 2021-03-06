# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Route Between Nodes: Given a directed graph, design an algorithm to find out whether there is a
route between two nodes.
'''

from graph import *

if __name__=="__main__":
    g = Graph(True)
    A = g.addVertex("A")
    B = g.addVertex("B")
    C = g.addVertex("C")
    D = g.addVertex("D")
    E = g.addVertex("E")
    F = g.addVertex("F")
    G = g.addVertex("G")
    g.addEdge(A, B)
    g.addEdge(A, C)
    g.addEdge(B, D)
    g.addEdge(B, E)
    g.addEdge(C, E)
    g.addEdge(D, E)
    g.addEdge(D, F)
    g.addEdge(E, F)
    print(g.checkRoute(E, A))