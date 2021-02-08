# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/critical-connections-in-a-network/     

# Time Complexity: O(V + E)

import collections

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.graph = collections.defaultdict(list)
        for u, v in connections:
            self.graph[u].append(v)
            self.graph[v].append(u)
        self.discovery = [float('-inf')] * len(self.graph)
        self.low = [float('-inf')] * len(self.graph)
        self.visited = [False] * len(self.graph)
        self.timer = 0
        self.parent = [None] * len(self.graph)
        self.criticalConnectionsList = []
        for u in self.graph:
            if not self.visited[u]:
                self.criticalConnectionsUtil(u)
        return self.criticalConnectionsList
    
    def criticalConnectionsUtil(self, u):
        self.visited[u] = True
        self.discovery[u] = self.timer
        self.low[u] = self.timer
        self.timer += 1
        for v in self.graph[u]:
            if not self.visited[v]:
                self.parent[v] = u
                self.criticalConnectionsUtil(v)
                if self.low[v] > self.discovery[u]:
                    self.criticalConnectionsList.append([u, v])
                self.low[u] = min(self.low[u], self.low[v])
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.discovery[v])
        
        