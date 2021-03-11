# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

# Time Complexity: O(n) n is number of chars

import collections
import heapq

class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        sol = []
        for char in S:
            if sol and char == sol[-1]:
                sol.pop()
            else:
                sol.append(char)
        return ''.join(sol)