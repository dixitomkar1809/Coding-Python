# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link:  https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        levelOrder = collections.defaultdict(list)
        queue = collections.deque([[root, 0]])
        lowLevel = 0
        highLevel = 0
        while queue:
            node, level = queue.popleft()
            if node:
                levelOrder[level].append(node.val)
                lowLevel = min(lowLevel, level)
                highLevel = max(highLevel, level)
                queue.append([node.left, level - 1])
                queue.append([node.right, level + 1])
        return [levelOrder[level] for level in range(lowLevel, highLevel + 1)]
        