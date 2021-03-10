# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-words-in-a-string-iii/

# Time Complexity: O(n) n is number of chars in s

import collections
import heapq

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(' ')
        for i, string in enumerate(s):
            s[i] = self.reverseStringHelper(string, 0, len(string)-1)
        return ' '.join(s)
    
    def reverseStringHelper(self, s, i, j):
        s = list(s)
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return ''.join(s)
        