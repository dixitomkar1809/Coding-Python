# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
There are N piles of coins each containing  Ai (1<=i<=N) coins.  Now, you have to adjust the number of coins in each pile such that for any two pile, if a be the number of coins in first pile and b is the number of coins in second pile then |a-b|<=K. In order to do that you can remove coins from different piles to decrease the number of coins in those piles but you cannot increase the number of coins in a pile by adding more coins. Now, given a value of N and K, along with the sizes of the N different piles you have to tell the minimum number of coins to be removed in order to satisfy the given condition.
'''

class Solution:
    def coinPiles(self, pileArr, k):
        minValue = min(pileArr)
        count = 0
        for i in range(len(pileArr)):
            diff = pileArr[i] - minValue
            if diff > k:
                count += (diff - k)
        return count

if __name__=='__main__':
    pileArr = [2,2,2,2]
    k = 0
    sol = Solution()
    print(sol.coinPiles(pileArr, k))