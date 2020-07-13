# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a sequence A of size N, find the length of the longest increasing subsequence from a given sequence .
'''

# Time Complexity: O(n^2)

class Solution:
    def longestIncreasingSubsequence(self, arr):
        lis = [1] * len(arr)
        maximum = 1
        for i in range(len(arr)):
            for j in range(i):
                if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
                    if lis[i] > maximum:
                        maximum = lis[i]
        return maximum

if __name__=='__main__':
    sol = Solution()
    print(sol.longestIncreasingSubsequence([10, 22, 9, 33, 21, 50, 41, 60]))
    print(sol.longestIncreasingSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
    print(sol.longestIncreasingSubsequence([5, 8, 3, 7, 9, 1]))


