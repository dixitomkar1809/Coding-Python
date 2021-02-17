# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/

class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if len(jobDifficulty) < d:
            return -1
        dp = [[0] * len(jobDifficulty)] + [[float('inf')] * len(jobDifficulty) for _ in range(d - 1)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[0][i] = max(dp[0][i-1], jobDifficulty[i])
        for i in range(1, d):
            for j in range(i, len(jobDifficulty)):
                max_r = jobDifficulty[j]
                for r in range(j, i-1, -1):
                    max_r = max(max_r, jobDifficulty[r])
                    dp[i][j] = min(dp[i][j], max_r + dp[i-1][r-1])
        return dp[-1][-1]
        