# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/search-suggestions-system/

# Time Complexity: O(n) n is chars of products

class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(None)
        
class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        root = trie.root
        self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for word in products:
            curr = root
            for char in word:
                if char.lower() not in curr.children:
                    curr.children[char.lower()] = TrieNode(char.lower())
                curr = curr.children[char.lower()]
            curr.isWord = True
        solution = []
        prefix = ''
        for char in searchWord:
            prefix += char
            temp = self.getSuggestions(root, prefix)
            solution.append(temp)
        return solution
    
    def getSuggestions(self, root, prefix):
        result = []
        curr = root
        for char in prefix:
            if char not in curr.children:
                return result
            curr = curr.children[char]
        self.dfs(curr, prefix, result)
        print(result)
        return result
    
    def dfs(self, curr, word, result):
        if len(result) == 3:
            return 
        if curr.isWord:
            result.append(word)
        for char in self.alphabets:
            if char in curr.children:
                self.dfs(curr.children[char], word+char, result)
        