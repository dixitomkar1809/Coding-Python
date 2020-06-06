# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given a binary tree for which you have to print its vertical order traversal. your task is to complete the function verticalOrder which takes one argument the root of the binary tree and prints the node of the binary tree in vertical order as shown below.
If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal.
'''
from collections import defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Solution:
    def __init__(self, root):
        self.root = root
        self.levelOrderTraversal = self.__levelOrderTraversal()
    
    # Time Complexity = O(n)
    def __levelOrderTraversal(self):
        queue = []
        queue.append([self.root, 0])
        levelOrderTraversal = defaultdict(list)
        while queue:
            node, level = queue.pop(0)
            levelOrderTraversal[level].append(node)
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        return levelOrderTraversal

if __name__=="__main__":
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    one.left = two
    one.right = three
    two.left = four
    two.right = five 
    three.left = six
    three.right = seven
    sol = Solution(one)
    for k in sol.levelOrderTraversal:
        for node in sol.levelOrderTraversal[k]:
            print(node.value, end=" ")
        print()