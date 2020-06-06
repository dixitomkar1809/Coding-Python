# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a binary tree, print the bottom view from left to right.
A node is included in bottom view if it can be seen when we look at the tree from bottom.
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
        self.levelOrderHorizontalDistanceTraversal = self.__levelOrderHorizontalDistanceTraversal()

    # Time Complexity = O(n)
    def __levelOrderHorizontalDistanceTraversal(self):
        queue = []
        queue.append([self.root, 0, 0])
        levelOrderHorizontalDistanceTraversal = defaultdict(list)
        while queue:
            node, level, horizontalDistance = queue.pop(0)
            levelOrderHorizontalDistanceTraversal[horizontalDistance].append(node.value)
            if node.left:
                queue.append([node.left, level+1, horizontalDistance - 1])
            if node.right:
                queue.append([node.right, level+1, horizontalDistance + 1])
        return levelOrderHorizontalDistanceTraversal
    
    # Time Complexity = O(n)
    def bottomView(self):
        print("Bottom View")
        for key in sorted(self.levelOrderHorizontalDistanceTraversal):
            print(self.levelOrderHorizontalDistanceTraversal[key][-1], end=" ")
        print()
        return 


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
    sol.bottomView()