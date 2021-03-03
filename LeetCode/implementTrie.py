# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: 

# Time Complexity: 

import collections
import heapq

class TrieNode:
    def __init__(self, val):
        self.char = val
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)
    
    # Time Complexity: O(n) n is number of chars in word
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        curr =  self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.isWord = True
        return

    # Time Complexity: O(n) n is number of chars in word
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            if char not in curr.children:
                return None
            curr = curr.children[char]
        if curr.isWord:
            return True
        return False
        
    # Time Complexity: O(n) n is number of chars in prefix
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        if curr:
            return True
        return False
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)