# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/moving-average-from-data-stream/

# Time Complexity: O(1)

import collections

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.windowSize = size
        self.queue = collections.deque()
        self.sum = 0.0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.queue) == self.windowSize:
            self.sum -= self.queue.popleft()
        self.queue.append(val)
        self.sum += val
        return self.sum / len(self.queue)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)