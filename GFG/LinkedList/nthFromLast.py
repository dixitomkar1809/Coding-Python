# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a linked list consisting of L nodes and given a number N. The task is to find the Nth node from the end of the linked list.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def nThFromLast(self, head, k):
        fast = head
        for i in range(k):
            if not fast:
                return -1
            fast = fast.next
        slow = head
        while fast: 
            fast = fast.next
            slow = slow.next
        return slow.val

if __name__=='__main__':
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    one.next=two
    two.next=three
    three.next=four
    four.next=five
    five.next=six
    six.next=seven
    seven.next=eight
    eight.next = nine
    sol = Solution()
    print(sol.nThFromLast(one, 10))