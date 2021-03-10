# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-words-in-a-string/

# Time Complexity: O(n) n is number of words

import collections
import heapq

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip().split(' ')
        stringList = []
        for string in s:
            if string:
                stringList.append(string)
        stringList = self.reverseStringHelper(stringList, 0, len(stringList)-1)
        return ' '.join(stringList)
    
    def reverseStringHelper(self, s, i, j):
        while i < j:
            s[i], s[j] = s[j], s[i]
            i+=1
            j-=1
        return s