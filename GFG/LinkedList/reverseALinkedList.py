# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a linked list of N nodes. The task is to reverse this list.
'''

# Time Complexity: O(n)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def reverse(self, root):
        next = prev = None
        curr = root
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev

    def printList(self, root):
        curr = root
        while curr:
            print(curr.value, end=" ")
            curr = curr.next
        print()

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    sol = Solution()
    newHead = sol.reverse(head)
    sol.printList(newHead)