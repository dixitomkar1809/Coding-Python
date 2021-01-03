# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Random Node: You are implementing a binary tree class from scratch which, in addition to insert, find, and delete, has a method getRandomNode() which returns a random node from the tree. All nodes should be equally likely to be chosen. Design and implement an algorithm for getRandomNode, and explain how you would implement the rest of the methods.
'''

import random

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.size = 1
        self.left = None
        self.right = None

class Solution:

    def insertAtOrder(self, value, root):
        if value < root.value:
            if not root.left:
                root.left = TreeNode(value)
            else:
                self.insertAtOrder(value, root.left)
        else:
            if not root.right:
                root.right = TreeNode(value)
            else:
                self.insertAtOrder(value, root.right)
        root.size += 1

    def getRandomNode(self, root, size):
        leftSize = 0 if not root.left else root.left.size
        index = random.randint(1, size)
        print(size, index, leftSize)
        if index < leftSize:
            return self.getRandomNode(root.left, size)
        elif index == leftSize:
            return root
        else:
            return self.getRandomNode(root.right, size)

    def find(self, value, root):
        if not root:
            return None
        if value < root.value:
            return self.find(value, root.left)
        elif value == root.value:
            return root.value
        else:
            return self.find(value, root.right)

if __name__=="__main__":
    root = TreeNode(50)
    sol = Solution()
    sol.insertAtOrder(20, root)
    sol.insertAtOrder(60, root)
    sol.insertAtOrder(25, root)
    sol.insertAtOrder(10, root)
    sol.insertAtOrder(15, root)
    sol.insertAtOrder(5, root)
    sol.insertAtOrder(70, root)
    sol.insertAtOrder(65, root)
    sol.insertAtOrder(80, root)
    print(sol.find(sol.getRandomNode(root, root.size).value, root))