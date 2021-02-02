# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/search-a-2d-matrix-ii/

# Time Complexity: O(n + m)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1
        col = 0
        while self.isValid(row, col, matrix):
            if matrix[row][col] == target:
                return True
            elif (matrix[row][col] < target):
                col += 1
            else:
                row -= 1
        
    def isValid(self, row, col, matrix):
        return row >= 0 and row < len(matrix) and col >= 0 and col < len(matrix[0])
        