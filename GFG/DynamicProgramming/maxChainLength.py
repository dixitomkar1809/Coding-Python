# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given N pairs of numbers. In every pair, the first number is always smaller than the second number. A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. Your task is to complete the function maxChainLen which returns an integer denoting the longest chain which can be formed from a given set of pairs. 
'''

# Time Complexity: O(n^2)

class Solution:
    def maxChainLength(self, arr):
        maxChainLength = [1] * len(arr)
        mcl = 0
        arr.sort(key=lambda x: x[0])
        for i in range(1, len(arr)):
            for j in range(0, i):
                if arr[i][0] > arr[j][1] and maxChainLength[i] <  maxChainLength[j] + 1:
                    maxChainLength[i] = maxChainLength[j] + 1
        for i in range(len(arr)):
            if mcl < maxChainLength[i]:
                mcl = maxChainLength[i]
        return mcl

if __name__=='__main__':
    sol = Solution()
    print(sol.maxChainLength([(5, 24), (15, 25), (27, 40), (50, 60)]))
    print(sol.maxChainLength([(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)]))
    print(sol.maxChainLength([(5, 10), (1, 11)]))