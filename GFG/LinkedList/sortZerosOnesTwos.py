# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a linked list of N nodes where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list such that all zeros segregate to head side, 2s at the end of the linked list, and 1s in the mid of 0s and 2s.
'''

# Time Complexity: O(n)

class Node:
    def  __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def sortLinkedList(self, head):
        zeroHead = None
        oneHead = None
        twoHead = None
        currZeroHead = None
        currOneHead = None
        currTwoHead = None
        curr = head
        while curr:
            if curr.value == 0:
                if not zeroHead:
                    zeroHead = curr
                    currZeroHead = zeroHead
                else:
                    currZeroHead.next = curr
                    currZeroHead = currZeroHead.next
            elif curr.value == 1:
                if not oneHead:
                    oneHead = curr
                    currOneHead = oneHead
                else:
                    currOneHead.next = curr
                    currOneHead = currOneHead.next
            else:
                if not twoHead:
                    twoHead = curr
                    currTwoHead = twoHead
                else:
                    currTwoHead.next = curr
                    currTwoHead = currTwoHead.next
            curr = curr.next
        currZeroHead.next = oneHead if oneHead else twoHead
        currOneHead.next = twoHead
        currTwoHead.next = None
        return zeroHead
            
    def printList(self, node): 
        while (node != None): 
            print(node.value, end = " ") 
            node = node.next  


if __name__=='__main__':
    sol = Solution()
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(0)
    head.next.next.next = Node(1)
    sol.printList(sol.sortLinkedList(head))