# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/armstrong-number/

# Time Complexity: O(n) n is number of digits

import collections
import heapq

class Solution(object):
    def isArmstrong(self, N):
        """
        :type N: int
        :rtype: bool
        """
        summ = 0
        k = len(str(N))
        for char in str(N):
            summ += (int(char) ** k)
        if summ == N:
            return True
        return False
        