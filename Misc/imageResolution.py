# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Image Resolution

import sys

def imageResolution(file):
    with open(file, 'rb') as image:
        image.seek(163)
        a = image.read(2)
        height = (a[0]<<8) + a[1]
        a = image.read(2)
        width = (a[0] << 8) +a[1]
        return (width, height)

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("Filename not read")
    else:
        print(imageResolution(sys.argv[1]))