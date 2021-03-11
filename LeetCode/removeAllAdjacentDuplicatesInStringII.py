# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/  

# Time Complexity: O(n) n is number of chars in s

import collections
import heapq

class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        stack = []
        for char in s:
            if stack and stack[-1][0] == char:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([char, 1])
        result = ''
        for char, count in stack:
            result += (char * count)
        return result
            