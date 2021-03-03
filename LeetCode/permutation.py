# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/permutations/

# Time Complexity: O() # LOL to do

import collections
import heapq

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.result = []
        self.backtrack(0)
        return self.result
    
    def backtrack(self, start):
        if start == len(self.nums):
            self.result.append(self.nums[:])
        for i in range(start, len(self.nums)):
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]
            self.backtrack(start+1)
            self.nums[start], self.nums[i] = self.nums[i], self.nums[start]