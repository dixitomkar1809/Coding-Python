# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to problem: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target-num], i]
            else:
                seen[num] = i
