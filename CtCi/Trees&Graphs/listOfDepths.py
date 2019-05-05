# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
'''
from Node import TreeNode, preOrderTraversal, postOrderTraversal, inOrderTraversal
from collections import defaultdict

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Simple level order traversal
def listOfDepths(root):
    cnt = 1
    queue = []
    queue.append([root, cnt])
    sol = defaultdict(list)
    while queue:
        node, level = queue.pop(0)
        sol[level].append(node.value)
        if node.left:
            queue.append([node.left, level+1])
        if node.right:
            queue.append([node.right, level+1])
    return sol

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
    lists = listOfDepths(one)
    print(lists)
    for l in lists:
        curr = LinkedListNode(None)
        for i in lists[l]:
            curr.next = LinkedListNode(i)
            curr = curr.next
        
        
