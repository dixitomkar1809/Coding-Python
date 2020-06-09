# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a linked list of N nodes. The task is to check if the the linked list has a loop. Linked list can contain self loop.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def detectLoop(self, head):
        slow = head
        fast = head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__=='__main__':
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    one.next = two
    two.next = three
    three.next = four
    four.next = five
    # five.next = two
    sol = Solution()
    print(sol.detectLoop(one))