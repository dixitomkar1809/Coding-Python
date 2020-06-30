# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array arr[] of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. Compute how much water can be trapped in between blocks after raining.
'''

# Time Complexity: O(n)

class Solution:
    def trapRainWater(self, arr):
        if not arr: return 0
        leftMax, rightMax = 0, 0
        left, right = 0, len(arr)-1
        water = 0
        while left < right:
            if arr[left] < arr[right]:
                if arr[left] >= leftMax:
                    leftMax = arr[left]
                else:
                    water += leftMax - arr[left]
                left += 1
            else:
                if arr[right] >= rightMax:
                    rightMax = arr[right]
                else:
                    water += rightMax - arr[right]
                right -= 1
        return water

if __name__=='__main__':
    sol = Solution()
    print(sol.trapRainWater([3,0,0,2,0,4]))
    print(sol.trapRainWater([7, 4, 0, 9]))
    print(sol.trapRainWater([6, 9, 9]))