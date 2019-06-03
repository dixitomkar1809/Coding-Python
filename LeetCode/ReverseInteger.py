# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isNegative = False
        res = 0
        if x < 0:
            isNegative = True
            x = x * (-1)
        while(x > 0):
            res = 10 * res + x % 10
            x = x//10
        print(res)
        if isNegative:
            if (-1 * res) < (-2 ** 31):
                return 0
            return (-1 * res)
        else:
            if res > (2**31 - 1):
                return 0
            return res
        