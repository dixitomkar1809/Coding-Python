# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there
is no valid build order, return an error.
    EXAMPLE
        Input:
        projects: a, b, c, d, e, f
        dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
        Output: f, e, a, b, d, c
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
    g.addEdge(A, D)
    g.addEdge(F, B)
    g.addEdge(B, D)
    g.addEdge(F, A)
    g.addEdge(D, C)
    print(g.topologicalSort())