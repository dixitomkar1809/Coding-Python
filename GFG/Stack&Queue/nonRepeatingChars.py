# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an input stream of N characters consisting only of lower case alphabets. The task is to find the first non repeating character, each time a character is inserted to the stream. If no non repeating element is found print -1.
'''

# Time COmplexity: Add to DLL O(1), remove O(1)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, value):
        newNode = Node(value)
        self.tail.prev.next = newNode
        newNode.next = self.tail
        newNode.prev = self.tail.prev
        self.tail.prev = newNode
        return newNode
    
    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev


class Solution:
    def nonRepeatingChars(self):
        inDLL = [None] * 256
        repeated = [False] * 256
        dll = DLL()
        while True:
            x = input('Enter Character: ')
            if x == 'exit':
                break
            x = str(x)
            if not inDLL[ord(x)] and not repeated[ord(x)]:
                # Element seen first time
                newNode = dll.add(x)
                inDLL[ord(x)] = newNode
            elif inDLL[ord(x)]:
                # Seen once
                repeated[ord(x)] = True
                dll.remove(inDLL[ord(x)])
                inDLL[ord(x)] = None
            print('Current First Non-repeating is: ', dll.head.next.value if dll.head.next.value else -1)    


if __name__=='__main__':
    sol = Solution()
    sol.nonRepeatingChars()