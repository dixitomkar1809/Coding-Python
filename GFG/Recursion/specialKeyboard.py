# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Imagine you have a special keyboard with the following keys: 
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed. If you can only press the keyboard for N times (with the above four keys), write a program to produce maximum numbers of A's. That is to say, the input parameter is N (No. of keys that you can press), the output is M (No. of As that you can produce).
'''

class Solution:
    def specialKeyboard(self, N):
        if N < 7:
            return N
        maxi = 0
        for i in range(N-3, 0, -1):
            curr = (N-i-1) * self.specialKeyboard(i)
            if curr > maxi:
                maxi = curr
        return maxi

if __name__=='__main__':
    N = 20 
    sol = Solution()
    print(sol.specialKeyboard(N))