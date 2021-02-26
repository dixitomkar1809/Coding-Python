# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/flood-fill/

# Time Complexity: O(M) m is number of pixels

import collections
import heapq

class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        self.image = image
        self.startingColor = self.image[sr][sc]
        self.newColor = newColor
        if self.startingColor == self.newColor:
            return self.image
        queue = collections.deque([[sr, sc]])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        while queue:
            row, col = queue.popleft()
            self.image[row][col] = self.newColor
            for direction in directions:
                newRow, newCol = row + direction[0], col + direction[1]
                if self.isValid(newRow, newCol):
                    queue.append([newRow, newCol])
        return self.image
    
    def isValid(self, i, j):
        return i >= 0 and j >= 0 and i < len(self.image) and j < len(self.image[0]) and self.image[i][j] == self.startingColor