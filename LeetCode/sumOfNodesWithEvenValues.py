# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.parents = collections.defaultdict(TreeNode)
        self.getParents(root, None)
        self.result = []
        self.inorder(root)
        return sum(self.result)
    
    def inorder(self, node):
        if not node:
            return
        parent = self.parents[node]
        grandparent = None
        if parent:
            grandparent = self.parents[parent]
        if grandparent and grandparent.val % 2 == 0:
            self.result.append(node.val)
        self.inorder(node.left)
        self.inorder(node.right)
        
    def getParents(self, node, parent):
        if not node:
            return 
        self.parents[node] = parent
        self.getParents(node.left, node)
        self.getParents(node.right, node)
        