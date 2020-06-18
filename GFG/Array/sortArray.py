# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.
'''

from collections import Counter

class Solution:
    def sortArray(self, arr):
        count = Counter(arr)
        i = 0
        while count[0] > 0:
            arr[i] = 0
            i+=1
            count[0]-=1
        while count[1] > 0:
            arr[i] = 1
            i+=1
            count[1]-=1
        while count[2] > 0:
            arr[i] = 2
            i+=1
            count[2]-=1
        return arr

if __name__=='__main__':
    sol = Solution()
    print(sol.sortArray([0,2,1,2,0]))
    print(sol.sortArray([0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]))
    print(sol.sortArray([0, 1, 0]))