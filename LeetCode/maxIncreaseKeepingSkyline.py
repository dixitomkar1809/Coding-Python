# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/max-increase-to-keep-city-skyline/

# Time Complexity: O(n*m) n is len(grid) and m is len(grid[0])

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        hormax = []
        vermax = []
        ans = 0
        for i in range(len(grid)):
            currmax = float('-inf')
            for j in range(len(grid[0])):
                currmax = max(currmax, grid[i][j])
            hormax.append(currmax)
        for i in range(len(grid[0])):
            currmax = float('-inf')
            for j in range(len(grid)):
                currmax = max(currmax, grid[j][i])
            vermax.append(currmax)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                ans += (min(hormax[i], vermax[j]) - grid[i][j])
                grid[i][j] = min(hormax[i], vermax[j])
        return ans