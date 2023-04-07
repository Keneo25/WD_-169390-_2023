import numpy as np


def fun(vec_length):
    main_axis = np.arange(vec_length, 0, -1)
    vec = np.diag(main_axis)
    return vec


if __name__ == '__main__':
    vec_leng = int(input("Podaj dlugosc wektora: "))
    n = fun(vec_leng)
    print(n)
