# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/find-median-from-data-stream/

# Time Complexity: O(logn)

import heapq

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.leftSide = [] # Max Heap
        self.rightSide = [] # Min Heap
        
    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heapq.heappush(self.leftSide, -num)
        heapq.heappush(self.rightSide, -heapq.heappop(self.leftSide))
        if len(self.leftSide) < len(self.rightSide):
            heapq.heappush(self.leftSide, -heapq.heappop(self.rightSide))

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.leftSide) == len(self.rightSide):
            return (-self.leftSide[0] + self.rightSide[0]) / 2.0
        else:
            return -self.leftSide[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()