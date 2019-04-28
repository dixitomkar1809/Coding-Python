# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
beginning of the loop.
DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
as to make a loop in the linked list.
EXAMPLE
Input: A -> B -> C - > D -> E -> C [the same C as earlier]
Output: C
'''

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def loopDetection(head):
    if not head or not head.next:
        return None
    fast = slow = head
    fast = fast.next.next
    slow = slow.next
    # Detects Loop
    while fast and fast.next:
        if fast == slow :
            break
        fast = fast.next.next
        slow = slow.next
    if slow != fast:
        return None
    slow = head
    while slow!=fast:
        fast = fast.next
        slow = slow.next
    return slow.val

if __name__ =="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next
    print(loopDetection(head))
