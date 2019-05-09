# Author: Omkar Dixit  
# Email: ond170030@utdallas.edu

'''
Successor: Write an algorithm to find the "next" node (i.e., in-order successor) of a given node in a
binary search tree. You may assume that each node has a link to its parent.
'''

from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal

# Gets the minimum value of that particular tree, we dont really have to search the entire tree since we need the immediate successsor, most of the time it will be the next node in sorted order of all nodes in the tree
# rType - TreeNode
# input - TreeNode
def minValue(root):
    curr = root
    while curr:
        if not curr.left:
            break
        curr = curr.left
    return curr    

# gets the immediate successor of the node sent to it.
# rType- TreeNode
# input - TreeNode
def successor(root):
    if root.right:
        return minValue(root.right)
    parent = root.parent
    while parent:
        if root != parent.right:
            break
        root = parent
        parent = parent.parent
    return parent

if __name__=="__main__":
    twenty = TreeNode(20)
    eight = TreeNode(20)
    four = TreeNode(4)
    twelve = TreeNode(12)
    ten = TreeNode(10)
    fourteen = TreeNode(14)
    twentytwo = TreeNode(22)
    # setting Parents
    eight.parent = twenty
    four.parent = eight
    twelve.parent = eight
    ten.parent = twelve
    fourteen.parent = twelve
    twentytwo.parent = twenty
    # left right
    twenty.right = twentytwo
    twenty.left = eight
    eight.left = four
    eight.right = twelve
    twelve.left = ten
    twelve.right = fourteen
    print(successor(fourteen).value)

