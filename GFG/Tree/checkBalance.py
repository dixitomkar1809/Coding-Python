# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree, find if it is height balanced or not. 
A tree is height balanced if difference between heights of left and right subtrees is not more than one for all nodes of tree.
'''

class Node:
    def __init__(self, data): 
        self.data = data 
        self.left = self.right = None

class Solution:
    def checkBalance(self, root):
        if not root:
            return True
        lh = self.height(root.left)
        rh = self.height(root.right)
        if (abs(lh - rh) <= 1) and self.checkBalance(root.right) and self.checkBalance(root.left):
            return True
        return False

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

if __name__=='__main__':
    sol = Solution()
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.left.left = Node(4) 
    root.left.right = Node(5) 
    root.right.left = Node(6) 
    root.left.left.left = Node(7)
    print(sol.checkBalance(root))