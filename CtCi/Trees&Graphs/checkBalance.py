# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Check Balanced: Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
'''

from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal

def height(root):
    if not root:
        return 0
    return max(height(root.left), height(root.right))+1

def checkBalance(root):
    if not root:
        return True
    leftHeight = height(root.left)
    rightHeight = height(root.right)
    if (abs(leftHeight-rightHeight)<=1) and checkBalance(root.right) and checkBalance(root.left):
        return True
    return False


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
    print(checkBalance(one))