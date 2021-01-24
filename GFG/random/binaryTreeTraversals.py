# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Binary tree traversal questions like left view, right view, top view, bottom view, maximum of a level, minimum of a level, children sum property, diameter etc.
'''

from collections import defaultdict

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.leftSum = 0
        self.rightSum = 0

class Solution:
    def __init__(self, root):
        self.root = root
        self.levelOrderTraversal = self.__levelOrderTraversal()
        self.levelOrderHorizontalDistanceTraversal = self.__levelOrderHorizontalDistanceTraversal()
        self.height = self.getHeight(self.root)
        self.diameter = self.getDiameter(self.root)
        print("Tree Height %d"%(self.height))
        print("Tree Diameter %d"%(self.diameter))
    
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
    def leftView(self):
        print("Left View")
        for item in self.levelOrderTraversal.values():
            print(item[0].value, end=" ")
        print()
        return 

    # Time Complexity = O(n)
    def rightView(self):
        print("Right View")
        for item in self.levelOrderTraversal.values():
            print(item[-1].value, end=" ")
        print()
        return 

    # Time Complexity = O(n)
    def topView(self):
        print("Top View")
        for key in sorted(self.levelOrderHorizontalDistanceTraversal):
            print(self.levelOrderHorizontalDistanceTraversal[key][0], end=" ")
        print()
        return 

    # Time Complexity = O(n)
    def bottomView(self):
        print("Bottom View")
        for key in sorted(self.levelOrderHorizontalDistanceTraversal):
            print(self.levelOrderHorizontalDistanceTraversal[key][-1], end=" ")
        print()
        return 

    # Time Complexity = O(n)
    def maxOfLevel(self, levelNumber):
        queue = []
        queue.append([self.root, 0])
        levelOrderTraversal = defaultdict()
        while queue:
            node, level = queue.pop(0)
            if level in levelOrderTraversal:
                if (levelOrderTraversal[level].value < node.value):
                    levelOrderTraversal[level] = node
            else:
                levelOrderTraversal[level] = node
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        if (level > len(levelOrderTraversal)) :
            print("Level doesn't Exist")
            return
        print("Max at %d Level "%(levelNumber))
        print(levelOrderTraversal[levelNumber].value)
        return 

    # Time Complexity = O(n)
    def minOfLevel(self, levelNumber):
        queue = []
        queue.append([self.root, 0])
        levelOrderTraversal = defaultdict()
        while queue:
            node, level = queue.pop(0)
            if level in levelOrderTraversal:
                if (levelOrderTraversal[level].value > node.value):
                    levelOrderTraversal[level] = node
            else:
                levelOrderTraversal[level] = node
            if node.left:
                queue.append([node.left, level+1])
            if node.right:
                queue.append([node.right, level+1])
        if (level > len(levelOrderTraversal)) :
            print("Level doesn't Exist")
            return
        print("Min at %d Level "%(levelNumber))
        print(levelOrderTraversal[levelNumber].value)
        return 

    # Time Complexity = O(n)
    def getHeight(self, node):
        if not node:
            return 0
        return 1 + max(self.getHeight(node.left), self.getHeight(node.right))
    
    def childrenSumProperty(self, root):
        print("Children Sum Property")
        self._childrenSumPropertyHelper(root)
        print("Root Left Sum: ", root.leftSum)
        print("Root Right Sum: ", root.rightSum)
        return

    def _childrenSumPropertyHelper(self, root):
        if not root:
            return 0
        root.leftSum = self._childrenSumPropertyHelper(root.left)
        root.rightSum = self._childrenSumPropertyHelper(root.right)
        return root.value + root.leftSum + root.rightSum

    # Time Complexity = O(n)
    def getDiameter(self, node):
        if not node:
            return 0
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        leftDiameter = self.getDiameter(node.left)
        rightDiameter = self.getDiameter(node.right)
        return max(leftHeight + rightHeight + 1, max(leftDiameter, rightDiameter))

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
    sol.leftView()
    sol.rightView()
    sol.topView()
    sol.bottomView()
    sol.maxOfLevel(2)
    sol.minOfLevel(1)
    sol.childrenSumProperty(one)