matrix1 = [[6, 3, 5], [4, 7, 6], [1, 1, 7]]
matrix2 = [[1, 0, 0], [4, 4, 8], [2, 2, 6]]

for i in range(0, len(matrix1)):
    for j in range(0, len(matrix1)):
        print(matrix1[j][i] + matrix2[j][i])