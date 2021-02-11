# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# Time Complexity: O(V + E)

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        self.graph = {}
        for i in range(n):
            self.graph[i] = []
        for u, v in edges:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.visited = [False] * n
        connectedComponents = 0
        for u in self.graph:
            if not self.visited[u]:
                self.dfs(u)
                connectedComponents += 1
        return connectedComponents
    
    def dfs(self, u):
        self.visited[u] = True
        for v in self.graph[u]:
            if not self.visited[v]:
                self.dfs(v)
        