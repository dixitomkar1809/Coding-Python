# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array arr[] of positive integers of size N. Reverse every sub-array of K group elements.
'''

# Time Complexity: O(n)

class Solution:
    def reverseKGroup(self, arr, k):
        for i in range(0, len(arr), k):
            if k+i > len(arr):
                arr = self.reverse(arr, i, len(arr)-1)
            else:
                arr = self.reverse(arr, i, k+i-1)
        return arr
    def reverse(self, arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l+=1
            r-=1
        return arr

if __name__=='__main__':
    sol = Solution()
    print(sol.reverseKGroup([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
    print(sol.reverseKGroup([10, 20, 30, 40, 50, 60], 2))