# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
'''

# Time Complexity: O(n)

class Solution:
    def reverseStringWithWords(self, str):
        return self.reverseStringHelper(str.strip().split('.'))

    def reverseStringHelper(self, str):
        if not str:
            return str
        i = 0
        j = len(str) - 1
        while i < j:
            str[i], str[j] = str[j], str[i]
            i += 1
            j -= 1
        return '.'.join(str)

if __name__=="__main__":
    sol = Solution()
    print(sol.reverseStringWithWords('i.like.this.program.very.much'))