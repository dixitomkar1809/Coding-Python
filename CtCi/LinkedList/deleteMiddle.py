# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
that node.
EXAMPLE
lnput:the node c from the linked lista->b->c->d->e->f
Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
'''

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def deleteMiddle(head, node):
    if (not node or not node.next):
        return False
    nextNode = node.next
    node.val = nextNode.val
    node.next = nextNode.next

if __name__=="__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    one.next=two
    two.next=three
    three.next=four
    four.next=five
    five.next=six
    six.next=seven
    seven.next=eight
    deleteMiddle(one, four)
    head = one
    while head:
        print(head.val)
        head = head.next