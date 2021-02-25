# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-string-ii/

# Time Complexity: O(n) n is number of chars in s

import collections
import heapq

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        i = 0
        while i < len(s):
            if (i + k) < len(s):
                s = s[:i] + s[i:i+k][::-1] + s[i+k:]
            else:
                s = s[:i] + s[i:][::-1]
            i += (2 * k)
        return s 
        