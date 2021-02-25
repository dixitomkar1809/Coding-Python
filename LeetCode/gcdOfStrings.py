# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/greatest-common-divisor-of-strings/

# Time Complexity: O(N) N is longest string

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        str1len = len(str1)
        str2len = len(str2)
        if str1len < str2len:
                return self.gcdOfStrings(str2, str1)
        if str1[:str2len] == str2:
            if str1len == str2len:
                return str2
            return self.gcdOfStrings(str2, str1[str2len:])
        return ''