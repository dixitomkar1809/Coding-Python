# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
'''

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