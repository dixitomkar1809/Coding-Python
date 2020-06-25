# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a N X N matrix (M) filled with 1, 0, 2, 3. The task is to find whether there is a path possible from source to destination, while traversing through blank cells only. You can traverse up, down, right and left.

A value of cell 1 means Source.
A value of cell 2 means Destination.
A value of cell 3 means Blank cell.
A value of cell 0 means Blank Wall.
'''

# Time Complexity: O(m*n)

class Solution:
    def findWhetherPathExists(self, matrix):
        source = None
        destination = None
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    source = [matrix[i][j], i, j]
                    break
        if not source:
            return None
        queue = [source]
        while queue:
            print(queue)
            val, i, j = queue.pop(0)
            if val == 2:
                return 1
            matrix[i][j] = 0
            if self.isValid(matrix, i+1, j):
                queue.append([matrix[i+1][j], i+1, j])
            if self.isValid(matrix, i-1, j):
                queue.append([matrix[i-1][j], i-1, j])
            if self.isValid(matrix, i, j+1):
                queue.append([matrix[i][j+1], i, j+1])
            if self.isValid(matrix, i, j-1):
                queue.append([matrix[i][j-1], i, j-1])
        return 0
            
    def isValid(self, matrix, i, j):
        return i >= len(matrix) and j >= len(matrix[0]) and i < 0 and j < 0 and matrix[i][j] != 0

if __name__=='__main__':
    sol = Solution()
    matrix = [[3, 0, 0, 0],
              [0, 3, 3, 0],
              [0, 1, 0, 3],
              [0, 3, 3, 3]]
    print(sol.findWhetherPathExists(matrix))
    