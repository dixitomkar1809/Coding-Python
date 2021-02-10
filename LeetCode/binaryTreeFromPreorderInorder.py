# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Time Complexity: T(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.inorderMap = {node: i for i, node in enumerate(inorder)}
        self.preorderindex = 0
        return self.buildTreeHelper(preorder, 0, len(inorder), inorder)
        
    def buildTreeHelper(self, preorder, inorderleftindex, inorderrightindex, inorder):
        if inorderleftindex >= inorderrightindex:
            return None
        root = TreeNode(preorder[self.preorderindex])
        index = self.inorderMap[root.val]
        self.preorderindex += 1
        root.left = self.buildTreeHelper( preorder, inorderleftindex, index, inorder)
        root.right = self.buildTreeHelper( preorder, index + 1, inorderrightindex, inorder)
        return root
        