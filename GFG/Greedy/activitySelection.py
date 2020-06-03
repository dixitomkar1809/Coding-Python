# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
'''


class Solution:
    def getMaxNumberOfActivities(self, start, end):
        i = 0
        count = 1
        for j in range(len(start)):
            if start[j] >= end[i]:
                i = j
                count += 1
        return count

if __name__=='__main__':
    timings = [[1,2], [3,4], [2,6], [5,7], [8,9], [5,9]]
    sol = Solution()
    start = []
    end = []
    for item in timings:
        start.append(item[0])
        end.append(item[1])
    print(sol.getMaxNumberOfActivities(start, end))