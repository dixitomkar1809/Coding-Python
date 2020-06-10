# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Complete the function to print spiral order traversal of a tree.
'''

from collections import defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def getSpiralFormLevelOrderTraversal(self, root):
        rightToLeft = [root]
        leftToRight = []
        while rightToLeft or leftToRight:
            while rightToLeft:
                node = rightToLeft.pop()
                print(node.value, end=' ')
                if node.right:
                    leftToRight.append(node.right)
                if node.left:
                    leftToRight.append(node.left)
            while leftToRight:
                node = leftToRight.pop()
                print(node.value, end=' ')
                if node.left:
                    rightToLeft.append(node.left)
                if node.right:
                    rightToLeft.append(node.right)


if __name__=='__main__':
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    one.left = two
    one.right = three
    two.left = seven
    two.right = six
    three.left = five
    three.right = four
    sol = Solution()
    sol.getSpiralFormLevelOrderTraversal(one)
