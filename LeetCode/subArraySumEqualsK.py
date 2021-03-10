# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: O(n) n is number of elements

# Time Complexity: https://leetcode.com/problems/subarray-sum-equals-k/

import collections
import heapq

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum = 0
        cnt = 0
        hashmap = collections.defaultdict(int)
        hashmap[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if (sum-k) in hashmap:
                cnt += hashmap[sum-k]
            hashmap[sum] = hashmap[sum] + 1 if sum in hashmap else 1
        return cnt
        