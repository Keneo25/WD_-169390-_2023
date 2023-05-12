import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def zad1():
    df = pd.read_excel('imiona.xlsx')
    df_of_k = df[df['imie'].str[0]=='K']
    df_unique = df_of_k['imie'].unique()
    print(len(df_unique))




def zad2():
    df = pd.read_excel('imiona.xlsx')
    result = df.groupby(['Imie','Plec'])['Liczba'].sum().reset_index()
    k = result[result['Plec'] == 'K']
    k_max = k['Liczba'].idmax()
    k_imie = k.ilosc[k_max]['Imie']
    print("Najpopularniejsze imie żeńskie",k_imie)

def zad3():
    df = pd.read_excel('imiona.xlsx')
    data = df[(df['Rok'] >= 2010) (df['Rok'] <= 2015)]
    data_group = data.groupby('Plec')['Liczba'].sum()
    data_group.plot.bar()

    sns.barplot(data=data,x ='Plec',y='Liczba')
    plt.show()
    print()
