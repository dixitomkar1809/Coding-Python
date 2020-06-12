# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
The task is to complete merge() function which is used to implement Merge Sort.
'''

class Solution:
    def mergeSort(self, arr):
        self._mergeSort(arr, 0, len(arr)-1)
        return arr

    def _mergeSort(self, arr, l, r):
        if l < r:
            m = int((l+r)/2)
            self._mergeSort(arr, l, m)
            self._mergeSort(arr, m+1, r)
            self._merge(arr, l, m, r)
    
    def _merge(self, arr, l, m, r):
        L = arr[l:m+1]
        R = arr[m+1:r+1]
        i, j = 0, 0
        for k in range(l, r+1):
            if j>=len(R) or (i < len(L) and L[i] <= R[j]):
                arr[k] = L[i]
                i+=1
            else:
                arr[k] = R[j]
                j+=1

if __name__=='__main__':
    arr = [10, 7, 8, 9, 1, 5]
    sol = Solution()
    print(sol.mergeSort(arr))
