# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/balanced-binary-tree/

# Time Complexity: O(nLogN) isBalanced O(n) solution isBalanced2

import collections
import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        return abs(lh-rh) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
    def height(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        return 1 + max(lh, rh)
    
    def isBalanced2(self, root):
        return self.isBalancedHelper(root)[0]

    def isBalancedHelper(self, root):
        if not root:
            return True, -1
        leftBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftBalanced:
            return False, 0
        rightBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightBalanced:
            return False, 0
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)