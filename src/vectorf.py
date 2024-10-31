from src import mathUtils as u
from src import matrixf as m


def vectorCreate(size, a, b, X_vector, const_f):
    for j in range(size):
        for i in range(size):
            if (i == a and j == b):
                X_vector.append(const_f)
            else:
                X_vector.append(0)


def vectorCalc(A_matrix, X_vector):
    global X_res
    matrix = A_matrix
    vector = X_vector
    n = len(matrix)
    i = 0
    for i in range(n - 1):
        pivot = u.find_max(matrix, i)
        u.swap_lines(matrix, i, pivot)
        u.swap_lines(vector, i, pivot)
        for k in range(i + 1, n):
            x = float(matrix[k][i] / matrix[i][i])
            m.matrix_calc(matrix, k, i, -x)
            m.matrix_calc(vector, k, i, -x)
    X_res = u.triangle(matrix, vector)


def vectorPrint(mode, a, b, size):
    if mode:
        for res in X_res:
            temp = round(res, 2) * 100
            if (temp % 10 == 5):
                temp += 1
            temp /= 100
            if (temp > -0.04 and temp < 0.01):
                temp = abs(temp)
            print('%.1f' % temp)
    else:
        temp = round(X_res[a + b * size], 3) * 100
        if (temp % 10 == 5):
            temp += 1
        temp /= 100
        if (temp > -0.04 and temp < 0.01):
            temp = abs(temp)
        print('%.1f' % temp)
