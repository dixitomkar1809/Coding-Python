# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a array of N strings, find the longest common prefix among all strings present in the array.
'''

# Time Complexity: O(sumOfAllChars)

class Solution:
    def longestPrefix(self, strArray):
        if not strArray:
            return None
        if len(strArray) == 1:
            return strArray[0]
        prefix = strArray[0]
        i = 0
        while i < len(strArray):
            while strArray[i][:len(prefix)] != prefix:
                prefix = prefix[:len(prefix)-1]
            i+=1
        return prefix

if __name__=='__main__':
    sol = Solution()
    print(sol.longestPrefix(['geeksforgeeks', 'geeks', 'geeks', 'geezer']))
    print(sol.longestPrefix(['apple', 'ape', 'april']))
