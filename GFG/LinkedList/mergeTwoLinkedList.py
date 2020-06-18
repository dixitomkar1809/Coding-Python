# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.
'''

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def mergeTwoLinkedList(self, head1, head2):
        if not head1:
            return head2
        if not head2:
            return head1
        x = head1
        y = head2
        head = None
        result = None
        if x.val < y.val:
            head = x
            x = x.next
        else:
            head = y
            y = y.next
        result = head
        while x and y:
            if x.val < y.val:
                result.next = x
                x = x.next
            else:
                result.next = y
                y = y.next
            result = result.next
        while y:
            result.next = y
            result = result.next
            y = y.next
        while x:
            result.next = x
            result = result.next
            x = x.next
        return head

    def printList(self, root):
        curr = root
        while curr:
            print(curr.val, end=" ")
            curr = curr.next
        print()

if __name__=='__main__':
    sol = Solution()
    head1 = Node(1)
    head1.next = Node(3)
    head1.next.next = Node(5)
    head2 = Node(2)
    head2.next = Node(4)
    head2.next.next = Node(6)
    sol.printList(sol.mergeTwoLinkedList(head1, head2))