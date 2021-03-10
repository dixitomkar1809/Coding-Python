# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/reverse-vowels-of-a-string/

# Time Complexity: O(n) n is number of chars in string

import collections
import heapq

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowelStack = []
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        for char in s:
            if char in vowels:
                vowelStack.append(char)
        for i, char in enumerate(list(s)):
            if char in vowels:
                s[i] = vowelStack.pop()
        return ''.join(s)