# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.
'''

# Time Complexity: O(n)

class Solution:
    def stockBuySell(self, price):
        i = 0
        n = len(price)
        sol = []
        while i < (n-1):
            while i < (n-1) and price[i+1] <= price[i]:
                i+=1
            if i == (n-1):
                break
            buy = i
            i += 1
            while i < (n) and price[i] >= price[i-1]:
                i += 1
            sell = i-1
            sol.append((buy, sell))
        return sol

if __name__=='__main__':
    sol = Solution()
    print(sol.stockBuySell([100, 180, 260, 310, 40, 535, 695]))