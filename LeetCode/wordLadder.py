# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Time Complexity: O(M*M*N) N is number of words, M is len of word

# Link: https://leetcode.com/problems/word-ladder/

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        visited = {}
        for word in wordList:
            visited[word] = False
        queue = [([beginWord], visited)]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        while queue:
            currWordList, currVisited = queue.pop(0)
            if currWordList[-1] == endWord:
                return len(currWordList)
            for i in range(len(currWordList[-1])):
                for letter in letters:
                    tempWord = currWordList[-1][:i] + letter + currWordList[-1][i+1:]
                    if tempWord in currVisited and currVisited[tempWord] == False:
                        currVisited[tempWord] = True
                        queue.append((currWordList + [tempWord], currVisited))
        return 0