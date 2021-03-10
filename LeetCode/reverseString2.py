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
        s= list(s)
        for i in range(0, len(s), 2 * k):
            if (i + k < len(s)):
                s = self.reverseStringHelper(s, i, (i+k-1))
            else:
                s = self.reverseStringHelper(s, i, (len(s)-1))
        s = ''.join(s)
        return s
                
    def reverseStringHelper(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s