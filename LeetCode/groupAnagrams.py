# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/group-anagrams/

# Time Complexity: O(n * k) n is number of strings, k is number of chars in string

import collections
import heapq

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        myDict = collections.defaultdict(list)
        for string in strs:
            letterCounts = [0] * 26
            for char in string:
                letterCounts[ord(char)-ord('a')] += 1
            myDict[tuple(letterCounts)].append(string)
        return list(myDict.values())
            