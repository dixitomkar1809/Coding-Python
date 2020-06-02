
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
    def getMedian(self, arr):
        leftSide = MaxHeap(len(arr))
        rightSide = MinHeap(len(arr))
        median = [arr[0]]
        leftSide.add(arr[0])
        for i in range(1, len(arr)):
            x = arr[i]
            if leftSide.size == rightSide.size:
                if x < median[-1]:
                    leftSide.add(x)
                    median.append(leftSide.peek())
                else:
                    rightSide.add(x)
                    median.append(rightSide.peek())
            elif leftSide.size < rightSide.size:
                if x < median[-1]:
                    leftSide.add(x)
                else:
                    leftSide.add(rightSide.remove())
                    rightSide.add(x)
                median.append((leftSide.peek() + rightSide.peek()) / 2)
            else:
                if x < median[-1]:
                    rightSide.add(leftSide.remove())
                    leftSide.add(x)
                else:
                    rightSide.add(x)
                median.append((rightSide.peek() + leftSide.peek()) / 2)
        print(arr)
        print(median)
        return median

if __name__=="__main__":
    arr = [5, 15, 10, 20, 3]
    sol = Solution()
    sol.getMedian(arr)
                