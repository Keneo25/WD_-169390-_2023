
def zad1():
    a = "*" * 20
    b = "*" * 20
    c = "*" * 20
    d = "*" * 20
    print(a)
    print(b)
    print(c)
    print(d)

def zad2():
    a = "*" * 20
    b = "*"
    c = " "
    print(a)
    print(b*1,c*16,b*1)
    print(b*1,c*16,b*1)
    print(a)


def zad3():
    a ="*"
    print(a)
    print(a*2)
    print(a*3)
    print(a*4)



def zad4():
    a = (512-282)/(47*48+5)
    print(a)


def zad5():
    x =7
    print(x,"---",x*2,"---",x*3,"---",x*4,"---",x*5)


def zad6():
    i = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. \n" \
            "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n" \
            " when an unknown printer took a galley of type and scrambled it to make a type \n" \
            "specimen book. It has survived not only five centuries, but also the leap into \n" \
            "electronic typesetting, remaining essentially unchanged. It was popularised in the \n" \
            " 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more \n" \
            "recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"
    print(i)

def zad7():
    a = eval(input("Wpisz wartosc a"))
    b = eval(input("Wpisz wartosc b"))
    c =a *b
    print("Mnozenie rowna sie: ",c)




def zad8():
    kilo = eval(input("Podaj swoja wage w kg"))
    funty = kilo *2.2
    print("Twoja waga w funtach wynosi: ",funty)




zad1()
print("\n")
zad2()
print("\n")
zad3()
print("\n")
zad4()
print("\n")
zad5()
print("\n")
zad6()
print("\n")
zad7()
print("\n")
zad8()