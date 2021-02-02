# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/number-of-provinces/

# Time Complexity: O(m*n)

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        for i in range(len(isConnected)):
            if (isConnected[i][i] == 1):
                self.dfshelper(i, isConnected)
                count += 1
        return count
    
    def dfshelper(self, i, grid):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = grid[j][i] = -1
                self.dfshelper(j, grid)
        