# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/product-of-array-except-self/

# Time Complexity: O(n)

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [-1] * len(nums)
        right = [-1] * len(nums)
        left[0] = 1
        right[-1] = 1
        for i in range(1, len(left)):
            left[i] = left[i-1] * nums[i-1]
        for i in range(len(right)-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        print(left, right)
        for i in range(len(right)):
            right[i] *= left[i]
        return right
        