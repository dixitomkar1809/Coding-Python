# Author: Omkar Dixit
# Email: omedxt@gmail.com

# Link: https://leetcode.com/problems/break-a-palindrome/

# Time Complexity: O(n)

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ''
        index = -1
        for i, char in enumerate(palindrome.lower()):
            if char != 'a' and (len(palindrome) % 2 == 0 or (len(palindrome) % 2 != 0 and i != int(len(palindrome)/2))):
                index = i
                break
        if index > -1:
            palindrome = palindrome[:index] + 'a' + palindrome[index + 1:]
        else:
            palindrome = palindrome[:len(palindrome)-1] + 'b'
        return palindrome
                