# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a singly linked list of N nodes. The task is to find the middle of the linked list. For example, if given linked list is 1->2->3->4->5 then the output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4.
'''

# Time Complexity: O(n)

class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class Solution:
    
    def getMiddle(self, head):
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.value

if __name__=="__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    sol = Solution()
    print(sol.getMiddle(head))