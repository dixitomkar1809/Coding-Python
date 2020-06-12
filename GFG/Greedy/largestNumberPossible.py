# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given two numbers 'N' and 'S' , find the largest number that can be formed with 'N' digits and whose sum of digits should be equals to 'S'.
'''

class Solution:
    def getLargestPossible(self, s, n):
        if s==0:
            if n == 1:
                print("Largest Possible is 0")
                return 
            else:
                print("Not Possible")
                return 
        if s > 9 * n:
            print("Not Possible")
            return
        number = [0] * n
        for i in range(n):
            if s >= 9:
                number[i] = '9'
                s -= 9
            else:
                number[i] = str(s)
                s=0
        print('Largest Number is ', ''.join(number))
        return 

if __name__=='__main__':
    sol = Solution()
    sol.getLargestPossible(20,3)
