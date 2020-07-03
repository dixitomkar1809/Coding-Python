# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array of strings A[], determine if the strings can be chained together to form a circle. A
string X can be chained together with another string Y if the last character of X is same as first
character of Y. If every string of the array can be chained, it will form a circle.

For eg for the array arr[] = {"for", "geek", "rig", "kaf"} the answer will be Yes as the given strings can be chained as "for", "rig", "geek" and "kaf"
'''

from collections import defaultdict

class Solution:
    def circleOfStrings(self, arrStrings):
        graph = defaultdict(list)
        mark = [False] * 26
        inD = {}
        outD = {}
        for i in range(26):
            inD[i] = 0
            outD[i] = 0
        for i in range(len(arrStrings)):
            frontLetter = ord(arrStrings[i][0]) - ord('a')
            endLetter = ord(arrStrings[i][-1]) - ord('a')
            mark[frontLetter] = True
            mark[endLetter] = True
            inD[endLetter] += 1
            outD[frontLetter] += 1
            graph[frontLetter].append(endLetter)
        for i in range(26):
            if inD[i] != outD[i]:
                return False
        return self.isConnected(graph, mark, ord(arrStrings[0][0]) - ord('a'))

    def isConnected(self, graph, mark, s):
        visit = [False] * 26
        self.dfs(graph, s, visit)
        for i in  range(26):
            if mark[i] != visit[i]:
                return False
        return True

    def dfs(self, graph, u, visited):
        visited[u] = True
        for i in range(len(graph[u])):
            if not visited[graph[u][i]]:
                self.dfs(graph, graph[u][i], visited)

if __name__=='__main__':
    sol = Solution()
    print(sol.circleOfStrings(["ab", "bc", "cd", "de", "ed", "da"]))
    print(sol.circleOfStrings(['abc', 'bcd', 'cdf']))
    print(sol.circleOfStrings(["ab", "bc", "cd", "da"]))
