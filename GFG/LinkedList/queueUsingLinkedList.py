# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Implement a Queue using Linked List.
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.count = 0

    
    def push(self, value):
        newNode = Node(value)
        if not self.head.value and not self.tail.value:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
    
    def pop(self):
        if self.head:
            val = self.head.value
            self.head = self.head.next
            return val
        self.__init__()
        return None

if __name__=='__main__':
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.head, q.tail)