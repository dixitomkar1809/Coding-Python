# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/merge-sorted-array/

# Time Complexity: O(m + n) m, n are number of elements in array

import collections
import heapq

class Solution(object):
    def merge(self, arr1, m, arr2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        arr1copy = arr1[:m]
        i = 0
        j = 0
        for p in range(m + n):
            if j >= n or (i < m and arr1copy[i] <= arr2[j]):
                arr1[p] = arr1copy[i]
                i += 1
            else:
                arr1[p] = arr2[j]
                j += 1
        
        