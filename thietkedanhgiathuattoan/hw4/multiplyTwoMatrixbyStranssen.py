# Nhân 2 ma trận bằng phương pháp stranssen.

import numpy as np
import time
import random as rd


def multiplyTwoMatrixbyStranssen(A, B):
    n = len(A)
    if n == 1:
        return A * B
    else:
        A11 = A[:n // 2, :n // 2]
        A12 = A[:n // 2, n // 2:]
        A21 = A[n // 2:, :n // 2]
        A22 = A[n // 2:, n // 2:]
        B11 = B[:n // 2, :n // 2]
        B12 = B[:n // 2, n // 2:]
        B21 = B[n // 2:, :n // 2]
        B22 = B[n // 2:, n // 2:]
        M1 = multiplyTwoMatrixbyStranssen(A11 + A22, B11 + B22)
        M2 = multiplyTwoMatrixbyStranssen(A21 + A22, B11)
        M3 = multiplyTwoMatrixbyStranssen(A11, B12 - B22)
        M4 = multiplyTwoMatrixbyStranssen(A22, B21 - B11)
        M5 = multiplyTwoMatrixbyStranssen(A11 + A12, B22)
        M6 = multiplyTwoMatrixbyStranssen(A21 - A11, B11 + B12)
        M7 = multiplyTwoMatrixbyStranssen(A12 - A22, B21 + B22)
        C11 = M1 + M4 - M5 + M7
        C12 = M3 + M5
        C21 = M2 + M4
        C22 = M1 - M2 + M3 + M6
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
        return C


def test_multiplyTwoMatrixbyStranssen(n):
    A = np.array([[rd.randint(0, 100) for i in range(n)] for j in range(n)])
    B = np.array([[rd.randint(0, 100) for i in range(n)] for j in range(n)])
    start_time = time.time()
    multiplyTwoMatrixbyStranssen(A, B)
    end_time = time.time()
    return end_time - start_time


# Đo thời gian thực hiện nhân 2 ma trận với các kích thước khác nhau
# và vẽ đồ thị thời gian thực hiện theo kích thước ma trận
import matplotlib.pyplot as plt

arr = []
for j in range(8):
    i = pow(2, j)
    x = test_multiplyTwoMatrixbyStranssen(i)
    arr.append(x)

plt.plot(arr)
plt.ylabel('Time')
plt.xlabel('Data size')
plt.show()
