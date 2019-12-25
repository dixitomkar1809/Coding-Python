# Author: Omkar Dixit
# Email: omedxt@gmail.com

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None

    def addChild(self, child):
        self.children.append(child)
        child.parent = self

class Tree:
    def __init__(self, root):
        self.root = root
        self.size = 1

if __name__=="__main__":
    root = Node('A')
    tree = Tree(root)


