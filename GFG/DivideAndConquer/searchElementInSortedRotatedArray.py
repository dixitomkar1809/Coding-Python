# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. The task is to find the index of the given element K in the array A.
'''

class Solution:
    def searchElementInSortedRotatedArray(self, arr, l, r, x):
        if l > r:
            return None
        mid = (l+r)//2
        if arr[mid] == x:
            return mid
        if arr[l] <= arr[mid]:
            if x >= arr[l] and x <= arr[mid]:
                return self.searchElementInSortedRotatedArray(arr, l, mid-1, x)
            else:
                return self.searchElementInSortedRotatedArray(arr, mid+1, r, x)
        else:
            if x >= arr[mid] and x <= arr[r]:
                return self.searchElementInSortedRotatedArray(arr, mid+1, r, x)
            else:
                return self.searchElementInSortedRotatedArray(arr, l, mid-1, x)

if __name__=='__main__':
    arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]     
    sol = Solution()
    print(sol.searchElementInSortedRotatedArray(arr, 0, len(arr)-1, 1))

