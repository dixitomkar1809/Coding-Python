# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/maximum-average-subtree/

# Time Complexity: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        return self.maxAvgHelper(root, 0)[2]
    
    def maxAvgHelper(self, root, maxAvg):
        if not root:
            return [0, 0, maxAvg]
        left = self.maxAvgHelper(root.left, maxAvg)
        right = self.maxAvgHelper(root.right, maxAvg)
        summ = left[0] + right[0] + root.val
        count = left[1] + right[1] + 1
        maxAvg = max(maxAvg, summ/count, left[2], right[2])
        return [summ, count, maxAvg]
         