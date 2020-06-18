# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string, find the minimum number of characters to be inserted to convert it to palindrome.
For Example:
ab: Number of insertions required is 1. bab or aba
aa: Number of insertions required is 0. aa
abcd: Number of insertions required is 3. dcbabcd
'''

class Solution:
    def formPalindrome(self, string):
        i = 0
        j = len(string) - 1
        cnt = 0
        while i<j:
            if string[i] == string[j]:
                i+=1
                j-=1
            else:
                if i == 0:
                    string = string[j] + string
                    cnt += 1
                    i+=1
                else:
                    string = string[:i] + string[j] + string[i:]
                    cnt += 1
                    i+=1
            print(string)
        return cnt

if __name__=='__main__':
    sol = Solution()
    print(sol.formPalindrome('geeks'))