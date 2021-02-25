# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = collections.deque([])
        levelOrderTraversal = collections.defaultdict(list)
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            levelOrderTraversal[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return levelOrderTraversal.values()
        