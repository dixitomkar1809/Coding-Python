# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Implement a Stack using two queues q1 and q2.
'''

class myStack:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    
    def push(self, element):
        self.queue1.append(element)
    
    def pop(self):
        if (len(self.queue1) == 0):
            return "Empty Stack"
        
        self.queue2 = []
        for i in range(len(self.queue1)-1, -1, -1):
            self.queue2.append(self.queue1[i])
        x = self.queue2[0]
        self.queue1 = []
        for i in range(len(self.queue2)-1, 0, -1):
            self.queue1.append(self.queue2[i])
        return x

if __name__=='__main__':
    myStack = myStack()
    myStack.push(1)
    myStack.push(2)
    myStack.push(3)
    myStack.push(4)
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    print(myStack.pop())
    myStack.push(4)
    print(myStack.pop())
    myStack.push(1)
    print(myStack.pop())