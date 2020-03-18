# Author: Omkar Dixit
# Email: omedxt@gmail.com

"""
"""



class KStackArray:
    """
    k is number of stacks the array contains
    n is size of the array
    free is the top of free stakc
    top tracks the top of each stack
    next is the next of k stakc or free stack
    arr is the actual array that has the stacks
    """
    def __init__(self, k, n): 
        self.k = k
        self.n = n
        self.free = 0
        self.top = [-1] * k
        self.next = [i+1 for i in range(n)]
        self.next[n-1] = -1
        self.arr = [0] * n

    def isEmpty(self, stackNumber):
        return self.top[stackNumber] == -1

    def isFull(self):
        return self.free == -1
    
    def push(self, stackNumber, value):
        if self.isFull(): return False
        location = self.free
        self.free = self.next[location]
        self.arr[location] = value
        self.next[location] = self.top[stackNumber]
        self.top[stackNumber] = location
        return True

    def pop(self, stackNumber):
        if self.isEmpty(stackNumber): return None
        stackTop = self.top[stackNumber]
        self.top[stackNumber] = self.next[self.top[stackNumber]]
        self.next[stackTop] = self.free
        self.free = stackTop
        return self.arr[stackTop]

if __name__=="__main__":
    kStack = KStackArray(3, 9)