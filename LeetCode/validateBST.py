# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to the problem: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: 'TreeNode') -> 'bool':
        mini = float('-inf')
        maxi = float('inf')
        return self.bstUtil(root, mini, maxi)

    def bstUtil(self, root, mini, maxi):
        if root is None:
            return True
        return root.val > mini and root.val < maxi and self.bstUtil(root.left, mini, root.val) and self.bstUtil(
            root.right, root.val, maxi)