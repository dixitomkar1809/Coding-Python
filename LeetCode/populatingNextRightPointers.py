# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        stack = collections.deque([])
        stack.append([root, 0])
        levelOrder = collections.defaultdict(list)
        while stack:
            node, level = stack.popleft()
            levelOrder[level].append(node)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        for level in levelOrder:
            for i in range(len(levelOrder[level])-1):
                levelOrder[level][i].next = levelOrder[level][i+1]
        return root