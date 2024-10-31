def cond_max(x, y, matrix_size, size):
    line = list()
    diag = x + y * size
    for cpt in range(matrix_size):
        if (cpt != diag):
            line.append(0)
        else:
            line.append(1)
    return line


def cond_eq(x, y, matrix_size, size, h, f):
    line = list()
    diag = x + y * size
    for cpt in range(matrix_size):
        if (cpt == x - 1 + y * size or cpt == x + 1 + y * size or cpt ==
                x + (y - 1) * size or cpt == x + (y + 1) * size):
            line.append(int(1 / h))
        elif (cpt == x + y * size):
            line.append(int(- 4 / h))
        else:
            line.append(0)
    return line


def swap_lines(matrix, i, j):
    temp = matrix[i]
    matrix[i] = matrix[j]
    matrix[j] = temp


def find_max(matrix, j):
    n = len(matrix)
    imax = j
    for i in range(j + 1, n):
        if abs(matrix[i][j]) > abs(matrix[j][j]):
            imax = i
    return imax


def triangle(matrix, vector):
    n = len(vector)
    x = [0 for i in range(n)]
    x[n - 1] = vector[n - 1] / matrix[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        s = 0
        for j in range(i + 1, n):
            s = s + matrix[i][j] * x[j]
        x[i] = (vector[i] - s) / matrix[i][i]
    return x
