# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a value N, find the number of ways to make change for N cents, if we have infinite supply of each of S = { S1, S2, .. , Sm} valued coins. The order of coins doesn’t matter. For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.
'''

# Time Complexity: O(target * lenOfCoins)

class Solution:
    def coinChange(self, coins, target):
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], target + 1):
                dp[j] += dp[j - coins[i]]
        return dp[-1]

if __name__=='__main__':
    sol = Solution()
    print(sol.coinChange([1, 2, 3], 4))
    print(sol.coinChange([2, 5, 3, 6], 10))