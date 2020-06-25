# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
In a candy store there are N different types of candies available  and the prices of all the N different types of candies are provided to you.
You are now provided with an attractive offer.
You can buy a single candy from the store and get atmost K other candies ( all are different types ) for free.
Now you have to answer two questions. Firstly, you have to tell what is the minimum amount of money you have to spend to buy all the N different candies. Secondly, you have to tell what is the maximum amount of money you have to spend to buy all the N different candies.
In both the cases you must utilize the offer i.e. you buy one candy and get K other candies for free.
'''

# Time Complexity: O(nLogn)

class Solution:
    def findMin(self, price, n, k):
        price.sort()
        i = 0
        cost = 0
        while n:
            cost += price[i]
            n -= k
            i += 1
        return cost

    def findMax(self, price, n, k):
        price.sort()
        i = n-1
        index = 0
        cost = 0
        while i >= index:
            cost += price[i]
            index += k
            i -= 1
        return cost

if __name__=='__main__':
    sol = Solution()
    print(sol.findMin([3,2,1,4], 4, 2), sol.findMax([3,2,1,4], 4, 2))