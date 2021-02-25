# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/two-sum-bsts/

# Time Complexity: O(n1 + n2) n1 is number of nodes in first tree and n2 in second tree

import collections

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        hashmap = {}
        queue = collections.deque([root1])
        while queue:
            node = queue.popleft()
            hashmap[node.val] = 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        queue = collections.deque([root2])
        while queue:
            node = queue.popleft()
            if (target - node.val) in hashmap:
                return True
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return False
            