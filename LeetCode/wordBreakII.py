# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/word-break-ii/

# Time Complexity: 

import collections
import heapq

import copy
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordDict = set(wordDict)
        queue = [[s]]
        solDict = {}
        sol = []
        while queue:
            listOfString = queue.pop()
            for i in range(len(listOfString[-1])):
                lastString = listOfString[-1]
                tempList = copy.deepcopy(listOfString)
                if lastString[:i] in wordDict:
                    before = lastString[:i]
                    after = lastString[i:]
                    tempList[-1] = before
                    tempList.append(after)
                    # print(before, after)
                    # print(tempList)
                    queue.append(tempList)
                else:
                    solDict[tuple(tempList)] = 1
        for key in solDict:
            if key[-1] in wordDict:
                print(' '.join(key))
                sol.append(' '.join(key))
        return sol
            