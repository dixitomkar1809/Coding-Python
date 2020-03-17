# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. Ifxis contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.
EXAMPLE
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8 
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def partition(head, x):
    smallHead = None
    smallLast = None
    bigHead = None
    bigLast = None
    equalHead = None
    equalLast = None
    while head:
        if head.val == x:
            if not equalHead:
                equalHead = equalLast = head
            else:
                equalLast.next = head
                equalLast = equalLast.next
        elif head.val < x:
            if not smallHead:
                smallHead = smallLast = head
            else:
                smallLast.next = head
                smallLast = smallLast.next
        else:
            if not bigHead:
                bigHead = bigLast = head
            else:
                bigLast.next = head
                bigLast = bigLast.next
        head = head.next
    if bigLast:
        bigLast.next = None
    if not smallHead:
        if not equalHead:
            return bigHead
        equalLast.next = bigHead
        return equalHead 
    
    if not equalHead:
        smallLast.next = bigHead
        return smallHead
    smallLast.next = equalHead
    equalLast.next = bigHead
    return smallHead

if __name__=="__main__":
    one = Node(1)
    two = Node(2)
    three = Node(3)
    five = Node(5)
    eight = Node(8)
    ten = Node(10)
    secondFive = Node(5)
    three.next = five
    five.next = eight
    eight.next = secondFive
    secondFive.next = ten
    ten.next = two
    two.next = one
    curr = partition(three, 5)
    while curr:
        print(curr.val)
        curr = curr.next
