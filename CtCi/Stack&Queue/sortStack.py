# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Sort Stack: Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
'''

class SortedStack:
    def __init__(self, capacity):
        self.stack = [float('-inf')] * capacity
        self.capacity = capacity
        self.size = 0
    
    def push(self, element):
        if not self.isFull():
            self.stack[self.size] = element
            self.size += 1
            return True
        print('Stack Full!')
        return False
    
    def pop(self):
        if not self.isEmpty():
            element = self.stack[self.size - 1]
            self.size -= 1
            return element
        else:
            return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.size-1]
        return None
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity

    def printStack(self):
        print(self.stack[:self.size])
    
def sortStackFunc(originalStack):
    tempStack = SortedStack(5)
    while not originalStack.isEmpty():
        currData = originalStack.pop()
        while not tempStack.isEmpty() and tempStack.peek() > currData:
            originalStack.push(tempStack.pop())
        tempStack.push(currData)
    while not tempStack.isEmpty():
        originalStack.push(tempStack.pop())

if __name__=="__main__":
    sortStack = SortedStack(5)
    sortStack.push(1)
    sortStack.push(3)
    sortStack.push(4)
    sortStack.push(2)
    sortStack.push(5)
    sortStackFunc(sortStack)
    sortStack.printStack()
    sortStack.pop()
    sortStackFunc(sortStack)
    sortStack.printStack()
    sortStack.push(6)
    sortStackFunc(sortStack)
    sortStack.printStack()