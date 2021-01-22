# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location
represents the height above sea level. A value of zero indicates water. A pond is a region of water
connected vertically, horizontally, or diagonally. The size of the pond is the total number of
connected water cells. Write a method to compute the sizes of all ponds in the matrix.
EXAMPLE
Input:
0 2 1 0
0 1 0 1
1 1 0 1   
0 1 0 1                                   
Output: 2, 4, 1 (in any order)
'''

# Time Complexity: O(m*n) m is rows, n is cols

def solution(grid):
    sizes = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                size = dfs(grid, i, j, 0)
                sizes.append(size)
    return sizes

def dfs(grid, i, j, size):
    size += 1
    grid[i][j] = '*'
    if (isValid(grid, i+1, j)):
        size = dfs(grid, i+1, j, size)
    if (isValid(grid, i-1, j)):
        size = dfs(grid, i-1, j, size)
    if (isValid(grid, i, j+1)):
        size = dfs(grid, i, j+1, size)
    if(isValid(grid, i,j-1)):
        size = dfs(grid, i, j-1, size)
    if (isValid(grid, i+1, j+1)):
        size = dfs(grid, i+1, j+1, size)
    if (isValid(grid, i+1, j-1)):
        size = dfs(grid, i+1, j-1, size)
    if (isValid(grid, i-1, j-1)):
        size = dfs(grid, i-1, j-1, size)
    if (isValid(grid, i-1, j+1)):
        size = dfs(grid, i-1, j+1, size)
    return size

def isValid(grid, i, j):
    if (i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 0 or i < 0 or j < 0):
        return False
    return True

if __name__ == "__main__":
    print(solution([[0,2,1,0], [0,1,0,1], [1,1,0,1], [0,1,0,1]]))