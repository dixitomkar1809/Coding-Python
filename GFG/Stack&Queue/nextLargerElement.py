# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array A of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array. If no such element exists, output -1 
'''

# Time Complexity: O(n)

class Solution():
    def nextLargerElement(self, arr):
        stack = [0]
        s = [-1] * len(arr)
        for i in range(1, len(arr)):
            next = arr[i]
            if stack:
                j = stack.pop()
                element = arr[j]
                while next > element:
                    s[j] = next
                    if not stack: break
                    j = stack.pop()
                    element = arr[j]
                if next < element:
                    stack.append(j)
            stack.append(i)
        while stack:
            s[stack.pop()] = -1
        return s

if __name__=="__main__":
    arr = [1, 3, 2, 4]
    arr2 = [4, 3, 2, 1]
    sol = Solution()
    print(sol.nextLargerElement(arr2))
