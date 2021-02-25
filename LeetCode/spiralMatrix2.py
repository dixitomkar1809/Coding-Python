# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/spiral-matrix-ii/

# Time Complexity: O(n^2)

import collections
import heapq

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        rowTop = 0
        colLeft = 0
        rowBottom = n - 1
        colRight = n - 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        k = 1
        while rowTop <= rowBottom and colLeft <= colRight:
            for j in range(colLeft, colRight + 1):
                if matrix[rowTop][j] == 0:
                    matrix[rowTop][j] = k
                    k += 1
            rowTop += 1
            for i in range(rowTop, rowBottom + 1):
                if matrix[i][colRight] == 0:
                    matrix[i][colRight] = k
                    k += 1
            colRight -= 1
            for j in range(colRight, colLeft - 1, -1):
                if matrix[rowBottom][j] == 0:
                    matrix[rowBottom][j] = k
                    k += 1
            rowBottom -= 1
            for i in range(rowBottom, rowTop - 1, -1):
                if matrix[i][colLeft] == 0:
                    matrix[i][colLeft] = k
                    k += 1
            colLeft += 1
        return matrix