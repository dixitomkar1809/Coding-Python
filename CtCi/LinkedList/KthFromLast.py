# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
'''

# Time Complexity: O(n) for n being the number of nodes

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def nthFromLast(head, n):
    fast = slow = head
    for i in range(n+1):
        if not fast:
            return "Out of Bounds"
        fast = fast.next
    while fast:
        slow = slow.next
        fast = fast.next
    return slow.val

if __name__=="__main__":
    if len(sys.argv) < 3:
        print("List not detected")
    else:
        n = int(sys.argv[1])
        head = Node(sys.argv[2])
        curr = head
        for i in sys.argv[3:]:
            node = Node(i)
            curr.next = node
            curr = node
        curr = head
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()
        print(nthFromLast(head, n))
