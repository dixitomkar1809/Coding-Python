# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a 2D screen, location of a pixel in the screen ie(x,y) and a color(K), your task is to replace color of the given pixel and all adjacent(excluding diagonally adjacent) same colored pixels with the given color K.
'''

class Solution:
    def floodFill(self, matrix, i, j, oldColor, newColor):
        if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0 or matrix[i][j] != oldColor or matrix[i][j] == newColor:
            return
        matrix[i][j] = newColor
        self.floodFill(matrix, i+1, j, oldColor, newColor)
        self.floodFill(matrix, i-1, j, oldColor, newColor)
        self.floodFill(matrix, i, j+1, oldColor, newColor)
        self.floodFill(matrix, i, j-1, oldColor, newColor)
        return matrix

if __name__=="__main__":
    matrix = [[1, 1, 1, 1, 1, 1, 1, 1],  
              [1, 1, 1, 1, 1, 1, 0, 0],  
              [1, 0, 0, 1, 1, 0, 1, 1],  
              [1, 2, 2, 2, 2, 0, 1, 0],  
              [1, 1, 1, 2, 2, 0, 1, 0],  
              [1, 1, 1, 2, 2, 2, 2, 0],  
              [1, 1, 1, 1, 1, 2, 1, 1],  
              [1, 1, 1, 1, 1, 2, 2, 1]]
    i, j = 4, 4
    newColor = 3
    oldColor = matrix[i][j]
    sol = Solution()
    print(sol.floodFill(matrix, i, j, oldColor, newColor))