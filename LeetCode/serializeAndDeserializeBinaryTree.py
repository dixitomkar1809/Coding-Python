# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

# Time Complexity: O(n) n is number of nodes

import collections
import heapq

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        return self.serializeHelper(root, '')
    
    def serializeHelper(self, root, data):
        if root is None:
            data += 'None,'
        else:
            data += (str(root.val) + ',')
            data = self.serializeHelper(root.left, data)
            data = self.serializeHelper(root.right, data)
        return data
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        dataList = data.split(',')
        return self.deserializeHelper(dataList)
    
    def deserializeHelper(self, data):
        if data[0] == 'None':
            data.pop(0)
            return None
        root = TreeNode(data.pop(0))
        root.left = self.deserializeHelper(data)
        root.right = self.deserializeHelper(data)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))