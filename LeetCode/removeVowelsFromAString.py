# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/remove-vowels-from-a-string/

# Time Complexity: O(n) n is number of chars in s

import collections
import heapq

class Solution(object):
    def removeVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol = ''
        for char in s:
            if char not in ['a', 'e', 'i', 'o', 'u']:
                sol += char
        return sol