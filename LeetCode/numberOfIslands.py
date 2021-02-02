# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/number-of-islands/

# Time Complexity: O(m*n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    self.islandHelper(i, j, grid)
                    islands += 1
        return islands
    
    def islandHelper(self, i, j, grid):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '*'
        self.islandHelper(i+1, j, grid)
        self.islandHelper(i-1, j, grid)
        self.islandHelper(i, j+1, grid)
        self.islandHelper(i, j-1, grid)
        return
            