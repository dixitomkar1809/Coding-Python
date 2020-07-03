# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. The Graph is represented as Adjancency Matrix, and the Matrix denotes the weight of the edegs (if it exists) else INF (1e7).
'''

# Time Complexity: O(n^3)

class Solution:
    def floydWarshall(self, dist):
        v = len(dist)
        for i in range(v):
            for j in range(v):
                for k in range(v):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

if __name__=='__main__':
    sol = Solution()
    print(sol.floydWarshall([[0, 1, 43],[1, 0, 6],[float('inf'), float('inf'), 0]]))