# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# String Rotation
import sys

def isSubstring(s1, s2):
    for i in range(len(s2)-len(s1)+1):
        for j in range(len(s1)):
            # print(s2[i+j], s1[j])
            if s2[i+j]!=s1[j]:
                break
            if j+1==len(s1):
                print(j+1)
                return True
    return False

def stringRotation(s1, s2): 
    if len(s1)==0 and len(s2)==0:
            return True
    elif len(s1)==0 or len(s2)==0:
        return False
    elif len(s1) > len(s2):
        return False
    l = 0
    r = len(s1)-1
    while l < r:
        if self.isSubstring(s1[l:r], s2):
            break
        r-=1
    if self.isSubstring(s1[l:r], s2) and self.isSubstring(s1[r:], s2):
        return True
    return False

if __name__=="__main__":
    if len(sys.argv)<3:
        print("Strings not read")
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    print(stringRotation(s1, s2))
    # print(isSubstring(s1, s2))