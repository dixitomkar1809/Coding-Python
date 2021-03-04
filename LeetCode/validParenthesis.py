# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/valid-parentheses/

# Time Complexity: O(n) n is number of chars in s

import collections
import heapq

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char in ['(', '{',  '[']:
                stack.append(char)
            else:
                if not stack or stack[-1] != self.getOpening(char):
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True
    
    def getOpening(self, char):
        if char == ')':
            return '('
        if char == '}':
            return '{'
        if char == ']':
            return '['
        