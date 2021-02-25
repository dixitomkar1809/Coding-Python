# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

# Time Complexity: O(n * c) n is words, c is max chars in a word

import copy

class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        hashMap = {}
        for char in chars:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1
        sol = 0
        for word in words:
            tempMap = copy.deepcopy(hashMap)
            goodWord = True
            for char in word:
                if char in tempMap and tempMap[char] > 0:
                    tempMap[char] -= 1
                else:
                    goodWord = False
            if goodWord:
                sol += len(word)
        return sol