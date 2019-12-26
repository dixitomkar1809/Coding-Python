# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to the problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        return self.inOrder(root, k, [])[k - 1]

    def inOrder(self, root, k, sol):
        if root:
            self.inOrder(root.left, k - 1, sol)
            sol.append(root.val)
            self.inOrder(root.right, k - 1, sol)
        # print(sol)
        return sol