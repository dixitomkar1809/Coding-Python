# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an unsorted array of size N. Find the first element in array such that all of its left elements are smaller and all right elements to it are greater than it.
'''

# Time Complexity: O(n)

class Solution:
    def leftRight(self, arr):
        leftMax = [float('-inf')] * len(arr)
        rightMax = [float('inf')] * len(arr)
        for i in range(1, len(arr)):
            leftMax[i] = max(leftMax[i-1], arr[i-1])
        for i in range(len(arr)-2, -1, -1):
            rightMax[i] = min(rightMax[i+1], arr[i+1])
        for i in range(1, len(arr)-1):
            if leftMax[i] < arr[i] and arr[i] < rightMax[i]:
                return arr[i]
        return -1

if __name__=='__main__':
    sol = Solution()
    print(sol.leftRight([4, 2, 5, 7]))
    print(sol.leftRight([11, 9, 12]))
    print(sol.leftRight([4, 3, 2, 7, 8, 9]))
    print(sol.leftRight([5, 1, 4, 3, 6, 8, 10, 7, 9]))