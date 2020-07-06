# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string S consisting only '0's and '1's,  print the last index of the '1' present in it.
'''

# Time Complexity: O(n)

class Solution:
    def lastOne(self, string):
        index = -1
        for i, char in enumerate(string):
            if char == '1':
                index = i
        return index

if __name__=='__main__':
    sol = Solution()
    print(sol.lastOne('00001'))
    print(sol.lastOne('0'))