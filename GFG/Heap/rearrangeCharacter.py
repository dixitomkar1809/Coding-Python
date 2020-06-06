# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string S with repeated characters (only lowercase). The task is to rearrange characters in a string such that no two adjacent characters are same.
'''

from heapq import heapify, heappop, heappush, nlargest
from collections import Counter

class Solution:
    def rearrangeCharacters(self, string):
        pq = []
        stringCntr = Counter(string)
        for k in stringCntr:
            heappush(pq, (stringCntr[k] * -1, k))
        output = ''
        prev = (1, '#')
        while pq:
            freq, char = heappop(pq)
            output += char
            if prev[0] < 0:
                heappush(pq, prev)
            freq += 1
            prev = (freq, char)
        if len(output) == len(string):
            return 1
        return 0

if __name__=='__main__':
    string = 'geeksforgeeks'
    sol = Solution()
    print(sol.rearrangeCharacters(string))