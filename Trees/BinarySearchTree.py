# Author: Omkar Dixit
# Email: omedxt@gmail.com

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def addLeft(self, child):
        self.left = child
        child.parent = self

    def addRight(self, child):
        self.right = child
        child.parent = self

class BST:
    def __init__(self, root):
        self.root = root
        self.size = 1
        self.stack = []

    def find(self, x):
        self.stack= []
        self.stack.append(None)
        return self.findHelper(self.root, x, self.stack)

    def findHelper(self, t, x, s):
        if not t or t.value == x:
            return t
        while True:
            if t.value < x:
                if not t.right: break
                s.append(t)
                t = t.right
            elif t.value == x:
                return t
            else:
                if not t.left: break
                s.append(t)
                t = t.left
        return t

    def contains(self, x):
        t = self.find(x)
        return t and t.value == x

    def min(self):
        if not self.root:
            return None
        t = self.root
        while t.left:
            t = t.left
        return t

    def max(self):
        if not self.root:
            return None
        t = self.root
        while t.right:
            t = t.right
        return t

    def add(self, x):
        if not self.root:
            self.root = Node(x)
            self.size = 1
            return True
        t = self.find(x)
        if x == t.value:
            t.value = x
            return False
        elif x < t.value:
            t.left = Node(x)
        else:
            t.right = Node(x)
        self.size += 1
        return True

    def remove(self, x):
        if not self.root:
            return None
        t = self.find(x)
        if t.value != x:
            return None
        result = t.value
        if not t.left or not t.right:
            self.bypass(t)
        else:
            self.stack.append(t)
            minRight = self.find(t.right, t.value)
            t.value = minRight.value
            self.bypass(minRight)
        self.size -= 1
        return result

    def bypass(self, t):
        parent = self.stack[0]
        if t.left:
            child = t.left
        else:
            child = t.right
        if not parent:
            self.root = child
        elif parent.left == t:
            parent.left = child
        else:
            parent.right = child

if __name__=="__main__":
    node8 = Node(8)
    node3 = Node(3)
    node10 = Node(10)
    node1 = Node(1)
    node6 = Node(6)
    node14 = Node(14)
    node4 = Node(4)
    node7 = Node(7)
    node13 = Node(13)
    node8.addRight(node10)
    # node8.addLeft(node3)
    # node3.addLeft(node1)
    node3.addRight(node6)
    node6.addLeft(node4)
    node6.addRight(node7)
    node10.addRight(node14)
    node14.addLeft(node13)
    bst = BST(node8)
    bst.add(3)
    bst.remove(3)
