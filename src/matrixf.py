from src import mathUtils as u


def matrixCreate(size, A_matrix, h, f):
    matrix_size = size * size
    for y in range(0, size):
        for x in range(0, size):
            if (y == 0 or y == size - 1 or x == 0 or x == size - 1):
                A_matrix.append(u.cond_max(x, y, matrix_size, size))
            else:
                A_matrix.append(
                    u.cond_eq(
                        x,
                        y,
                        matrix_size,
                        size,
                        h,
                        f))


def matrix_calc(matrix, i, j, coeff):
    if type(matrix[0]) != list:
        matrix[i] = matrix[i] + coeff * matrix[j]
    else:
        n = len(matrix[0])
        for k in range(n):
            matrix[i][k] = matrix[i][k] + coeff * matrix[j][k]


def matrixPrint(size, A_matrix):
    matrix_size = size * size
    for line in A_matrix:
        i = 0
        for j in line:
            i += 1
            if (i < matrix_size):
                print("%d\t" % j, end="")
            else:
                print("%d" % j)
