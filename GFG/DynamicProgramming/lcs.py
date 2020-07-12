# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two strings X and Y. The task is to find the length of the longest common substring.
'''

# Time Complexity: O(n*m)

class Solution:
    def longestCommonSubstring(self, str1, str2):
        lcsTable = [[0 for _ in range(len(str2)+1)] for _ in range(len(str1)+1) ] 
        result = 0 
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i == 0 or j == 0:
                    lcsTable[i][j] = 0
                elif str1[i-1] == str2[j-1]:
                    lcsTable[i][j] = lcsTable[i-1][j-1] + 1
                    result = max(result, lcsTable[i][j])
                else:
                    lcsTable[i][j] = 0
        return result

if __name__=='__main__':
    sol = Solution()
    print(sol.longestCommonSubstring('ABCDGH', 'ACDGHR'))
    print(sol.longestCommonSubstring('ABC', 'AC'))