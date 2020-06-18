# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array. Equilibrium position in an array is a position such that the sum of elements before it is equal to the sum of elements after it.
'''

#Time Complexity: O(n)

class Solution:
    def equilibriumPoint(self, arr):
        totalSum = sum(arr)
        leftSum = 0
        for i in range(1, len(arr)):
            leftSum += arr[i-1]
            if totalSum - arr[i] - leftSum == leftSum:
                return i
        return 1

if __name__=='__main__':
    sol = Solution()
    print(sol.equilibriumPoint([16,3,5,2,9]))