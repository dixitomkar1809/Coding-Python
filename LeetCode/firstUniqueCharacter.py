# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/first-unique-character-in-a-string/

# Time Complexity: O(n) n is number of chars

import collections
import heapq

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = collections.Counter(list(s))
        print(counts)
        for i, char in enumerate(s):
            if counts[char] == 1:
                return i
        return -1