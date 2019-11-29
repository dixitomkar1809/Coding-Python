class TrieNode:
    def __init__(self, sentence, times):
        self.sentence = sentence
        self.times = times
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode(None, None)

