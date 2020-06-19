# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a matrix of dimension r*c where each cell in the matrix can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

So, we have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. If it is impossible to rot every orange then simply return -1.
'''

# Time Complexity: O(m*n)

class Solution:
    def __init__(self, matrix):
        self.counter = 0
        self.matrix = matrix
        self.fresh = self.getFresh()
    
    def rottenOranges(self):
        return self.rottenOrangesHelper()

    def rottenOrangesHelper(self):
        queue = [(-1, -1)]
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 2:
                    queue.append((i, j))
        return self.setRotten(queue)


    def getFresh(self):
        freshOranges = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 1:
                    freshOranges += 1  
        return freshOranges

    def setRotten(self, queue):
        delimeter = queue.pop(0)
        tempFresh = self.fresh
        while queue:
            i, j = queue.pop(0)
            if self.isValid(i+1, j):
                if self.matrix[i+1][j] == 1:
                    self.matrix[i+1][j] = 2
                    self.fresh-=1
            if self.isValid(i-1, j):
                if self.matrix[i-1][j] == 1:
                    self.matrix[i-1][j] = 2
                    self.fresh-=1
            if self.isValid(i, j+1):
                if self.matrix[i][j+1] == 1:
                    self.matrix[i][j+1] = 2
                    self.fresh-=1
            if self.isValid(i, j-1):
                if self.matrix[i][j-1] == 1:
                    self.matrix[i][j-1] = 2
                    self.fresh-=1
        self.counter+=1
        if self.fresh==0:
            return self.counter
        elif tempFresh != self.fresh:
            return self.rottenOrangesHelper()
        else:
            return -1

    def isValid(self, i, j):
        return (i >= 0 and j >= 0 and i < len(self.matrix) and j < len(self.matrix[0]));


if __name__=='__main__':
    matrix = [[2,1,0,2,1],
              [1,0,1,2,1],
              [1,0,0,2,1]]
    sol = Solution(matrix)
    print(sol.rottenOranges())