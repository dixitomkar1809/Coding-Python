# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given an expression string exp. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in exp.
For example, the program should print 'balanced' for exp = “[()]{}{[()()]()}” and 'not balanced' for exp = “[(])”
'''

# Time Complexity: O(n)

class Solution:
    def parenthesisChecker(self, parenthesis):
        stack = []
        for char in parenthesis:
            if self.isOpening(char):
                stack.append(char)
            else:
                if not (self.isMatching(stack.pop(), char)):
                    return False
        if stack:
            return False
        return True
    
    def isOpening(self, char):
        if char == '(':
            return True
        elif char == '[':
            return True
        elif char == '{':
            return True
        else:
            return False

    def isClosing(self, char):
        if char == ')':
            return True
        elif char == ']':
            return True
        elif char == '}':
            return True
        else:
            return False

    def isMatching(self, opening, closing):
        if closing == ')':
            return opening == '('
        elif closing == ']':
            return opening == '['
        elif closing == '}':
            return opening == '{'
        return False

if __name__=="__main__":
    str = "[({)]"
    sol = Solution()
    print(sol.parenthesisChecker(list(str)))
