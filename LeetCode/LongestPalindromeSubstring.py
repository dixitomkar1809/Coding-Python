# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/longest-palindromic-substring/

# Time Complexity: O(n ^ 2)

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        sol = ""
        for i in range(len(s)):
            temp = self.longestPalindrome1(s, i, i)
            if len(sol) < len(temp):
                sol = temp
            temp = self.longestPalindrome1(s, i, i+1)
            if len(sol) < len(temp):
                sol = temp
        return sol
    
    def longestPalindrome1(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l-=1
            r+=1
        return s[l+1:r]