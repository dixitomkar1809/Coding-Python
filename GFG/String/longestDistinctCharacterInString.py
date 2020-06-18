# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
'''

# Time Complexity: O(n)

class Solution:
    def longestDistinctCharacterInString(self, string):
        lastIndex = [-1] * 256
        i = 0
        res = 0
        for j in range(len(string)):
            i = max(i, lastIndex[ord(string[j])] + 1)
            res = max(res, j-i+1)
            lastIndex[ord(string[j])] = j
        return res

if __name__=='__main__':
    sol = Solution()
    print(sol.longestDistinctCharacterInString('geeks'))
    print(sol.longestDistinctCharacterInString('abababcdefababcdab'))
    print(sol.longestDistinctCharacterInString('geeksforgeeks'))