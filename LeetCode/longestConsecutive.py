# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/longest-consecutive-sequence/

class Solution(object):
    def longestConsecutive(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashMap = {}
        ans = 0
        for item in arr:
            hashMap[item] = 0
        for i in range(len(arr)):
            if arr[i] - 1 not in hashMap:
                j = arr[i]
                while j in hashMap:
                    j += 1
                ans = max(ans, j - arr[i])
        return ans
