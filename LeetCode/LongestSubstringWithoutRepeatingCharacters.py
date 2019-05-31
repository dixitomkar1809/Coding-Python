# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        ans = 0
        hmap = {}
        i = 0
        for j in range(n):
            if s[j] in hmap:
                i = max(hmap[s[j]], i)
            ans = max(ans, j-i+1)
            hmap[s[j]] = j+1
        return ans
        