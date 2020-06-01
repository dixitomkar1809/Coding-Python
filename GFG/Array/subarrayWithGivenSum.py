# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an unsorted array A of size N of non-negative integers, find a continuous sub-array which adds to a given number S.
'''

# Time Complexity = O(n)

class Solution:
    def subarrayWithSum(self, arr, sum):
        if not arr:
            return 0
        i = 0
        j = 1
        currSum = arr[i]
        while j <= len(arr):
            while currSum > sum and i < j-1:
                currSum -= arr[i]
                i+=1
            if currSum == sum:
                return i, j-1
            if j < len(arr):
                currSum += arr[j]
            j+=1
        return 0

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    arr2 = [1, 4, 0, 0, 3, 10, 5]
    arr3 = [1, 4]
    arr4 = [15, 2, 4, 8, 9, 5, 10, 23]
    sol = Solution()
    print(sol.subarrayWithSum(arr4, 23))
