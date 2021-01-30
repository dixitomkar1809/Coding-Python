# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

import collections

def solution(s, k):
    left = 0
    right = 0
    ans = {}
    hashmap = collections.defaultdict()
    while right < len(s):
        char = s[right]
        if char in hashmap:
            del hashmap[char]
        hashmap[char] = right
        if len(hashmap) > k or right - left + 1> k:
            left += 1
        if (len(hashmap) == k and right - left + 1 == k):
            ans[s[left: right+1]]=1
        right += 1
    return list(ans.keys())

if __name__=="__main__":
    print(solution('abcabc', 3))