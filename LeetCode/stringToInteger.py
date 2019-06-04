# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        intMin = -2 ** 31
        intMax = 2 ** 31 - 1
        if not s or s.isspace():
            return 0
        
        s = s.strip()
        # print(s)
        
        if not (s[0].isdigit() or s[0] in {'+', '-'}):
            return 0
        
        sign = 1
        if s[0] == "+":
            s = s[1:]
        elif s[0] == "-":
            s = s[1:]
            sign = -1
        
        integer = 0
        for i in range(len(s)):
            if s[i].isdigit():
                print(s[i])
                print(ord(s[i]), ord('0'))
                digit = ord(s[i]) - ord('0')
                # print(digit)
                integer = integer * 10 + digit
            else:
                break
        
        integer*=sign
        
        # print(integer)
        
        if integer < intMin:
            integer = intMin
        elif integer > intMax:
            integer = intMax
        
        return integer
        