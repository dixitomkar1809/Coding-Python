# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
In operating systems that use paging for memory management, page replacement algorithm are needed to decide which page needs to be replaced when the new page comes in. Whenever a new page is referred and is not present in memory, the page fault occurs and Operating System replaces one of the existing pages with a newly needed page. Given a sequence of pages and memory capacity, your task is to find the number of page faults using Least Recently Used (LRU) Algorithm.
'''
from collections import defaultdict

class Page:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class PageFaults:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = Page(0, 0)
        self.tail = Page(0, 0)
        self.head.next, self.tail.prev = self.tail, self.head
        self.pageMap = defaultdict(Page)
        self.size = 0
        self.pageFaults = 0

    def addPage(self, key, value):
        page = self.pageMap.get(key, None)
        if page:
            page.value = value
            self._moveToHead(page)
        else:
            page = Page(key, value)
            self.pageMap[key] = page
            self._addPage(page)
            self.size += 1
            self.pageFaults += 1
            if self.size > self.capacity:
                tail = self._popTail()
                del self.pageMap[tail.key]
                self.size -= 1
        print('Page Faults: ', self.pageFaults)
    
    def _moveToHead(self, page):
        self._removePage(page)
        self._addPage(page)
    
    def _addPage(self, page):
        page.prev = self.head
        page.next = self.head.next
        self.head.next.prev = page
        self.head.next = page
    
    def _popTail(self):
        tail = self.tail.prev
        self._removePage(tail)
        return tail
    
    def _removePage(self, page):
        prev= page.prev
        next= page.next
        prev.next, next.prev = next, prev

    def getPage(self, key):
        page = self.pageMap.get(key, None)
        if page:
            self._moveToHead(page)
            return page
        else:
            return None

if __name__=='__main__':
    pageFaultCounter = PageFaults(4)
    pageFaultCounter.addPage(5,5)
    pageFaultCounter.addPage(0,0)
    pageFaultCounter.addPage(1,1)
    pageFaultCounter.addPage(3,3)
    pageFaultCounter.addPage(2,2)
    pageFaultCounter.addPage(4,4)
    pageFaultCounter.addPage(1,1)
    pageFaultCounter.addPage(0,0)
    pageFaultCounter.addPage(5,5)

