# Author: Omkar Dixit
# Email: ond170030@utdallas.edu

# Rotate Matrix

import sys

def rotateMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()
    return matrix


if __name__=="__main__":
    # matrix = [
    #     [1, -2, -6],
    #     [0, 3, 7],
    #     [1, -2, 5]
    # ]
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # print("Rotating {}".format(matrix))
    # print("Done")
    print(rotateMatrix(matrix))