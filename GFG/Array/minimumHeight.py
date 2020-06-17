# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A[ ] denoting heights of N towers and a positive integer K, modify the heights of each tower either by increasing or decreasing them by K only once and then find out the minimum difference of the heights of shortest and longest towers.
'''

# Time Complexity: O(nLogn)

class Solution:
    def minimumHeight(self, arr, k):
        if len(arr) == 1:
            return 0
        arr.sort()
        ans = arr[-1] - arr[0]
        small = arr[0]  + k
        big = arr[-1] - k
        if small > big:
            small, big = big, small
        for i in range(1, len(arr)-1):
            add = arr[i] + k
            substract = arr[i] - k
            if (substract >= small or add <= big):
                continue
            if (big - substract <= add - small):
                small = substract
            else:
                big = add
        return min(ans, big-small)

if __name__=='__main__':
    sol = Solution()
    print(sol.minimumHeight([1,15,10], 6))
    print(sol.minimumHeight([100, 150, 200, 250, 300, 400], 4))
    print(sol.minimumHeight([3, 9, 12, 16, 20], 3))
    print(sol.minimumHeight([1, 5, 8, 10], 2))