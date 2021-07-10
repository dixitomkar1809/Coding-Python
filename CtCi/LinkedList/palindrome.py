# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Palindrome: Implement a function to check if a linked list is a palindrome.
'''

# Time Complexity: O(n) for n being the number of nodes

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def palindrome(head):
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    prev = next = None
    curr = slow
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    while prev:
        if head.val != prev.val:
            return False
        head = head.next
        prev = prev.next
    return True

if __name__=="__main__":
    # head = Node(1)
    # head.next = Node(2)
    # head.next.next = Node(2)
    # head.next.next.next = Node(1)
    head = Node(1)
    head.next = Node(3)
    head.next.next = Node(4)
    print(palindrome(head))