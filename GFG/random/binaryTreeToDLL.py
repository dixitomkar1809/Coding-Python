# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a Binary Tree (BT), convert it to a Doubly Linked List(DLL) In-Place. The left and right pointers in nodes are to be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be same as Inorder of the given Binary Tree. The first node of Inorder traversal (left most node in BT) must be head node of the DLL.
'''

# Time Complexity = O(n)

class TreeDLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.head = TreeDLLNode(None)
        self.root = None

    def binaryToDLL(self, root):
        if not root:
            return 
        self.binaryToDLL(root.right)
        root.next = self.head
        if self.head.value:
            self.head.prev = root
        self.head = root
        self.binaryToDLL(root.left)

    def printDLL(self):
        root = self.head
        while root:
            print(root.value)
            if not root.next: break
            root = root.next

if __name__=="__main__":
    ten = TreeDLLNode(10)
    twelve = TreeDLLNode(12)
    fifteen = TreeDLLNode(15)
    twentyFive = TreeDLLNode(25)
    thirty = TreeDLLNode(30)
    thirtySix = TreeDLLNode(36)
    ten.left = twelve
    ten.right = fifteen
    twelve.right = thirty
    twelve.left = twentyFive
    fifteen.left = thirtySix
    sol = Solution()
    sol.binaryToDLL(ten)
    sol.printDLL()