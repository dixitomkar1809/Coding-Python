# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given weights and values of N items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. Note that we have only one quantity of each item.
'''

# Time Complexity: O(n * W)

class Solution:
    def knapsack(self, W, val, wt):
        knapsackTable = [[0 for _ in range(W+1)] for _ in range(len(val) + 1)]
        for i in range(len(val) + 1):
            for j in range(W+1):
                if j == 0 or i == 0:
                    knapsackTable[i][j] = 0
                elif wt[i-1] <= j:
                    knapsackTable[i][j] = max(val[i-1] + knapsackTable[i-1][j-wt[i-1]], knapsackTable[i-1][j])
                else:
                    knapsackTable[i][j] = knapsackTable[i-1][j]
        return knapsackTable[-1][-1]

if __name__=='__main__':
    sol = Solution()
    print(sol.knapsack(50, [60, 100, 120] , [10, 20, 30] ))
    print(sol.knapsack(4, [1, 2, 3], [4, 5, 1]))
    print(sol.knapsack(3, [1, 2, 3], [4, 5, 6]))