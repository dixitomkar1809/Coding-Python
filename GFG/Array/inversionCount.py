# Author: Omkar Dixit
# Email: omedxt@gmail.com   

'''
Given an array of positive integers. The task is to find inversion count of array.
'''

class Solution:
    def getInversionCount(self, arr):
        tempArr = [0] * len(arr)
        return self._mergeSort(arr, tempArr, 0, len(arr)-1)
    
    def _mergeSort(self, arr, tempArr, l, r):
        inversionCount = 0
        if l<r:
            mid = (l+r)//2
            inversionCount += self._mergeSort(arr, tempArr, l, mid)
            inversionCount += self._mergeSort(arr, tempArr, mid+1, r)
            inversionCount += self._merge(arr, tempArr, l, mid, r)
        return inversionCount

    def _merge(self, arr, tempArr, l, mid, r):
        i = l
        j = mid + 1
        k = l
        inversionCount = 0
        while i <= mid and j<=r:
            if arr[i] < arr[j]:
                tempArr[k] = arr[i]
                i += 1
                k += 1
            else:
                tempArr[k] = arr[j]
                inversionCount += (mid - i + 1)
                j += 1
                k += 1
        while i <= mid:
            tempArr[k] = arr[i]
            i += 1
            k += 1
        while j<=r:
            tempArr[k] = arr[j]
            j += 1
            k += 1
        arr[l:r+1] = tempArr[l:r+1]
        return inversionCount



if __name__=='__main__':
    arr = [2,4,1,3,5]
    arr = [1, 20, 6, 4, 5] 
    sol = Solution()
    print(sol.getInversionCount(arr))