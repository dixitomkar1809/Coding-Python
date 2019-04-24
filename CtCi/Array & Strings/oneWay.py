# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# One Way

from collections import Counter
import sys

def oneWay(str1, str2):
    if len(str1) > len(str2):
        if len(Counter(str1)-Counter(str2))==1:
            return True
        return False
    else:
        if len(Counter(str2)-Counter(str1))==1:
            return True
        return False

if __name__=="__main__":
    if len(sys.argv)<3:
        print("Strings not read...")
    else:
        str1 = str(sys.argv[1])
        str2 = str(sys.argv[2])
        print(oneWay(str1, str2))