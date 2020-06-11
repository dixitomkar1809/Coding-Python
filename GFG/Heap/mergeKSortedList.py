# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given K sorted linked lists of different sizes. The task is to merge them in such a way that after merging they will be a single sorted linked list.
'''

# Time Complexity: O(n * k * logk)

class MinHeapNode:
    def __init__(self, value, arrI, nextI):
        self.value = value
        self.arrI = arrI
        self.nextI = nextI

class MinHeap:
    def __init__(self, arr, k):
        self.pq = arr
        self.size = k
        i = (self.size - 1)//2
        while i >= 0:
            self.heapify(i)
            i-=1
    
    def getLeftChild(self, i):
        return (2 * i) + 1
    
    def getRightChild(self, i):
        return (2 * i) + 2

    def heapify(self, i):
        left = self.getLeftChild(i)
        right = self.getRightChild(i)
        smallest = i
        if left < self.size and self.pq[left].value < self.pq[smallest].value:
            smallest = left
        if right < self.size and self.pq[right].value < self.pq[smallest].value:
            smallest = right
        if smallest != i:
            self.pq[smallest], self.pq[i] = self.pq[i], self.pq[smallest]
            self.heapify(smallest)
    
if __name__=="__main__":
    arr = [
        [2, 6, 34],
        [1, 9, 20, 1000],
        [23, 34, 90]
    ]
    k = 3
    pq = []
    size = 0
    for i in range(len(arr)):
        minHeapNode = MinHeapNode(arr[i][0], i, 1)
        pq.append(minHeapNode)
        size += len(arr[i])
    minHeap = MinHeap(pq, k)
    result = []
    for i in range(size):
        smallestNode = minHeap.pq[0]
        result.append(smallestNode.value)
        if smallestNode.nextI < len(arr[smallestNode.arrI]):
            smallestNode.value = arr[smallestNode.arrI][smallestNode.nextI]
            smallestNode.nextI += 1
        else:
            smallestNode.value = float('inf')
        minHeap.heapify(0)
    print(result)
