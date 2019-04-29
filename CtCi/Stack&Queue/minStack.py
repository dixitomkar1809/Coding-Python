# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Stack Min: How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.
'''

import sys

class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x):
        self.stack.append(x)
        if not self.minStack or self.minStack[-1] >= x:
            self.minStack.append(x)
        return
    
    def pop(self):
        if not self.stack:
            return None
        x = self.stack.pop()
        if x == self.minStack[-1]:
            self.minStack.pop()
        return x
    
    def getMin(self):
        if not self.minStack:
            return None
        return self.minStack[-1]

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]


if __name__=="__main__":
    ms = minStack()
    ms.push(-2)
    ms.push(0)
    ms.push(-3)
    print(ms.getMin())
    print(ms.pop())
    print(ms.top())
    print(ms.getMin())