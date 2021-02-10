# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/analyze-user-website-visit-pattern/

import collections
class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        userHistory = collections.defaultdict(list)
        browsingSequence = collections.defaultdict(int)
        allInfo = []
        for time, user, website in zip(timestamp, username, website):
            allInfo.append((time, user, website))
        allInfo.sort(key=lambda x: x[0])
        for i in range(len(allInfo)):
            userHistory[allInfo[i][1]].append(allInfo[i][2])
        print(userHistory)
        self.put3Sequence(userHistory, browsingSequence)
        sol = []
        maxCount = max(browsingSequence.values())
        for sequence in sorted(browsingSequence.keys()):
            if browsingSequence[sequence] == maxCount:
                sol.append(list(sequence))
        sol.sort()
        print(sol)
        return sol[0]
    
    def put3Sequence(self, userHistory, browsingSequence):
        for user in userHistory:
            websitesVisited = set(combinations(userHistory[user], 3))
            for seq in websitesVisited:
                browsingSequence[seq] += 1
