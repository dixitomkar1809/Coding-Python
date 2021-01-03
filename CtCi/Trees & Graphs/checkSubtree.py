# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Check Subtree: Tl and T2 are two very large binary trees, with Tl much bigger than T2. Create an
algorithm to determine if T2 is a subtree of Tl.
A tree T2 is a subtree of Tl if there exists a node n in Tl such that the subtree of n is identical to T2.
That is, if you cut off the tree at node n, the two trees would be identical.
'''

from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal

def checkSubtree(r1, r2):
    if not r1 or not r2:
        return False
    if r1.value==r2.value and sameTree(r1, r2):
        return True
    else:
        return checkSubtree(r1.left, r2) or checkSubtree(r1.right, r2)

def sameTree(r1, r2):
    if not r1 and not r2:
        return True
    elif not r1 or not r2:
        return False
    elif r1.value != r2.value:
        return False
    else:
        return sameTree(r1.left, r2.left) and sameTree(r1.right, r2.right)

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
    r1 = one
    newOne = TreeNode(2)
    newOne.left = TreeNode(4)
    newOne.right = TreeNode(5)
    r2 = newOne
    print(checkSubtree(r1, r2))
