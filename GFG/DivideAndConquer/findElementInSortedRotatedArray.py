# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a sorted array A, size N, of integers; every element appears twice except for one. Find that element that appears once in array.
'''
#Time Complexity: O(logn)
class Solution:
    def findElementInSortedRotatedArray(self, arr, l, r):
        if l > r:
            return None
        if l == r:
            return arr[l]
        mid = l + (r-l)//2    
        if mid % 2 == 0:
            if arr[mid] == arr[mid + 1]:
                return self.findElementInSortedArray(arr, mid + 2, r)
            else:
                return self.findElementInSortedArray(arr, l, mid)
        else:
            if arr[mid] == arr[mid-1]:
                return self.findElementInSortedArray(arr, mid + 1, r)
            else:
                return self.findElementInSortedArray(arr, l, mid-1)
    

if __name__=='__main__':
    arr = [1,1,4,4,5,5,6]
    sol = Solution()
    print(sol.findElementInSortedRotatedArray(arr, 0, len(arr)-1))
