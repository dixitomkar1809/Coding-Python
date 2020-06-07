# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given 2 sorted arrays A and B of size N each. Print sum of middle elements of the array obtained after merging the given arrays.
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
            print("PQ is Full")
            return False
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

class MaxHeap:
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
            print("PQ is Full")
            return False
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
        while i > 0 and x > self.pq[self.__getParent(i)]:
            self.pq[i] = self.pq[self.__getParent(i)]
            i = self.__getParent(i)
        self.pq[i] = x

    def percolateDown(self, i):
        x = self.pq[i]
        c = self.__getFirstChild(i)
        while c <= self.size - 1:
            if self.pq[c] <= self.pq[c + 1]:
                c = c + 1
            if x > self.pq[c]: break
            self.pq[i] = self.pq[c]
            i = c
            c = self.__getFirstChild(i)
        self.pq[i] = x

    def peek(self):
        return self.pq[0]

class Solution:
    def getSumOfMiddleElements(self, arr1, arr2, n):
        i, j = 0, 0
        k = n
        while k:
            if arr1[i] == arr2[j]:
                i+=1
                j+=1
                k-=1
                k-=1
            elif arr1[i] < arr2[j]:
                i+=1
                k-=1
            else:
                j+=1
                k-=1
        return arr1[i] + arr2[j]

if __name__=='__main__':
    arr1 = [1, 2, 4, 6, 10]
    arr2 = [4, 5, 6, 9, 12]
    sol = Solution()
    print(sol.getSumOfMiddleElements(arr1, arr2, len(arr1)-1))