# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A of positive integers of size N, where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having packet with minimum chocolates is minimum.
'''

# Time Complexity: O(nLogn)

class Solution:
    def choclateDistributionProblem(self, arr, n, m):
        arr.sort()
        i = 0
        minDiff = float('inf')
        while i + m - 1 < n:
            if arr[i + m - 1] - arr[i] < minDiff:
                minDiff = arr[i + m - 1] - arr[i]
            i+=1
        return minDiff

if __name__=='__main__':
    sol = Solution()
    print(sol.choclateDistributionProblem([3, 4, 1, 9, 56, 7, 9, 12], 8, 5))
    print(sol.choclateDistributionProblem([7, 3, 2, 4, 9, 12, 56], 7, 3))