class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None   

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
