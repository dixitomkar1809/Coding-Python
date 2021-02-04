class TrieNode:
    def __init__(self, char):
        self.char = char
        self.isWord = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(None)

if __name__=="__main__":
    wordList = ["mouse", "moneypot", "mousepad", "mobile", "monitor"]
    trie = Trie()
    root = trie.root
    for word in wordList:
        curr = root
        for char in word:
            if char.lower() not in curr.children:
                curr.children[char.lower()] = TrieNode(char.lower())
            curr = curr.children[char.lower()]
        curr.isWord = True
    