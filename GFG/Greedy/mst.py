# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a weighted, undirected and connected graph. The task is to find the sum of weights of the edges of the Minimum Spanning Tree.
'''

from heapq import heapify, heappop, heappush, heappushpop

class Solution:
    def minimumSpanningTree(self, graph):
        mstSum = 0
        visited = {}
        for u in graph:
            visited[u] = False
        queue = []
        source = list(graph)[0]
        for v, w in graph[source]:
            heappush(queue, [w,source,v])
        visited[source] = True
        while queue:
            w, u, v = heappop(queue)
            if not visited[v]:
                mstSum += w
            visited[v] = True
            for toVertex, weight in graph[v]:
                if not visited[toVertex]:
                    heappush(queue, [weight, v, toVertex])
        return mstSum

if __name__=='__main__':
    sol = Solution()
    graph = {
        1: [(2,5), (3,1)],
        2: [(1,5), (3,3)],
        3: [(2,3), (1,1)]
    }
    print(sol.minimumSpanningTree(graph))