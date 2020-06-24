# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Your task is to implement the function strstr. The function takes two strings as arguments (s,x) and  locates the occurrence of the string x in the string s. The function returns and integer denoting the first occurrence of the string x in s (0 based indexing).
'''

class Solution:
    def strStr(self, string, pattern):
        if len(pattern) > len(string):
            return -1
        patternLength = len(pattern)
        stringLength = len(string)
        j = 0
        for i in range(stringLength - patternLength + 1):
            j = 0
            while j < patternLength:
                if string[i+j] != pattern[j]:
                    break
                if j + 1 == patternLength:
                    return i
                j += 1
        return -1
        
if __name__=='__main__':
    sol = Solution()
    print(sol.strStr('hello', 'll'))
    print(sol.strStr('GeeksForGeeks', 'Fr'))
    print(sol.strStr('GeeksForGeeks', 'For'))
