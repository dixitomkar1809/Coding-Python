# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a singly linked list of size N. The task is to swap elements in the linked list pairwise.
For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.
'''

# Time Complexity = O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def pairWiseSwap(self, head, k=2):
        next = prev = None
        curr = head
        count = k
        while curr and count != 0:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count -= 1
        if next:
            head.next = self.pairWiseSwap(next)
        return prev
    
    def printList(self, root):
        curr = root
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

if __name__=='__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    # head.next.next.next.next = Node(5)
    # head.next.next.next.next.next = Node(6)
    # head.next.next.next.next.next.next = Node(7)
    # head.next.next.next.next.next.next.next = Node(8)
    sol = Solution()
    newHead = sol.pairWiseSwap(head)
    sol.printList(newHead)