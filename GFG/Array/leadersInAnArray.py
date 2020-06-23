# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. Also, the rightmost element is always a leader. 
'''

class Solution:
    def leadersInAnArray(self, arr):
        currMax = float('-inf')
        res = []
        for i in range(len(arr)-1, -1, -1):
            if arr[i] >=  currMax:
                currMax = arr[i]
                res.append(arr[i])
        return res[::-1]

if __name__=='__main__':
    sol = Solution()
    arr = [16,17,4,3,5,2]
    print(sol.leadersInAnArray(arr))