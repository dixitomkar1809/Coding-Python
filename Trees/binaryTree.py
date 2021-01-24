# Author: Omkar Dixit
# Email: omedxt@gmail.com

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.leftSum = 0
        self.rightSum = 0

    def addLeft(self, child):
        self.left = child
        child.parent = self

    def addRight(self, child):
        self.right = child
        child.parent = self

class BinaryTree:
    def __init__(self, root):
        self.root = root
        self.size = 1

    def getDepth(self, node):
        if not node:
            return -1
        else:
            return 1 + self.getDepth(node.parent)

    def getHeight(self, node):
        if not node:
            return -1
        lh = self.getHeight(node.left)
        rh = self.getHeight(node.right)
        return 1 + max(lh, rh)

    def traverse(self):
        self.__traverseHelper(self.root, 0)

    def __traverseHelper(self, node, depth):
        if not node:
            return -1
        else:
            lh = self.__traverseHelper(node.left, depth + 1)
            rh = self.__traverseHelper(node.right, depth + 1)
            height = 1 + max(lh, rh)
            print(node.value, depth, height)
            return height
    
    def getDiameter(self, root):
        if not root:
            return 0
        lh = self.getHeight(root.left)
        rh = self.getHeight(root.right)
        ld = self.getDiameter(root.left)
        rd = self.getDiameter(root.right)
        return max(1 + lh + rh, max(ld, rd))
    
    def getSum(self, root):
        if not root:
            return 0
        root.leftSum = self.getSum(root.left)
        root.rightSum = self.getSum(root.right)
        return root.value + root.leftSum + root.rightSum

if __name__=="__main__":
    root = Node('A')
    tree = BinaryTree(root)
    nodeB = Node('B')
    nodeC = Node('C')
    root.addLeft(nodeB)
    root.addRight(nodeC)
    tree.traverse()
