import numpy
import numpy as np


def fun(n):
    k = np.diag([n for _ in range(0, n)])
    k3 = np.diag([n for _ in range(0, n)], 1)
    k1 = np.zeros((n, n), dtype=int)
    k1[0] = [1,2,3,4,5]
    k1[1] = [6,5,7,8,9]
    k1[2] = [10,11,12,13,14]
    k1[3] = [15,16,17,18,19]
    k1[4] = [20,21,22,23,24]
    print(k3)
    xd = np.diag_indices(3)
    k1[xd] = 123
    print(k3[xd])
    # print(k1)


if __name__ == '__main__':
    fun(5)