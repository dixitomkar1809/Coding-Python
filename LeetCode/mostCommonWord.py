# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/most-common-word/

# Time Complexity: O(n + m) n is chars in input, m is chars in banned words

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        lowerCaseCleanString = ''
        for char in paragraph:
                if char.isalnum():
                    lowerCaseCleanString += char.lower()
                else:
                    lowerCaseCleanString += ' '
        lowerCaseCleanStringList = lowerCaseCleanString.split(' ')
        bannedWordsSet = {}
        for word in banned:
            bannedWordsSet[word] = 1
        counts = []
        for word in lowerCaseCleanStringList:
            if word and word not in bannedWordsSet:
                counts.append(word)
        return (collections.Counter(counts).most_common(1)[0][0])