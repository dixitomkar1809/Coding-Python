# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/132-pattern/

# Time Complexity: O(n)

import collections
import heapq

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        minArray = [-1] * len(nums)
        minArray[0] = nums[0]
        for i in range(1, len(nums)):
            minArray[i] = min(minArray[i-1], nums[i])
        for j in range(len(nums)-1, -1, -1):
            if not (nums[j] <= minArray[j]):
                while stack and stack[-1] <= minArray[j]:
                    stack.pop()
                if stack and stack[-1] < nums[j]:
                    return True
                stack.append(nums[j])
        return False