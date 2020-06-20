# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a boolean 2D matrix (0-based index), find whether there is path from (0,0) to (x,y) and if there is one path, print the minimum no of steps needed to reach it, else print -1 if the destination is not reachable. You may move in only four direction ie up, down, left and right. The path can only be created out of a cell if its value is 1.
'''

class Solution:
    def shortestPath(self, matrix, x, y):
        if x > len(matrix) or y > len(matrix) or x < 0 or y < 0:
            return -1
        queue = []
        queue.append((0,0,0))
        minPath = float('inf')
        while queue:
            i, j, path = queue.pop(0)
            if i == x and j == y:
                if path < minPath:
                    minPath = path
            else:
                if self.isValid(i+1, j, matrix):
                    if matrix[i+1][j] == 1:
                        queue.append((i+1, j, path+1))
                        matrix[i+1][j] == '*'
                if self.isValid(i-1, j, matrix):
                    if matrix[i-1][j] == 1:
                        queue.append((i-1, j, path+1))
                        matrix[i-1][j] = '*'
                if self.isValid(i, j+1, matrix):
                    if matrix[i][j+1] == 1:
                        queue.append((i, j+1, path+1))
                        matrix[i][j+1] = '*'
                if self.isValid(i, j-1, matrix):
                    if matrix[i][j-1] == 1:
                        queue.append((i, j-1, path+1))
                        matrix[i][j-1] = '*'
        if minPath == float('inf'):
            return -1
        return minPath

    def isValid(self, i, j, matrix):
        return (i < len(matrix) and j < len(matrix[0]) and i >= 0 and j >= 0)

if __name__=='__main__':
    sol = Solution()
    matrix = [[1,0,0,0],
              [1,1,0,1],
              [0,1,1,1]]
    x = 2
    y = 3
    print(sol.shortestPath(matrix, x, y))