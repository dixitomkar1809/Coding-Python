# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Binary Search Tree (with all values unique) and two node values. Find the Lowest Common Ancestors of the two nodes in the BST.
'''

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None

class Solution:
    def findLCABST(self, root, node1, node2):
        if not root:
            return None
        if root.data > node1.data and root.data > node2.data:
            return self.findLCABST(root.left, node1, node2)
        if root.data < node1.data and root.data < node2.data:
            return self.findLCABST(root.right, node1, node2)
        return root.data

if __name__=='__main__':
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    five.left = four
    five.right = six
    four.left = three
    six.right = seven
    seven.right = eight
    sol = Solution()
    print(sol.findLCABST(five, three, eight))