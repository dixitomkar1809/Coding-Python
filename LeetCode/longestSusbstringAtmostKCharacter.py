# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

import collections

class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        i = 0
        j = 0
        ans = 0
        sol = ''
        hashmap = collections.OrderedDict()
        while j < len(s):
            char = s[j]
            if char in hashmap:
                del hashmap[char]
            hashmap[char] = j
            j += 1
            if len(hashmap) > k:
                _, index = hashmap.popitem(last = False)
                i = index + 1
            ans = max(ans, j-i)
        return ans