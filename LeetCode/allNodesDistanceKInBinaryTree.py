# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

# Time Complexity: O(n)

import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        if not root:
            return []
        if K == 0:
            [root.val]
        self.parents = collections.defaultdict(TreeNode)
        self.seen = collections.defaultdict(bool)
        self.inorderProcess(root, None)
        queue = [(target, K)]
        self.seen[target] = True
        ans = []
        while queue:
            node, distance = queue.pop(0)
            if distance == 0:
                ans.append(node.val)
            else:
                if node.left and not self.seen[node.left]:
                    queue.append((node.left, distance - 1))
                    self.seen[node.left] = True
                if node.right and not self.seen[node.right]:
                    queue.append((node.right, distance - 1))
                    self.seen[node.right] = True
                if self.parents[node] and not self.seen[self.parents[node]]:
                    queue.append((self.parents[node], distance - 1))
                    self.seen[self.parents[node]] = True
        return ans
    
    def inorderProcess(self, root, parent):
        if root:
            self.inorderProcess(root.left, root)
            self.parents[root] = parent
            self.seen[root] = False
            self.inorderProcess(root.right, root)