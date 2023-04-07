import numpy as np


def fun(number, n):
    return np.logspace(1, stop=n, num=n, base=number, dtype=int)


if __name__ == '__main__':
    print(fun(3, 4))