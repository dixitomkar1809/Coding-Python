# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link to the problem: https://leetcode.com/problems/boundary-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.boundary = []
    
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return self.boundary
        if self.isLeaf(root):
            return [root.val]
        else:
            self.boundary.append(root.val)
            curr = root.left
            self.getLeftBoundary(curr)
            self.getLeaves(root)
            curr = root.right
            self.getRightBoundary(curr)
            return self.boundary 
        
    def isLeaf(self, root):
        return root.left == None and root.right == None
    
    def getLeaves(self, root):
        if self.isLeaf(root):
            self.boundary.append(root.val)
        else:
            if root.left:
                self.getLeaves(root.left)
            if root.right:
                self.getLeaves(root.right)
        return 
    
    def getLeftBoundary(self, root):
        while root:
            if not self.isLeaf(root):
                self.boundary.append(root.val)
            if root.left:
                root = root.left
            else:
                root = root.right
        return
    
    def getRightBoundary(self, root):
        stack = []
        while root:
            if not self.isLeaf(root):
                stack.append(root.val)
            if root.right:
                root = root.right
            else:
                root = root.left
        while stack:
            self.boundary.append(stack.pop())
        return
        