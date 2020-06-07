# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a sorted array A[](0 based index) and a key "k"  you need to complete the function bin_search to  determine the position of the key if the key is present in the array. If the key is not  present then you have to return -1. The arguments left and right denotes the left most index  and right most index of the array A[]. There are multiple test cases. For each test case, this function will be called individually.
'''

class Solution:
    def binarySearch(self, arr, l, r, x):
        if l > r:
            return -1
        mid = l + (r-l)//2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            return self.binarySearch(arr, mid + 1, r, x)
        else:
            return self.binarySearch(arr, l, mid - 1, x)

if __name__=='__main__':
    arr = [ 2, 3, 4, 10, 40 ] 
    x = 11
    sol = Solution()
    print(sol.binarySearch(arr, 0, len(arr)-1, x))