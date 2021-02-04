# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/sliding-window-maximum/

# Time Complexity: O(n)

import collections

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        self.deque = collections.deque()
        self.result = []
        self.k = k
        self.nums = nums
        maxIndex = 0
        for i in range(self.k):
            self.cleanDeque(i)
            self.deque.append(i)
            if self.nums[i] > self.nums[maxIndex]:
                maxIndex = i
        self.result.append(self.nums[maxIndex])
        for i in range(k, len(self.nums)):
            self.cleanDeque(i)
            self.deque.append(i)
            self.result.append(self.nums[self.deque[0]])
        return self.result
    
    def cleanDeque(self, i):
        if self.deque and self.deque[0] == i - self.k:
            self.deque.popleft()
        while self.deque and self.nums[i] > self.nums[self.deque[-1]]:
            self.deque.pop()