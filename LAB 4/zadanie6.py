import numpy as np


if __name__ == '__main__':
    n = np.zeros((6, 6), dtype=str)
    malina = "malina"
    lizak = "lizak"
    mkzab = "mkzab"

    malina_ar = np.fromiter(malina, dtype='S1')
    malina_ar.resize((1, 6))

    lizak_ar = np.fromiter(lizak, dtype='S1')
    lizak_ar.resize((1, 6))

    mkzab_ar = np.fromiter(mkzab, dtype='S1')
    mkzab_ar.resize((1, 6))

    n[2:3] = lizak_ar
    n[:, 0] = malina_ar
    np.fill_diagonal(n, mkzab_ar)

    print(n)