# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-words-in-a-string-ii/

# Time Complexity: O(n) n is number of chars

import collections
import heapq

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        self.reverseStringHelper(s, 0, len(s)-1)
        self.reverseEachWord(s)
    
    def reverseEachWord(self, s):
        i = 0
        j = 0
        while i < len(s) :
            while j < len(s) and s[j] != ' ':
                j += 1
            self.reverseStringHelper(s, i, j-1)
            i = j + 1
            j += 1
                
        
    def reverseStringHelper(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s