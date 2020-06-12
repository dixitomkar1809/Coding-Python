# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are anagram of each other.
'''
from collections import Counter
class Solution:
    def getAnagram(self, s1, s2):
        return Counter(s1) == Counter(s2)

if __name__=='__main__':
    s1 = 'geeksforgeeks'
    s2 = 'forgeeksgeeks'
    s3 = 'allergy'
    s4 = 'allergic'
    sol = Solution()
    print(sol.getAnagram(s3, s4))