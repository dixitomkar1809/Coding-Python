# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Delete Middle

import sys

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    
def deleteMiddle(head):
    temp = head.next
    head.val = temp.val
    head.next = temp.next
    temp = None
    return head

if __name__=="__main__":
    if len(sys.argv)==1:
        print("List not detected")
    else:
        head = Node(sys.argv[1])
        if len(sys.argv)==2:
            print(head.val)
        else:
            curr = head
            for i in sys.argv[2:]:
                node = Node(i)
                curr.next = node
                curr = node
            head = deleteMiddle(head.next)
            while(head):
                print(head.val, end=" ")
                head = head.next