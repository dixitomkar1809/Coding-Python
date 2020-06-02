# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of size N. The task is to sort the array elements by completing functions heapify() and buildHeap() which are used to implement Heap Sort.
'''

class Solution:

    def heapify(self, arr, i, size):
        largest = i
        left = (2*i) + 1
        right = (2*i) + 2
        if left < size and arr[i] < arr[left]:
            largest = left
        if right < size and arr[largest] < arr[right]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, largest, size)

    def buildHeap(self, arr):
        n = len(arr)
        for i in range((n//2)-1, -1, -1):
            self.heapify(arr, i, n)
        for i in range(n-1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, 0, i)

if __name__=="__main__":
    arr = [12, 11, 13, 5, 6, 7]
    arr2 = [4, 1, 3, 9, 7]
    arr3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sol = Solution()
    sol.buildHeap(arr3)
    
    
