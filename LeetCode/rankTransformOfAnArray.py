# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/rank-transform-of-an-array/

# Time Complexity: O(nLogn)

class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        ranks = {}
        for k, v in enumerate(list(sorted(set(arr)))):
            ranks[v] = k
        for i in range(len(arr)):
            arr[i] = ranks[arr[i]] + 1
        return arr