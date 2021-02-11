# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/course-schedule-ii/

# Time Complexity: O(V + E) V is number of courses E is number of prereqs

import collections
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        self.graph = collections.defaultdict(list)
        self.indegree = {u: 0 for u in range(numCourses)}
        self.color = ['white'] * numCourses
        self.stack = []
        self.isPossible = True
        for v, u in prerequisites:
            self.graph[u].append(v)
        for u in range(numCourses):
            if self.color[u] == 'white':
                self.dfs(u)
        return self.stack[::-1] if self.isPossible else []
    
    def dfs(self, u):
        self.color[u] = 'gray'
        if not self.isPossible:
            return
        for v in self.graph[u]:
            if self.color[v] == 'white':
                self.dfs(v)
            elif self.color[v] == 'gray':
                self.isPossible = False
        self.color[u] = 'black'
        self.stack.append(u)
            