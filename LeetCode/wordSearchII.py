# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/word-search-ii/

class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.isWord = False
        self.word = ''
        self.children = {}
        
class Trie:
    def __init__(self):
        self.root = TrieNode(None)

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        root = trie.root
        self.board = board
        for word in words:
            curr = root
            for char in word:
                if char.lower() not in curr.children:
                    curr.children[char.lower()] = TrieNode(char.lower())
                curr = curr.children[char.lower()]
            curr.isWord = True
            curr.word = word
        self.solution = []
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                char = self.board[row][col]
                if char in root.children:
                    self.dfs(row, col, root)
        return list(set(self.solution))
    
    def dfs(self, row, col, parent):
        char = self.board[row][col]
        currNode = parent.children[char]
        if currNode.isWord:
            self.solution.append(currNode.word)
        self.board[row][col] = '#'
        for (rowDirection, colDirection) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            newRow = row + rowDirection
            newCol = col + colDirection
            if self.isValid(newRow, newCol, currNode):
                self.dfs(newRow, newCol, currNode)
        self.board[row][col] = char
        
    def isValid(self, row, col, parent):
        return row >= 0 and row < len(self.board) and col >= 0 and col < len(self.board[0]) and self.board[row][col] in parent.children