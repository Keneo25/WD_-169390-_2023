import pandas as pd


def zad_a(df):
    gp = df[df["Liczba"] > 1000]
    print(gp)


def zad_b(df):
    gp = df[df["Imie"] == "ŁUKASZ"]
    print(gp)


def zad_c(df):
    gp = df.sum()
    print(gp["Liczba"])


def zad_d(df):
    gp = df.groupby(df["Rok"]).sum()
    print(gp)


def zad_e(df):
    filt = df.Liczba <= 2005
    filt2 = df.Liczba >= 2000
    gp = df[filt & filt2]
    print(gp)


def zad_f(df):
    filt = df.Plec == "M"
    filt2 = df.Plec == "K"
    ll = df[filt].sum()
    ll2 = df[filt2].sum()
    print(ll.Liczba)
    print(ll2.Liczba)


def zad_g(df):
    male = df[df.Plec == "M"]
    female = df[df.Plec == "K"]

    g1 = male.groupby(df.Imie).sum()
    g2 = female.groupby(df.Imie).sum()
    print(g1.Liczba.idxmax())
    print(g2.Liczba.idxmax())


def zad_h(df):
    years = df.groupby([df.Rok, df.Imie]).sum().sort_values(by=df.Liczba)
    print(years)


if __name__ == '__main__':
    data = pd.read_excel("datasets_cw6/imiona.xlsx")
    # zad_a(df)
    # zad_b(data)
    # zad_c(df)
    # zad_d(df)
    # zad_e(data)
    # zad_f(data)
    # zad_g(data)
    zad_h(data)



