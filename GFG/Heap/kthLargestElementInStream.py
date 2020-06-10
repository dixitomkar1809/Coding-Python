# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an input stream of n integers, find the kth largest element for each element in the stream.
'''

class MinHeap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pq = [float('-inf')] * self.capacity
        self.size = 0

    def __getParent(self, i):
        return int((i - 1) / 2)

    def __getFirstChild(self, i):
        return 2 * i + 1

    def add(self, x):
        if self.size == self.capacity:
            currentKth = self.peek()
            if x > currentKth:
                self.remove()
            else:
                return True
        self.pq[self.size] = x
        self.percolateUp(self.size)
        self.size += 1
        return True

    def remove(self):
        x = self.pq[0]
        self.size -= 1
        self.pq[0] = self.pq[self.size]
        self.percolateDown(0)
        return x

    def percolateUp(self, i):
        x = self.pq[i]
        while i > 0 and x < self.pq[self.__getParent(i)]:
            self.pq[i] = self.pq[self.__getParent(i)]
            i = self.__getParent(i)
        self.pq[i] = x

    def percolateDown(self, i):
        x = self.pq[i]
        c = self.__getFirstChild(i)
        while c <= self.size - 1:
            if self.pq[c] >= self.pq[c + 1]:
                c = c + 1
            if x <= self.pq[c]: break
            self.pq[i] = self.pq[c]
            i = c
            c = self.__getFirstChild(i)
        self.pq[i] = x

    def peek(self):
        return self.pq[0]

    def printHeap(self):
        for i in range(self.size):
            print(self.pq[i])

if __name__=='__main__':
    k = 3
    minHeap = MinHeap(k)
    x=''
    while True:
        x = input('Enter Element:')
        if x == 'exit':
            break
        if x == '':
            continue
        x= int(x)
        minHeap.add(x)
        print('Current Kth largest', minHeap.peek())
        print('Current Heap', minHeap.pq)