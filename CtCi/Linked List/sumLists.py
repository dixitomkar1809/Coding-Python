# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

'''
Sum Lists: You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.
EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.
FOLLOW UP
Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 - > 1 -> 2. That is, 912.
'''

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sumLists(l1, l2):
    carry = 0
    head =l1
    while l2:
        summ = l2.val + l1.val + carry
        l1.val = summ % 10
        carry = summ //10
        if not l1.next:
            l1.next = l2.next
            break
        if not l2.next:
            break
        l1 = l1.next
        l2 = l2.next
    while carry > 0:
        if not l1.next:
            l1.next =  ListNode(0)
        l1 = l1.next
        summ = carry + l1.val
        l1.val = summ % 10
        carry  = summ //10
    return head

if __name__=="__main__":
    l1 = Node(2)
    l1.next = Node(4)
    l1.next.next = Node(3)
    l2 = Node(5)
    l2.next = Node(6)
    l2.next.next = Node(4)
    curr = sumLists(l1, l2)
    while curr:
        print(curr.val, end=" ")
        curr = curr.next