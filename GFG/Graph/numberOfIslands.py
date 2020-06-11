# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Matrix consisting of 0s and 1s. Find the number of islands of connected 1s present in the matrix. 
'''

class Solution:
    def numberOfIslands(self, matrix):
        if not matrix:
            return 0
        islands = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    self.numberOfIslandsHelper(matrix, i, j)
                    islands += 1
        return islands

    def numberOfIslandsHelper(self, matrix, i, j):
        if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0 or matrix[i][j] != 1:
            return 
        matrix[i][j] = '*'
        self.numberOfIslandsHelper(matrix, i, j+1)
        self.numberOfIslandsHelper(matrix, i, j-1)
        self.numberOfIslandsHelper(matrix, i+1, j)
        self.numberOfIslandsHelper(matrix, i+1, j+1)
        self.numberOfIslandsHelper(matrix, i+1, j-1)
        self.numberOfIslandsHelper(matrix, i-1, j+1)
        self.numberOfIslandsHelper(matrix, i-1, j-1)
        self.numberOfIslandsHelper(matrix, i-1, j)

if __name__=="__main__":
    matrix = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
    sol = Solution()
    print(sol.numberOfIslands(matrix))