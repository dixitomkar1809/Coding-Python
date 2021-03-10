# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-string/

# Time Complexity: O(n) n is number of chars

import collections
import heapq

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        return self.reverseStringHelper(s, 0, len(s)-1)
    
    def reverseStringHelper(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s