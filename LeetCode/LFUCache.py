# Author: Omkar Dixit
# Email: omedxt@gmail.com

#Link: https://leetcode.com/problems/lfu-cache/

import collections

class DLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        self.freq = 1

class DLL:
    def __init__(self):
        self.head = DLLNode(None, None)
        self.tail = DLLNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    
    def insertAtHead(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
        self.size += 1
    
    def popTail(self):
        tail = self.tail.prev
        self.removeNode(tail)
        return tail
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = collections.defaultdict(DLLNode)
        self.freqTable = collections.defaultdict(DLL)
        self.capacity = capacity
        self.minFrequency = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        else:
            self.updateCache(self.cache[key], key, self.cache[key].value)
            return self.cache[key].value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
            return
        if key in self.cache:
            self.updateCache(self.cache[key], key, value)
        else:
            
            if self.capacity == len(self.cache):
                prevTail = self.freqTable[self.minFrequency].popTail()
                del self.cache[prevTail.key]
            node = DLLNode(key, value)
            self.cache[key] = node
            self.freqTable[1].insertAtHead(node)
            self.minFrequency = 1
        return 
            
    def updateCache(self, node, key, value):
        node.value = value
        prevFreq = node.freq
        node.freq += 1
        self.freqTable[prevFreq].removeNode(node)
        self.freqTable[node.freq].insertAtHead(node)
        if prevFreq == self.minFrequency and self.freqTable[prevFreq].size == 0:
            self.minFrequency += 1
        return 
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)