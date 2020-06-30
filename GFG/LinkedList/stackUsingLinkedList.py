# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Implement a Stack using Linked List.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self, value):
        newNode = Node(value)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
    
    def pop(self):
        if self.head:
            val = self.head.value
            self.head = self.head.next
            return val
        self.__init__()
        return None

if __name__=='__main__':
    q = Stack()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())