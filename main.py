def zad1():
    a = input("Wpisz jakies zdanie program policzy spacje:")
    print(a.count(" "));


def zad2():
    a = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. " \
        "Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. " \
        "Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. " \
        "Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum," \
        "a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker"
    k = a.split()
    print(k)
    print(type(a))


def zad3():
     x = 2
     a = 4;
     print(a == x) #return false poniewaz nie sa sobie rowne
     print(a!=x) #return true poniewaz sa rozne
     print(a >= x) # return true poniewaz a jest wieksze
     print(a <= x)  # return false poniewaz a nie jest mniejsze ani rowne

def zad4():
    x = eval(input("Podaj liczbe calkowita: ")) #musi byc eval
    if x < 0:
        print("Wynik: ",x*-1)
    else:
        print("wynik: ",x)


def zad5():
    a = eval(input("Podaj a: "))
    b = eval(input("Podaj b: "))
    c = eval(input("Podaj c: "))
    if a >= 0 and a <=10:
        print("A zawiera sie w przedziale od 0 do 10")
        if a >b or b >c:
            print("a jest wieksze od b badz b jest wieksze od c")
    else:
        print("A NIE zawiera sie w przedziale od 0 do 10")


def zad6():
      for i in range(0,51):
          if i % 5 ==0:
              print("\n",i)

def zad7():
    x = eval(input("Podaj ile liczb: "))
    for i in  range(0,x):
        a = eval(input("Podaj "+ str(i+1) +" liczbe: "))
        print("Kwadrat "+str(a)+" =", a*a)



def zad9():

    list = []
    while list!=0:
        x = input("Podaj wartosc: ")
        if x.isdigit():
            list.append(x)
            print(list)
        elif x == "end":
            print(list)
            break
def zad10():
    a = eval(input("Podaj liczbe: "))
    if a >0 and a<=10:
       if a == 1:
        print("A")
       elif a==2:
        print("AA")
       elif a == 3:
        print("AAA")
       elif a == 4:
        print("AAAA")
       elif a == 5:
        print("AAAAA")
       elif a == 6:
        print("AAAAAA")
       elif a == 7:
        print("AAAAAAA")
       elif a == 8:
        print("AAAAAAAA")
       elif a == 9:
        print("AAAAAAAAA")
       elif a == 10:
        print("AAAAAAAAAA")




zad9()
print("\n")
