# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/rotting-oranges/

# Time Complexity: O(m*n)

class Solution(object):
    def orangesRotting(self, grid):
        """  
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        queue = []
        time = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append([i, j, time])
        while queue:
            i, j, timestamp = queue.pop(0)
            time = timestamp
            if self.isValid(i+1, j, grid):
                grid[i+1][j] = 2
                queue.append([i+1, j, timestamp + 1])
            if self.isValid(i-1, j, grid):
                grid[i-1][j] = 2
                queue.append([i-1, j, timestamp + 1])
            if self.isValid(i, j+1, grid):
                grid[i][j+1] = 2
                queue.append([i, j+1, timestamp + 1])
            if self.isValid(i, j-1, grid):
                grid[i][j-1] = 2
                queue.append([i, j-1, timestamp + 1])
        # print(grid)
        # print(timestamp)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time
                
            
    def isValid(self, i, j, grid):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1