# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
There are two parallel roads, each containing N and M buckets, respectively. Each bucket may contain some balls. The buckets on both roads are kept in such a way that they are sorted according to the number of balls in them. Geek starts from the end of the road which has the bucket with a lower number of balls(i.e. if buckets are sorted in increasing order, then geek will start from the left side of the road).
The geek can change the road only at the point of intersection(which means, buckets with the same number of balls on two roads). Now you need to help Geek to collect the maximum number of balls.
'''

class Solution:
    def collectBalls(self, a, b, n, m):
        i, j, res = 0,0,0
        first, second = 0,0
        while i < n and j < m:
            if a[i] < b[j]:
                first += a[i]
                i+=1
            elif a[i] > b[j]:
                second += b[j]
                j+=1
            else:
                res += max(first, second) + a[i]
                first = 0
                second = 0
                temp = a[i]
                i+=1
                temp = b[j]
                j+=1
                while i<n and a[i]==temp:
                    res += a[i]
                    i+=1
                while j<m and b[j]==temp:
                    res += b[j]
                    j+=1
        while i < n:
            first += a[i]
            i += 1
        while j < m:
            second += b[j]
            j += 1
        res += max(first, second)
        return res

if __name__=='__main__':
    sol = Solution()
    a = [1,4,5,6,8]
    b = [2,3,4,6,9]
    print(sol.collectBalls(a, b, len(a), len(b)))