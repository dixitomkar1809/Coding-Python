# Author: Omkar Dixit
# Email: omedxt@gmail.com 

# link: https://leetcode.com/problems/prison-cells-after-n-days/

# Time Complexity: O(n)

class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        N = (N-1)%14 +1
        for _ in range(N):
            tempCells = [0] * len(cells)
            for j in range(1, len(cells)-1):
                if cells[j-1] == cells[j+1]:
                    tempCells[j] = 1
            print(tempCells)
            cells = tempCells
        return cells
        