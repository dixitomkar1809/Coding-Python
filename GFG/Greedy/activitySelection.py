# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
'''

from operator import itemgetter

class Solution:
    def getMaxNumberOfActivities(self, start, end):
        i = 0
        print(start[i], end[i])
        count = 1
        for j in range(len(start)):
            if start[j] >= end[i]:
                print(start[j], end[j])
                i = j
                count += 1
        return count

if __name__=='__main__':
    timings = sorted([[1,2], [2,6], [3,4], [5,7], [8,9], [5,9]], key=itemgetter(1))
    sol = Solution()
    start = []
    end = []
    for item in timings:
        start.append(item[0])
        end.append(item[1])
    print(sol.getMaxNumberOfActivities(start, end), 'Activities')