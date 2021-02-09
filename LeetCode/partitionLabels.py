# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/partition-labels/

# Time Complexity: O(n)

import collections
class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lastIndex = collections.defaultdict(int)
        for i, char in enumerate(S):
            lastIndex[char] = i
        sol = []
        partitionIndex = j = 0
        for i, char in enumerate(S):
            j = max(j, lastIndex[char])
            if i == j:
                sol.append(i - partitionIndex + 1)
                partitionIndex = i + 1
        return sol
        