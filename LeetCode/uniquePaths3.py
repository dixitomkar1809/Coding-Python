# Author: Omkar Dixit
# Email: omedxt@gmail.com

#Link: https://leetcode.com/problems/unique-paths-iii/

# Time Complexity: O(3 ^ N) as there will be only 3 directions to be checked for each node as the last direction we wont be checking

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.ans = 0
        self.grid = grid
        self.directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        src = []
        non_obstacles = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= 0:
                    non_obstacles += 1
                if grid[i][j] == 1:
                    src = [i, j]
        self.dfs(src[0], src[1], non_obstacles)
        return self.ans
    
    def dfs(self, i, j, non_obstacles):
        if self.grid[i][j] == 2 and non_obstacles == 1:
            self.ans += 1
            return
        temp = self.grid[i][j]
        self.grid[i][j] = -4
        non_obstacles -= 1
        for direction in self.directions:
            newI, newJ = i + direction[0], j + direction[1]
            if not (newI >= 0 and newI < len(self.grid) and newJ >= 0 and newJ < len(self.grid[0])):
                continue
            if self.grid[newI][newJ] < 0:
                continue
            self.dfs(newI, newJ, non_obstacles)
        self.grid[i][j] = temp