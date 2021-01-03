class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    
    def setLeft(r1, r2):
        if not r1 or not r2:
            return False
        r1.left = r2
    
    def setRight(r1, r2):
        if not r1 or not r2:
            return False
        r1.right = r2
    
    def getChildren(root):
        return [root.left, root.right]

def preOrderTraversal(root):
    if not root: 
        return
    print(root.value) 
    preOrderTraversal(root.left) 
    preOrderTraversal(root.right) 

def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.left)
    postOrderTraversal(root.right)
    print(root.value)

def inOrderTraversal(root):
    if not root:
        return 
    inOrderTraversal(root.left)
    print(root.value)
    inOrderTraversal(root.right)
