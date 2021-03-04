# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: O(m*n*max(m, n)) m is number of rows in maze, n is number of columns

# Time Complexity: 

import collections
import heapq

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        self.maze = maze
        queue = collections.deque([start])
        minDistance = []
        for _ in range(len(self.maze)):
            minDistance.append([float('inf')] * len(self.maze[0]))
        minDistance[start[0]][start[1]] = 0
        print(minDistance)
        self.directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue:
            location = queue.popleft()
            for direction in self.directions:
                newI, newJ = location[0] + direction[0], location[1] + direction[1]
                tempDistance = 0
                while self.isValid(newI, newJ):
                    newI, newJ = direction[0] + newI, direction[1] + newJ
                    tempDistance += 1
                if minDistance[newI-direction[0]][newJ-direction[1]] > minDistance[location[0]][location[1]] + tempDistance:
                    minDistance[newI-direction[0]][newJ-direction[1]] = minDistance[location[0]][location[1]] + tempDistance
                    queue.append((newI-direction[0], newJ-direction[1]))
        print(minDistance)
        return -1 if minDistance[destination[0]][destination[1]] == float('inf') else minDistance[destination[0]][destination[1]]
    
    def isValid(self, i, j):
        return i >= 0 and j >= 0 and i < len(self.maze) and j < len(self.maze[0]) and self.maze[i][j] == 0