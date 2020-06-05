# Author: Omkar Dixit
# Email: omedxt@gmail.com

'''
Given a string s, recursively remove adjacent duplicate characters from the string s. The output string should not have any adjacent duplicates.
'''
# Time Complexity: O(n)
class Solution:
    def removeDups(self, s, lastRemoved):
        if len(s) == 0 or len(s) == 1:
            return s
        if s[0] == s[1]:
            lastRemoved = ord(s[0])
            while len(s) > 1 and s[0] == s[1]:
                s = s[1:]
            s = s[1:]
            return self.removeDups(s, lastRemoved)
        rem_str = self.removeDups(s[1:], lastRemoved)
        if len(rem_str) != 0 and rem_str[0] == s[0]:
            lastRemoved = ord(s[0])
            return rem_str[1:]
        if len(rem_str) == 0 and lastRemoved==ord(s[0]):
            return rem_str
        return s[0] + rem_str

if __name__ == '__main__':
    str1 = "geeksforgeeg"
    str2 = "azxxxzy"
    str3 = "caaabbbaac"
    str4 = "gghhg"
    str5 = "aaaacddddcappp"
    str6 = "aaaaaaaaaa"
    str7 = "qpaaaaadaaaaadprq"
    str8 = "acaaabbbacdddd"
    sol = Solution()
    print(sol.removeDups(str1, 0))
    print(sol.removeDups(str2, 0))
    print(sol.removeDups(str3, 0))
    print(sol.removeDups(str4, 0))
    print(sol.removeDups(str5, 0))
    print(sol.removeDups(str6, 0))
    print(sol.removeDups(str7, 0))
    print(sol.removeDups(str8, 0))