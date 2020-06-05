# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
'''

# Time Complexity: O(n^2)

class Solution:
    def longestSubstring(self, s):
        sol = ''
        for i in range(len(s)):
            temp = self.helper(s, i, i)
            if len(temp) > len(sol):
                sol = temp
            temp = self.helper(s, i, i+1)
            if len(temp) > len(sol):
                sol = temp
        return sol


    def helper(self, s, left, right):
        l = left
        r = right
        while l >= 0 and r < len(s) and s[l]==s[r]:
            l-=1
            r+=1
        return s[l+1:r]

if __name__=='__main__':
    s = 'abcba'
    s2 = 'babad'
    s3 = 'cbbd'
    sol = Solution()
    print(sol.longestSubstring(s3))