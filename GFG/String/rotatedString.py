# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two strings a and b. The task is to find if a string 'a' can be obtained by rotating another string 'b' by 2 places.
'''

class Solution:
    def rotatedStringByTwo(self, string, rotatedString):
        return (string[2:] + string[:2] == rotatedString)

if __name__=='__main__':
    string = 'geeksforgeeks'
    rotatedString = 'geeksgeeksfor'
    sol = Solution()
    print(sol.rotatedStringByTwo(string, rotatedString))
