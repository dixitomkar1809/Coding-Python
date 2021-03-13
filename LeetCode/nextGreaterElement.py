# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/next-greater-element-i/

# Time Complexity: O(m+n) m , n is number of elements in nums1 and nums2

import collections
import heapq

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        greaterElementMap = {}
        for num in nums2:
            while stack and num > stack[-1]:
                greaterElementMap[stack.pop()] =  num
            stack.append(num)
        while stack:
            greaterElementMap[stack.pop()] = -1
        return [greaterElementMap[item] for item in nums1]