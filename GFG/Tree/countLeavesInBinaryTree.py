
# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Binary Tree of size N , You have to count leaves in it. For example, there are two leaves in following tree
'''

class Node: 
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Solution:
    def countLeaves(self, root, leaf):
        if not root:
            return leaf
        if not root.left and not root.right:
            leaf += 1
            return leaf
        leaf = self.countLeaves(root.left, leaf)
        leaf = self.countLeaves(root.right, leaf)
        return leaf

if __name__=='__main__':
    sol = Solution()
    root = Node(1) 
    root.left = Node(2) 
    root.right = Node(3) 
    root.right.left = Node(4)
    root.right.right = Node(5)
    print(sol.countLeaves(root, 0))