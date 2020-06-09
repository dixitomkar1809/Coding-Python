# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def getIntersection(self, head1, head2):
        curr1 = head1
        curr2 = head2
        while True:
            if curr1 == curr2:
                return curr1.value
            elif not curr1:
                curr1 = head2
            elif not curr2:
                curr2 = head1
            else:
                curr1 = curr1.next
                curr2 = curr2.next

if __name__=='__main__':
    three = Node(3)
    six = Node(6)
    nine = Node(9)
    fifteen = Node(15)
    thirty = Node(30)
    ten = Node(10)
    three.next = six
    six.next = nine
    nine.next = fifteen
    fifteen.next = thirty
    ten.next = fifteen
    sol = Solution()
    print(sol.getIntersection(three, ten))