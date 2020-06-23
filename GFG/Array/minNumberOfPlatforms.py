# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given arrival and departure times of all trains that reach a railway station. Your task is to find the minimum number of platforms required for the railway station so that no train waits.
'''

class Solution:
    def minNumberOfPlatforms(self, arrivals, departures):
        for i in range(len(arrivals)):
            arrivals[i] = int(arrivals[i])
            departures[i] = int(departures[i])
        departures.sort()
        arrivals.sort()
        i = 0
        j = 0
        platform = 0
        currMax = 0
        while i<len(arrivals) and j < len(departures):
            if arrivals[i] <= departures[j]:
                platform += 1
                i += 1
            elif arrivals[i] > departures[j]:
                platform -= 1
                j += 1
            if currMax < platform:
                currMax = platform
        return currMax

if __name__=='__main__':
    sol = Solution()
    arrivals = ['0900',  '0940', '0950',  '1100', '1500', '1800']
    departures = ['0910', '1200', '1120', '1130', '1900', '2000']
    print(sol.minNumberOfPlatforms(arrivals, departures))
    arrivals = ['0900', '1100', '1235']
    departures = ['1000', '1200', '1240']
    print(sol.minNumberOfPlatforms(arrivals, departures))