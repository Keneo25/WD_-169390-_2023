import numpy as np


def fib(n):
    if n == 1 or n == 0:
        return n
    return fib(n - 1) + fib(n - 2)


def fun():
    n = np.arange(25)   # 5 * 5
    for k in range(0, len(n)):
        n[k] = fib(k + 1)
    return n.reshape((5, 5))


if __name__ == '__main__':
    print(fun())