# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
There is one meeting room in a firm. There are N meetings in the form of (S[i], F[i]) where S[i] is start time of meeting i and F[i] is finish time of meeting i.
'''

from operator import itemgetter

class Solution:
    def getNMeetingsInARoom(self, start, end):
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
    timings = sorted([[1,2], [3,4], [0, 6], [5,7], [8,9], [5,9]], key=itemgetter(1))
    sol = Solution()
    start = []
    end = []
    for item in timings:
        start.append(item[0])
        end.append(item[1])
    print(sol.getNMeetingsInARoom(start, end), 'Meetings')