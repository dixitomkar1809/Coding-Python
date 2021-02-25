# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/synonymous-sentences/

import collections

class Solution(object):
    def generateSentences(self, synonyms, text):
        """
        :type synonyms: List[List[str]]
        :type text: str
        :rtype: List[str]
        """
        graph = collections.defaultdict(dict)
        queue = collections.deque()
        ans = set()
        queue.append(text)
        for key, value in synonyms:
            graph[key][value] = 1
            graph[value][key] = 1
        while queue:
            currText = queue.popleft()
            ans.add(currText)
            words = currText.split()
            for i, word in enumerate(words):
                if word in graph:
                    for newWord in graph[word]:
                        newText = ' '.join(words[:i] + [newWord] + words[i+1:])
                        if newText not in ans:
                            queue.append(newText)
        return sorted(list(ans))