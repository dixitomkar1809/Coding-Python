# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
'''

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def intersection(l1, l2):
    if not l1 or not l2:
        return None
    headA, headB = l1, l2
    while headA != headB and (headA or headB):
        if not headA:
            headA = l2
        if not headB:
            headB = l1
        if headA == headB:
            break
        headA = headA.next
        headB = headB.next
    return headA.val if headA==headB else None

if __name__=="__main__":
    l1 = Node(4)
    l1.next = Node(1)
    l1.next.next = Node(8)
    l1.next.next.next = Node(4)
    l1.next.next.next.next = Node(5)
    l2 = Node(5)
    l2.next = Node(0)
    l2.next.next = Node(1)
    l2.next.next.next = l1.next.next
    l2.next.next.next.next = Node(4)
    l2.next.next.next.next.next = Node(5)
    print(intersection(l1, l2))
