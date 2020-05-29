# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two numbers represented by two lists, write a function that returns the sum list. The sum list is list representation of the addition of two input numbers.
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
            l1.next = Node(0)
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