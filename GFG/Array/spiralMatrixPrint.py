# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.
'''

# Time Complexity: O(R*C)

class Solution:
    def spitalMatrixPrint(self, matrix, m, n):
        k = 0
        l = 0
        result = []
        while k < m and l < n:
            for i in range(l, n):
                result.append(matrix[k][i])
            k+=1
            for i in range(k, m):
                result.append(matrix[i][n-1])
            n-=1
            if k < m:
                for i in range(n-1, l-1, -1):
                    result.append(matrix[m-1][i])
                m-=1
                for i in range(m-1, k-1, -1):
                    result.append(matrix[i][l])
                l+=1
        return result

if __name__=='__main__':
    sol = Solution()
    print(sol.spitalMatrixPrint([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]], 3, 6))
    print(sol.spitalMatrixPrint([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4, 4))