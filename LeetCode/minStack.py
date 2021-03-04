# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/min-stack/

# Time Complexity: O(1)

import collections
import heapq

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if x < self.minStack[-1]:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])
        return

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()