# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/single-element-in-a-sorted-array/

# Time Complexity: O(logn) n is number of elements in array

import collections
import heapq

class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right-left)//2
            evenDivision = (right - mid) % 2  == 0
            if nums[mid + 1] == nums[mid]:
                if evenDivision:
                    left = mid + 2
                else:
                    right = mid - 1
            elif nums[mid - 1] == nums[mid]:
                if evenDivision:
                    right = mid - 2
                else:
                    left = mid + 1
            else:
                return nums[mid]
        return nums[left]