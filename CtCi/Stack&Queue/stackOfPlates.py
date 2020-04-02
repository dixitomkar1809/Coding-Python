# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
FOLLOW UP
Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
'''

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [float('-inf')] * self.capacity
        self.size = 0

    def pop(self):
        if self.isEmpty():
            return None
        val = self.stack[self.size-1]
        self.size-=1
        return val

    def push(self, value):
        if self.isFull():
            return False
        self.stack[self.size] = value
        self.size += 1
        return True

    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity

class setOfStacks:
    def  __init__(self, capacity): 
        self.setOfStacks = []
        self.stackCapacity = capacity
        self.noOfStacks = 0
        self.size = 0
        self.addStack(Stack(self.stackCapacity))
    
    def addStack(self, newStack):
        self.setOfStacks.append(newStack)
        self.noOfStacks += 1

    def getLastStack(self):
        return self.setOfStacks[-1]

    def pop(self):
        last = self.getLastStack()
        if not last: return None
        value = last.pop()
        if last.isEmpty():
            del self.setOfStacks[-1]
            self.noOfStacks -= 1
        return value
    
    # def pop(self, i):
    #     pass

    def push(self, value):
        last = self.getLastStack()
        if not last.isFull():
            last.push(value)
            return True
        print('here')
        newStack = Stack(self.stackCapacity)
        newStack.push(value)
        self.addStack(newStack)
        return True

if __name__ == '__main__':
    stackOfPlates = setOfStacks(6)
    stackOfPlates.push(1)
    stackOfPlates.push(1)
    stackOfPlates.push(1)
    stackOfPlates.push(1)
    stackOfPlates.push(1)
    stackOfPlates.push(1)
    stackOfPlates.push(2)
    stackOfPlates.pop()
    for stack in stackOfPlates.setOfStacks:
        print(stack.stack)


