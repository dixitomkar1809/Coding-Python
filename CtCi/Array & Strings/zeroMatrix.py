# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Zero Matrix

# Time Complexity - O(n*m)
def zeroMatrix(matrix):
    pass
    value = float('inf')
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                for k in range(len(matrix[0])):
                    matrix[i][k]=value if matrix[i][k] != 0 else 0
                for k in range(len(matrix)):
                    matrix[k][j]=value if matrix[k][j] != 0 else 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==value:
                matrix[i][j]=0
    return matrix

if __name__=="__main__":
    # matrix = [
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [1, 1, 1]
    # ]
    matrix = [
        [0,1,2,0],
        [3,4,5,2],
        [1,3,1,5]
    ]
    print(zeroMatrix(matrix))