# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Write an efficient program for printing k largest elements in an array. Elements in array can be in any order.
For example, if given array is [1, 23, 12, 9, 30, 2, 50] and you are asked for the largest 3 elements i.e., k = 3 then your program should print 50, 30 and 23.
'''

# Time Complexity = O(nLogn)

class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pq = [float('-inf')] * self.capacity
        self.size = 0

    def __getParent(self, i):
        return int((i-1)/2)
    
    def __getFirstChild(self, i):
        return (2 * i) + 1

    def remove(self):
        x = self.pq[0]
        self.size -= 1
        self.pq = self.pq[self.size]
        self.percolateDown(0)
        return x
    
    # Time Complexity = O(logn)
    def percolateDown(self, i):
        x = self.pq[i]
        c = self.__getFirstChild(i)
        while c <= self.size - 1:
            if c + 1 < self.size and self.pq[c] > self.pq[c + 1]:
                c = c + 1
            if x <= self.pq[c]: break
            self.pq[i] = self.pq[c]
            i = c
            c = self.__getFirstChild(i)
        self.pq[i] = x
    
    def add(self, x):
        if self.size == self.capacity:
            print("PQ is Full")
            return False
        self.pq[self.size] = x
        self.percolateUp(self.size)
        self.size += 1
        return True

    # Time Complexity = O(logn)
    def percolateUp(self, i):
        x = self.pq[i]
        while i > 0 and x < self.pq[self.__getParent(i)]:
            self.pq[i] = self.pq[self.__getParent(i)]
            i = self.__getParent(i)
        self.pq[i] = x