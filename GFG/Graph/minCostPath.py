# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a square grid of size N, each cell of which contains integer cost which represents a cost to traverse through that cell, we need to find a path from top left cell to bottom right cell by which total cost incurred is minimum. You can move in 4 directions : up, down, left an right.
'''

# Time Complexity: O(R*C)

class Solution:
    def minCostPath(self, matrix):
        R = len(matrix)
        C = len(matrix[0])
        cost = [[float('inf') for _ in range(C)] for _ in range(R)]
        rowChange = [-1, 0, 1, 0]
        colChange = [0, 1, 0, -1]
        cost[0][0] = matrix[0][0]
        stack = [(0, 0, 0)]
        while stack:
            i, j, value = stack.pop(0)
            for k in range(4):
                newI = i + rowChange[k]
                newJ = j + colChange[k]
                if not self.isValid(matrix, newI, newJ):
                    continue
                if cost[newI][newJ] > cost[i][j] + matrix[newI][newJ]:
                    cost[newI][newJ] = cost[i][j] + matrix[newI][newJ]
                    stack.append((newI, newJ, cost[newI][newJ]))
        return cost[-1][-1]

    def isValid(self, matrix, i, j):
        return i < len(matrix) and j < len(matrix[0]) and i >= 0 and j >= 0

if __name__=='__main__':
    sol = Solution()
    matrix = [[31, 100, 65, 12, 18], 
              [10, 13, 47, 157, 6], 
              [100, 113, 174, 11, 33], 
              [88, 124, 41, 20, 140], 
              [99, 32, 111, 41, 20 ]]
    print(sol.minCostPath(matrix))