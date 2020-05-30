# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
The stock span problem is a financial problem where we have a series of n daily price quotes for a stock and we need to calculate span of stock’s price for all n days.
The span Si of the stock’s price on a given day i is defined as the maximum number of consecutive days just before the given day, for which the price of the stock on the current day is less than or equal to its price on the given day.
For example, if an array of 7 days prices is given as {100, 80, 60, 70, 60, 75, 85}, then the span values for corresponding 7 days are {1, 1, 1, 2, 1, 4, 6}
'''

class Solution:
    def stockSpan(self, price):
        span = [1] * len(price)
        for i in range(len(price)):
            j =  i - 1
            while j >= 0 and price[i] >= price[j]:
                span[i] += 1
                j-=1
        return span

    def stockSpan2(self, price):
        stack = [0]
        span = [1]  * len(price)
        for i in range(len(price)):
            while len(stack) > 0 and price[i] >= price[stack[-1]]:
                stack.pop()
            span[i] = i + 1 if len(stack) <= 0 else (i - stack[-1])
            stack.append(i)
        return span

if __name__=="__main__":
    price = [100, 80, 60, 70, 60, 75, 85]
    sol = Solution()
    print(sol.stockSpan(price))
    print(sol.stockSpan2(price))