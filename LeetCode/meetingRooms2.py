# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/meeting-rooms-ii/

# Time Complexity: O(nLogn)

import heapq

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if not intervals:
            return 0
        rooms = []
        intervals.sort(key=lambda x: x[0])
        heapq.heappush(rooms, intervals[0][1])
        for i in range(1, len(intervals)):
            if rooms[0] <= intervals[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals[i][1])
        return len(rooms)