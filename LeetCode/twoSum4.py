# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

# Time Complexity: O(N) N is number of nodes

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.hashmap = {}
        return self.helper(root, k)
        
    def helper(self, root, target):
        if root:
            if (target - root.val) in self.hashmap:
                return True
            self.hashmap[root.val] = 1
            return self.helper(root.left, target) or self.helper(root.right, target)