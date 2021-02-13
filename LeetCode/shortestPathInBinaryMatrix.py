# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/shortest-path-in-binary-matrix/

# Time Complexity: O(M*N) M is rows, N is cols

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        queue = [(0, 0, 1)]
        endI, endJ = len(grid) - 1, len(grid[0]) - 1
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        while queue:
            i, j, currDistance = queue.pop(0)
            if i == endI and j == endJ:
                return currDistance 
            else:
                for direction in directions:
                    if self.isValid(i + direction[0], j + direction[1], grid):
                        queue.append((i + direction[0], j + direction[1], currDistance + 1))
                        grid[i + direction[0]][j + direction[1]] = '*'
        return -1
    
    def isValid(self, i, j, grid):
        return i >= 0 and i < len(grid) and j >= 0 and j < len(grid) and grid[i][j] == 0