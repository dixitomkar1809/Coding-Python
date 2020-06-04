# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
'''

class Solution:
    def maxSumOfContiguousArrray(self, arr):
        maxSoFar = float('-inf')
        currMax = 0
        start = 0
        end = 0
        s = 0
        for i in range(len(arr)):
            currMax = currMax + arr[i]
            if maxSoFar < currMax:
                maxSoFar = currMax
                start = s
                end = i
            if currMax < 0:
                currMax = 0
                s = i+1
        return maxSoFar, start, end

if __name__=='__main__':
    arr = [1, 2, 3, -2, 5]
    arr2 = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
    arr3 =  [-2, -3, 4, -1, -2, 1, 5, -3] 
    sol = Solution()
    print(sol.maxSumOfContiguousArrray(arr3))