# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given three increasingly sorted arrays A, B, C of sizes N1, N2, and N3 respectively, you need to print all common elements in these arrays.
'''
class Solution:
    def commonElements(self, a1, a2, a3):
        n1 = len(a1)
        n2 = len(a2)
        n3 = len(a3)
        i, j, k = 0, 0, 0
        commonElements = []
        while i < n1 and j < n2 and k < n3:
            if a1[i]==a2[j] and a2[j]==a3[k]:
                commonElements.append(a1[i])
                i += 1
                j += 1
                k += 1
            elif a1[i] < a2[j]:
                i += 1
            elif a2[j] < a3[k]:
                j += 1
            else:
                k += 1 
        return commonElements

if __name__=='__main__':
    a1 = [1, 5, 10, 20, 40, 80] 
    a2 = [6, 7, 20, 80, 100] 
    a3 = [3, 4, 15, 20, 30, 70, 80, 120] 
    sol = Solution()
    print(sol.commonElements(a1, a2, a3))