# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.
'''

class Solution:
    def atoi(self, string):
        string = string.strip()
        result = 0
        for i in range(len(string)):
            result = result * 10 + (ord(string[i]) - ord('0'))
        return result, type(result)


if __name__=='__main__':
    sol = Solution()
    print(sol.atoi('123'))