# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a singly linked list of size N. The task is to rotate the linked list counter-clockwise by k nodes, where k is a given positive integer smaller than or equal to length of the linked list.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def rotateLinkedList(self, head, k):
        if k == 0 or not head:
            return head
        count = 1
        curr = head
        while k != count and curr:
            count+=1
            curr = curr.next
        if not curr:
            return None
        newHead = curr
        while curr.next:
            curr = curr.next
        curr.next = head
        head = newHead.next
        newHead.next = None
        return head


if __name__=='__main__':
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    one.next=two
    two.next=three
    three.next=four
    four.next=five
    five.next=six
    six.next=seven
    seven.next=eight
    sol = Solution()
    head = sol.rotateLinkedList(one, 3)
    while head:
        print(head.value)
        head = head.next