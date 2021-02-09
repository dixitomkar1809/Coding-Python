# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/design-in-memory-file-system/

import collections
class TrieNode():
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isFile = False
        self.content = ''

class FileSystem(object):

    def __init__(self):
        self.root = TrieNode()

    # Time Complexity: O(m + n + klogk) k log k for the sort rest for the __add
    def ls(self, path):
        """
        :type path: str
        :rtype: List[str]
        """
        if path == '/':
            return sorted(list(self.root.children.keys()))
        pathList = path.split('/')
        node = self.__add(pathList)
        if node.isFile:
            return [pathList[-1]]
        return sorted(list(node.children.keys()))
    
    # Time Complexity: O(m + n) m would be the length of stirng and n would be the levels on the trie
    def __add(self, pathList):
        node = self.root
        for dir in pathList[1:]:
            node = node.children[dir]
        return node
    
    def mkdir(self, path):
        """
        :type path: str
        :rtype: None
        """
        self.__add(path.split('/'))
    
    # Time Complexity: O(m + n) for the __add
    def addContentToFile(self, filePath, content):
        """
        :type filePath: str
        :type content: str
        :rtype: None
        """
        node = self.__add(filePath.split('/'))
        node.isFile = True
        if node.content != '':
            node.content += content
        else:
            node.content = content.strip()
        return None
    
    # Time Complexity: O(m + n) for the __add
    def readContentFromFile(self, filePath):
        """
        :type filePath: str
        :rtype: str
        """
        return self.__add(filePath.split('/')).content
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)