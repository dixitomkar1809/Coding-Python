# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.
'''

# Time Complexity = O(n)

class Solution:
    def nextGreaterElement(self, arr):
        stack = [arr[0]]
        s = [-1] * len(arr)
        for i in range(1, len(arr)):
            next = arr[i]
            if stack:
                element = stack.pop()
                while next > element:
                    print(element ,"---", next)
                    if not stack: break
                    element = stack.pop()
                if next < element:
                    stack.append(element)
            stack.append(next)
        while stack:
            print(stack.pop(), "---", -1)
        

if __name__=="__main__":
    arr = [11,13,21,3]
    sol = Solution()
    sol.nextGreaterElement(arr)
