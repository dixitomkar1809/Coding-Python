# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given a pointer/ reference to the node which is to be deleted from the linked list of N nodes. The task is to delete the node. Pointer/ reference to head node is not given. 
'''

# Time Complexity: O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def deleteNode(self, node):
        if not node or not node.next:
            node = None
            return 
        curr = node
        while curr.next:
            curr.value = curr.next.value
            curr = curr.next
        curr = None
        return node

if __name__=='__main__':
    sol = Solution()
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    sol.deleteNode(head1.next)