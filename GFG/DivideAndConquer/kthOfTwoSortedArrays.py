# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two sorted arrays A and B of size M and N respectively and an element k. The task is to find the element that would be at the k’th position of the final sorted array.
'''

# Time Complexity: O(log(m+n))

class Solution:
    def findKth(self, a, b, m, n, k):
        if m > n:
            return self.findKth(b, a, n, m, k)
        if m == 0 and n > 0:
            return b[k-1]
        if k == 1:
            return min(a[0], b[0])
        i = min(m, int(k/2))
        j = min(n, int(k/2))
        if a[i-1] < b[j-1]:
            return self.findKth(a[i:], b, m-i, j, k-i)
        else:
            return self.findKth(a, b[j:], m, n-j, k-j)
        

if __name__=='__main__':
    sol = Solution()
    a = [2,3,6,7,9]
    b = [1,4,8,10]
    k = 5
    print(sol.findKth(a, b, len(a), len(b), k))