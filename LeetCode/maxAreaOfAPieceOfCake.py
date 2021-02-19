# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/

# Time Complexity: O(max(h, w))

class Solution(object):
    def maxArea(self, h, w, horizontalCuts, verticalCuts):
        """
        :type h: int
        :type w: int
        :type horizontalCuts: List[int]
        :type verticalCuts: List[int]
        :rtype: int
        """
        horizontalMax = self.helper(h, horizontalCuts)
        verticalMax = self.helper(w, verticalCuts)
        return (horizontalMax * verticalMax) % 1000000007
        
    def helper(self, c, cuts):
        cuts = sorted(cuts)
        maxCut = max(c - cuts[-1], cuts[0])
        for i in range(1, len(cuts)):
            maxCut = max(maxCut, cuts[i] - cuts[i-1])
        return maxCut