# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/

# Time Complexity: O(nLogn) n is number of dominoes

import collections

class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        myDict = collections.defaultdict(int)
        for i in range(len(dominoes)):
            a, b = sorted(dominoes[i])
            myDict[(a, b)] += 1
        pairs = 0
        for k, v in myDict.items():
            if v >= 2:
                pairs += (v * (v-1)) // 2
        return pairs