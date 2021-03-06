# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a value N, total sum you have. You have to make change for Rs. N, and there is infinite supply of each of the denominations in Indian currency, i.e., you have infinite supply of { 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000} valued coins/notes, Find the minimum number of coins and/or notes needed to make the change for Rs N.
'''

# Time Complexity: O(coins * target)
# Time Complexity: O(nLogn)

class Solution:
    def minCoins(self, coins, target):
        targetTable = [0] * (target + 1)
        targetTable[0] = 0
        for i in range(1, target + 1):
            targetTable[i] = float('inf')
        for i in range(1, target + 1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    temp = targetTable[i - coins[j]]
                    if temp != float('inf') and temp + 1 < targetTable[i]:
                        targetTable[i] = temp + 1
        return targetTable[target]

    def minCoins2(self, coins, target):
        ans = []
        i = len(coins) - 1
        while i >= 0:
            while target >= coins[i]:
                target-=coins[i]
                ans.append(coins[i])
            i -= 1
        return ans

if __name__=='__main__':
    sol = Solution()
    print(sol.minCoins([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], 43))
    print(sol.minCoins2([1, 2, 5, 10, 20, 50, 100, 200, 500, 2000], 43))
    print(sol.minCoins([1,5,6,9], 11))
    print(sol.minCoins2([1,5,6,9], 11))