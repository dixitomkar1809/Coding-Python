# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given a number N. You have to find the number of operations required to reach N from 0. You have 2 operations available:

Double the number
Add one to the number
'''

class Solution:
    def minimumOperations(self, n):
        count = 0
        if n <=2:
            return 1 
        while n:
            if n % 2 == 0:
                count += 1
                n = n/2    
            else:
                count += 1
                n -= 1
        return count

if __name__=='__main__':
    sol = Solution()
    print(sol.minimumOperations(8))
    print(sol.minimumOperations(7))