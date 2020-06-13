# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
You are given a linked list of N nodes. The task is to remove the loop from the linked list, if present.
'''

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def loopDetection(self, head):
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
        slow.next = None
    
    def printList(self, head):
        curr = head
        while curr:
            print(curr.val)
            curr = curr.next


if __name__ =="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = head.next
    sol = Solution()
    sol.loopDetection(head)
    sol.printList(head)
