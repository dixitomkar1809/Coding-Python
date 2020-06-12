# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of integers. Complete the partition() function used for the implementation of Quick Sort.
'''

class Solution:
    def quickSort(self, arr):
        self._quickSort(arr, 0, len(arr)-1)
        return arr
    
    def _quickSort(self, arr, l, r):
        if l < r:
            p = self.partition(arr, l, r)
            self._quickSort(arr, l, p-1)
            self._quickSort(arr, p+1, r)
    
    def partition(self, arr, l, r):
        pivot = arr[r]
        leftWall = l
        for i in range(l+1, r+1):
            if pivot > arr[i]:
                arr[i], arr[leftWall] = arr[leftWall], arr[i]
                leftWall += 1
        arr[r], arr[leftWall] = arr[leftWall], arr[r]
        return leftWall

if __name__=='__main__':
    arr = [10, 7, 8, 9, 1, 5]
    sol = Solution()
    print(sol.quickSort(arr))




