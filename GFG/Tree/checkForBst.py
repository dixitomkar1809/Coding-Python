# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree. Check whether it is a BST or not.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def checkBst(self, root, left = None, right = None):
        if not root:
            return True
        if left and root.value < left.value:
            return False
        if right and root.value >= right.value:
            return False
        return self.checkBst(root.left, left, root) and self.checkBst(root.right, root, right)

if __name__=="__main__":
    root = Node(3)  
    root.left = Node(2)  
    root.right = Node(5)  
    # root.right.left = Node(1)  
    # root.right.right = Node(4)
    sol = Solution()
    print(sol.checkBst(root))