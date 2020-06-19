# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A and an integer K. Find the maximum for each and every contiguous subarray of size K.
'''

# Time Complexity: O(n)

class Solution:
    def maxOIfSubarrayK(self, arr, k):
        if len(arr) < k:
            return []
        result = []
        maxVal = float('-inf')
        j = 0
        for i in range(k):
            if arr[i] > maxVal:
                maxVal = arr[i]
            j += 1
        i = 1
        result.append(maxVal)
        while j < len(arr):
            if arr[j] > maxVal:
                maxVal = arr[j]
            result.append(maxVal)
            i += 1
            j += 1
        return result

    

if __name__=='__main__':
    sol = Solution()
    arr = [1,2,3,1,4,5,2,3,6]
    k = 3
    print(sol.maxOIfSubarrayK(arr, k))
    arr = [8,5,10,7,9,4,15,12,90,13]
    k = 4
    print(sol.maxOIfSubarrayK(arr, k))