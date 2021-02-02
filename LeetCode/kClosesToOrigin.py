# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/k-closest-points-to-origin

# Time Complexity: O(nLogn)

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        distanceMap = collections.defaultdict(list)
        origin = [0, 0]
        for point in points:
            distanceMap[self.getDistance(point, origin)].append(point)
        sortedDistances = list(sorted(distanceMap.keys()))
        sol = []
        for distance in sortedDistances:
            for point in distanceMap[distance]:
                if len(sol) < K:
                    sol.append(point)
        return sol
        
    def getDistance(self, a, b):
        return ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)