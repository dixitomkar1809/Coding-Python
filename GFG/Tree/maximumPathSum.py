# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree in which each node element contains a number. Find the maximum possible sum from one leaf node to another.
'''

# Time Complexity: O(n)

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    def maximumPathSum(self, node):
        res = [float('-inf')]
        self.maximumPathSumUtil(node, res)
        return res[0]

    def maximumPathSumUtil(self, root, res):
        if not root:
            return 0
        if not root.left and not root.right:
            return root.data
        ls = self.maximumPathSumUtil(root.left, res)
        rs = self.maximumPathSumUtil(root.right, res)
        if root.left and root.right:
            res[0] = max(res[0], ls + rs + root.data)
            return max(ls, rs) + root.data
        if not root.left:
            return rs + root.data
        else:
            return ls + root.data

if __name__=='__main__':
    sol = Solution()
    root = Node(-15) 
    root.left = Node(5) 
    root.right = Node(6) 
    root.left.left = Node(-8) 
    root.left.right = Node(1) 
    root.left.left.left = Node(2) 
    root.left.left.right = Node(6) 
    root.right.left = Node(3) 
    root.right.right = Node(9) 
    root.right.right.right= Node(0) 
    root.right.right.right.left = Node(4) 
    root.right.right.right.right = Node(-1) 
    root.right.right.right.right.left = Node(10) 
    print(sol.maximumPathSum(root))