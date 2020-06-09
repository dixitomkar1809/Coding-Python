# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an string in roman no format (s)  your task is to convert it to integer .
'''

class Solution:
    def romanToInt(self, string):
        res = 0
        i = 0
        while i < len(string):
            s1 = self.value(string[i])
            if i+1 < len(string):
                s2 = self.value(string[i+1])
                if s1 >= s2:
                    res = res + s1
                    i+=1
                else:
                    res = res + s2 - s1
                    i += 2
            else:
                res += s1
                i += 1
        return res
    
    def value(self, char):
        if (char == 'I'): 
            return 1
        if (char == 'V'): 
            return 5
        if (char == 'X'): 
            return 10
        return -1

if __name__=='__main__':
    string = 'VII'
    sol = Solution()
    print(sol.romanToInt(string))