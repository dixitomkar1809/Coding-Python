# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/subtree-of-another-tree/

# Time Complexity: O(n * m)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s or not t:
            return False
        elif s.val == t.val and self.checkSubtree(s, t):
            return True
        else:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def checkSubtree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        elif s.val != t.val:
            return False
        else:
            return self.checkSubtree(s.left, t.left) and self.checkSubtree(s.right, t.right)