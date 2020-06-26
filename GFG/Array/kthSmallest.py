# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.
'''

# Tiem Complexity: O(n^2) or O(n)

class Solution:
    def kthSmallest(self, arr, k):
        if arr:
            pivot = self.partition(arr, 0, len(arr)-1)
            if k > pivot+1:
                return self.kthSmallest(arr[pivot+1:], k-pivot-1)
            elif k < pivot+1:
                return self.kthSmallest(arr[:pivot], k)
            else:
                return arr[pivot]
    def partition(self, arr, l, r):
        pivot = l
        while l < r:
            if arr[l] < arr[r]:
                arr[l], arr[pivot] = arr[pivot], arr[l]
                pivot+=1
            l+=1
        arr[pivot], arr[r] = arr[r], arr[pivot]
        return pivot

if __name__=='__main__':
    sol = Solution()
    print(sol.kthSmallest([7, 10, 4, 3, 20, 15], 3))
    print(sol.kthSmallest([7, 10, 4, 20, 15], 4))
    
