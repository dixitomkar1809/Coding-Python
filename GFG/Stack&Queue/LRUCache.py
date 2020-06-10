# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
The task is to design and implement methods of an LRU cache. The class has two methods get() and set() which are defined as follows.
get(x)   : Returns the value of the key x if the key exists in the cache otherwise returns -1.
set(x,y) : inserts the value if the key x is not already present. If the cache reaches its capacity it should invalidate the least recently used item before inserting the new item.
In the constructor of the class the size of the cache should be intitialized.
'''

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.hMap = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.size = 0
        self.capacity = capacity
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        node = self.hMap.get(key, None)
        if not node:
            return -1
        self.__moveToHead(node)
        return node.value
    
    def put(self, key, value):
        node = self.hMap.get(key)
        if not node:
            newNode = Node(key, value)
            self.hMap[key] = newNode
            self.__addNode(newNode)
            self.size += 1
            if self.size > self.capacity:
                tail = self.__popTail()
                del self.hMap[tail.key]
                self.size -= 1
        else:
            node.value = value
            self.__moveToHead(node)
    
    def __addNode(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    def __removeNode(self, node):
        prev = node.prev
        new = node.next
        prev.next, new.prev = new, prev
    
    def __moveToHead(self, node):
        self.__removeNode(node)
        self.__addNode(node)
    
    def __popTail(self):
        res = self.tail.prev
        self.__removeNode(res)
        return res
    
if __name__=='__main__':
    lruCache = LRUCache(2)
    lruCache.put(1, 1)
    lruCache.put(2, 2)
    print(lruCache.get(1))
    lruCache.put(3, 3)
    print(lruCache.get(2))
    lruCache.put(4, 4)
    print(lruCache.get(1))
    print(lruCache.get(3))
    print(lruCache.get(4))
