# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/

# Time Complexity: O(n) n is number of nodes in tree

import collections
import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        self.limit = limit
        result = self.dfs(root, 0)
        return None if result < limit else root
    
    def dfs(self, node, summ):
        if not node:
            return summ
        left = self.dfs(node.left, summ + node.val)
        right = self.dfs(node.right, summ + node.val)
        if not node.left and not node.right:
            value = summ + node.val
        elif not node.left:
            value = right
        elif not node.right:
            value = left
        else:
            value = max(left, right)
        if left < self.limit:
            node.left = None
        if right < self.limit:
            node.right = None
        return value