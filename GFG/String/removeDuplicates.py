# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string, the task is to remove duplicates from it. Expected time complexity O(n) where n is length of input string and extra space O(1) under the assumption that there are total 256 possible characters in a string.
'''

class Solution:
    def removeDuplicates(self, string):
        chars = [0] * 256
        output = ''
        for char in string:
            if chars[ord(char)] == 0:
                chars[ord(char)] += 1
                output+=char
        return output


if __name__=='__main__':
    string = 'geeks for geeks'
    sol = Solution()
    print(sol.removeDuplicates(string))