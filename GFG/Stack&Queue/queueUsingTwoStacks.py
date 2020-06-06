# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Implement a Queue using 2 stacks s1 and s2 
'''

class MyQueue(object):
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackOne = []
        self.stackTwo = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while (len(self.stackOne) != 0):
            self.stackTwo.append(self.stackOne[-1])
            self.stackOne.pop()
        self.stackOne.append(x)
        while len(self.stackTwo) != 0:
            self.stackOne.append(self.stackTwo[-1])
            self.stackTwo.pop()

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if (len(self.stackOne) == 0):
            return None
        return self.stackOne.pop()

if __name__=='__main__':
    q = MyQueue()
    q.push(1)
    print(q.pop())
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.pop())