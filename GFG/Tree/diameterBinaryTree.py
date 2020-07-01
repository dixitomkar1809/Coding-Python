# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Binary Tree, find diameter of it.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def diameter(self, root):
        if not root:
            return 0
        lh = self.height(root.left)
        rh = self.height(root.right)
        ld = self.diameter(root.left)
        rd = self.diameter(root.right)
        return max(lh + rh + 1, max(ld, rd))

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
    print(sol.diameter(root))