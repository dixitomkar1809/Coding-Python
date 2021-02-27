# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/two-sum-less-than-k/

# Time Complexity: O(n)

import collections
import heapq

class Solution(object):
    def twoSumLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        i = 0
        j = len(nums) - 1
        ans = -1
        while i < j:
            summ = nums[i] + nums[j]
            if summ < k:
                ans = max(ans, summ)
                i += 1
            else:
                j -= 1
        return ans