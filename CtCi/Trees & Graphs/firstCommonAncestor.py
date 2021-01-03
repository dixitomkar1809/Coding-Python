# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is noxt
necessarily a binary search tree.
'''

from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal

bothPending = 2
leftDone = 1
bothDone = 0

def firstCommonAncestor(root, p, q):
    stack = [(root, bothPending)]
    # Set when p or q is found
    oneNodeFound = False
    # common Ancestor Index
    fcaIndex = -1    
    while stack:
        parentNode, parentState = stack[-1]
        if parentState != bothDone:
            if parentState == bothPending:
                if parentNode==p or parentNode==q:
                    if oneNodeFound:
                        return stack[fcaIndex][0].value
                    else:
                        oneNodeFound=True
                        fcaIndex = len(stack)-1
                childNode = parentNode.left
            else:
                childNode = parentNode.right
            stack.pop()
            stack.append((parentNode, parentState-1))
            if childNode:
                stack.append((childNode, bothPending))
        else:
            if oneNodeFound and len(stack)-1==fcaIndex:
                fcaIndex-=1
            stack.pop()
    return None
        
if __name__=="__main__":
    one = TreeNode(1)
    two = TreeNode(2)
    three = TreeNode(3)
    four = TreeNode(4)
    five = TreeNode(5)
    six = TreeNode(6)
    seven = TreeNode(7)
    eight = TreeNode(8)
    nine = TreeNode(9)
    one.left = two
    one.right = three
    two.left = four
    two.right = five 
    three.left = six
    three.right = seven
    four.left = eight
    four.right = nine
    print(firstCommonAncestor(one, eight, five))