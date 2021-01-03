# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Validate BST: Implement a function to check if a binary tree is a binary search tree.
'''

from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal

# recent keeps track of the last value compared

def validBST(root, recent):
    if not root:
        return True
    if not(validBST(root.left, recent)):
        return False
    if recent is not None and root.value <= recent:
        return False
    recent = root.value
    if not(validBST(root.right, recent)):
        return False
    return True

if __name__=="__main__":
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    print(validBST(one, None))