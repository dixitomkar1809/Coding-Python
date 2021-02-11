# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/

# Time Complexity: O(n)

import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [(0, root)]
        self.levels = collections.defaultdict(list)
        while queue:
            level, node = queue.pop(0)
            self.levels[level].append(node.val)
            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))
        for level in self.levels:
            if level  % 2 != 0:
                self.levels[level] = reversed(self.levels[level])
        return list(self.levels.values())