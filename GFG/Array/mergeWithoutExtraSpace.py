# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two sorted arrays arr1[] and arr2[] in non-decreasing order with size n and m. The task is to merge the two sorted arrays into one sorted array (in non-decreasing order).
'''

class Solution:
    def mergeSortedArrayWithoutSpace(self, arr1, arr2):
        for i in range(len(arr2)-1, -1, -1):
            last = arr1[-1]
            j = len(arr1) - 2 # -1 would be last element, we need the one before that 
            while j >= 0 and arr1[j] >= arr2[i]:
                arr1[j+1] = arr1[j]
                j-=1
            if j != len(arr1) - 2 or last > arr2[i]:
                arr1[j+1] = arr2[i]
                arr2[i] = last
        return arr1, arr2

if __name__=='__main__':
    arr1 = [1, 5, 9, 10, 15, 20] 
    arr2 = [2, 3, 8, 13]
    sol = Solution()
    print(sol.mergeSortedArrayWithoutSpace(arr1, arr2))