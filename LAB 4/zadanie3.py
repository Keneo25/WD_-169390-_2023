import numpy as np


def fun(n):
    arr = np.arange(1, n + 1)
    for k in range(0, len(arr)):
        arr[k] = arr[k] * arr[k]
    return arr


if __name__ == '__main__':
    array = fun(int(input("Podaj liczbe n: ")))
    print(array)
    print(array.size)
