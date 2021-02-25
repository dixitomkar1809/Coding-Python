# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

# Time Complexity: O(n) n is size of array

import collections
import heapq

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        self.i = 0
        self.preorder = preorder
        return self.helper(float('-inf'), float('inf'))
    
    def helper(self, lower, upper):
        if self.i == len(self.preorder):
            return None
        if self.preorder[self.i] < lower or self.preorder[self.i] > upper:
            return None
        root = TreeNode(self.preorder[self.i])
        self.i+=1
        root.left = self.helper(lower, root.val)
        root.right = self.helper(root.val, upper)
        return root