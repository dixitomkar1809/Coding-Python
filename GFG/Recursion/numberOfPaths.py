# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
The problem is to count all the possible paths from top left to bottom right of a MxN matrix with the constraints that from each cell you can either move to right or down.
'''

# Time Complexity: T(m*n)

class Solution:
    def __init__(self):
        self.paths = 0
    
    def numberOfPaths(self, map):
        self.__numberOfPathsHelper(map, 0, 0, len(map)-1, len(map[0])-1)

    def __numberOfPathsHelper(self, map, i, j, endI, endJ):
        if i >= len(map) or j >= len(map[0]):
            return 
        elif map[i][j] == map[endI][endJ]:
            self.paths += 1
            return 
        else:
            self.__numberOfPathsHelper(map, i, j+1, endI, endJ)
            self.__numberOfPathsHelper(map, i+1, j, endI, endJ)
        
        

if __name__=="__main__":
    sol = Solution()
    map = [['A','B','C'],['D','E','F'],['G','H','I']]
    sol.numberOfPaths(map)
    print(sol.paths)