# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1′ into ‘str2′.

Insert
Remove
Replace
All of the above operations are of cost=1.
Both the strings are of lowercase.
'''

# Time Complexity: O(m*n)

class Solution:
    def editDistance(self, str1, str2):
        editDistance = [[0 for x in range(len(str2))] for x in range(len(str1))] 
        for i in range(len(str1)):
            for j in range(len(str2)):
                if i == 0:
                    editDistance[i][j] = j
                elif j == 0:
                    editDistance[i][j] = i
                elif str1[i] == str2[j]:
                    editDistance[i][j] = editDistance[i-1][j-1]
                else:
                    editDistance[i][j] = 1 + min(editDistance[i][j-1], editDistance[i-1][j], editDistance[i-1][j-1])
        return editDistance[-1][-1]

if __name__=='__main__':
    sol = Solution()
    print(sol.editDistance("sunday", "saturday"))
    print(sol.editDistance("geek", "gesek"))