# Author: Omkar Dixit
# Email: omedxt@gmail.com

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

if __name__=="__main__":
    heap = MaxHeap(5)
    array = [4, 2, 10]
    for i,x in enumerate(array):
        heap.pq[i] = x
    heap.size = len(array)
    for i in range(len(array)-1, -1, -1):
        heap.percolateDown(i)
    print(heap.pq)
    heap.add(15)
    print(heap.pq)
    print(heap.size)
    print(heap.remove())
    print(heap.pq)


