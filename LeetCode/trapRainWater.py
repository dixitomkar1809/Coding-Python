# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/trapping-rain-water/

# Time Complexity: O(n)

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0 or len(height) == 1:
            return 0
        leftMax = [-1] * len(height)
        rightMax = [-1] * len(height)
        leftMax[0] = height[0]
        rightMax[-1] = height[-1]
        for i in range(1, len(height)):
            if height[i] > leftMax[i-1]:
                leftMax[i] = height[i]
            else:
                leftMax[i] = leftMax[i-1]
        for i in range(len(height)-2, -1, -1):
            if height[i] > rightMax[i+1]:
                rightMax[i] = height[i]
            else:
                rightMax[i] = rightMax[i+1]
        water = 0
        for i in range(len(height)):
            if min(leftMax[i], rightMax[i]) - height[i] > 0 :
                water += min(leftMax[i], rightMax[i]) - height[i]
        return water