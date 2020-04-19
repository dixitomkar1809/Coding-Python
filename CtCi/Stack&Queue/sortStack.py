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
            if self.isEmpty():
                self.stack[0] = element
                self.size += 1
                return True
            else:
                tempStack = self.stack[:]
                index = 0
                for item in tempStack:
                    if item > element:
                        self.stack[index] = element
                        self.stack[index+1:] = tempStack[index:-1]
                        self.size += 1
                        return True
                    else:
                        if item == float('-inf'):
                            self.stack[index] = element
                            index += 1
                            self.size += 1
                            return True
                        self.stack[index] = item 
                        index += 1
                self.stack[index-1] = element
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
            return self.stack[0]
        return None
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity

    def printStack(self):
        print(self.stack[:self.size])

if __name__=="__main__":
    sortStack = SortedStack(5)
    sortStack.push(1)
    sortStack.push(3)
    sortStack.push(4)
    sortStack.push(2)
    sortStack.push(5)
    sortStack.pop()
    sortStack.printStack()
    sortStack.push(6)
    sortStack.printStack()
    print(sortStack.stack)