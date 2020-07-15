# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A of N positive integers. Find the sum of maximum sum increasing subsequence of the given array.
'''

# Time Complexity: O(n * n)

class Solution:
    def maxIncreasingSumSubsequence(self, arr):
        result = []
        sequence = []
        for i in range(len(arr)):
            result.append(arr[i])
            sequence.append(i)
        maxIndex = 0
        for i in range(len(arr)):
            for j in range(i):
                if arr[j] < arr[i]:
                    if arr[i] + result[j] >= result[i]:
                        result[i] = arr[i] +  result[j]
                        sequence[i] = j
                        if result[maxIndex] <= result[i]:
                            maxIndex = i
        sol = []
        while True:
            sol.append(arr[maxIndex])
            if maxIndex == sequence[maxIndex]:
                break
            maxIndex = sequence[maxIndex]
        return list(reversed(sol))

if __name__=='__main__':
    sol = Solution()
    print(sol.maxIncreasingSumSubsequence([1, 101, 2, 3, 100, 4, 5]))
    print(sol.maxIncreasingSumSubsequence([10, 5, 4, 3]))