# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array having both positive and negative integers. The task is to complete the function maxLen() which returns the length of maximum subarray with 0 sum. The function takes two arguments an array A and n where n is the size of the array A.
'''

# Time Complexity: O(n)

class Solution:
    def maxLen(self, arr):
        maxLen = 0
        summ = 0
        hMap = {}
        for i in range(len(arr)):
            summ += arr[i]
            if arr[i] == 0 and maxLen == 0:
                maxLen = 1
            if summ == 0:
                maxLen = i + 1
            if summ in hMap:
                maxLen = max(maxLen, i - hMap[summ])
            else:
                hMap[summ] = i
        return maxLen

if __name__=='__main__':
    arr = [15, -2, 2, -8, 1, 7, 10, 13] 
    sol = Solution()
    print(sol.maxLen(arr))