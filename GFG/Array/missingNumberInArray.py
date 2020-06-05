# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
'''

# Time Complexity: O(n)

class Solution:
    def getMissingNumberInArray(self, arr, n):
        currSum = sum(arr)
        total = (n * (n+1))/2
        return total - currSum


if __name__=='__main__':
    arr = [1,2,3,4,5]
    n = 6
    sol = Solution()
    print(sol.getMissingNumberInArray(arr, n))