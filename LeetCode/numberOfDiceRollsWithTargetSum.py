# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

# Time Complexity: O(d * target)

class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = dp[i][j] + dp[i-1][j-k]
                    k += 1
        return dp[-1][-1] % (1000000007)