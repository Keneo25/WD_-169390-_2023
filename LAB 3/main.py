import random


#ZADANIE 1

def funkcja_montonicznosc(a,b):
        if(a>0):
            print("Funkcja jest rosnąca")
        elif(a<0):
            print("Funkcja jest malejąca")
        elif(a==0):
            print("Funckaj jest stala")




def monotonicznosc():
    a = eval(input("Podaj a: "))
    b = eval(input("Podaj a: "))
    print(a,"x","+",b)
    funkcja_montonicznosc(a,b)




#
# monotonicznosc()



#ZADANIE 2

def funcja_rownolegle(a1,b1,a2,b2):
    if(a1 == a2):
        print("Funcje sa rownolegle")
    elif(a1 * a2 == -1):
        print("Funcje sa prostopadle")
    else:
        print("Niewlasciwy wynik")






def rownolegle():
    print("Sprawdzamy czy funcje sa rownolegle \n")
    print("Podaj piwerwsza funcje: ")
    a1 =eval(input("Podaj a: "))
    b1 =eval(input("Podaj b: "))
    print("Podaj druga funcje: ")
    a2 = eval(input("Podaj a: "))
    b2 = eval(input("Podaj b: "))
    funcja_rownolegle(a1,b1,a2,b2)





# rownolegle()



# ZADANIE 3

def funkcja_pitagoras(a =9,b=5):
    print(a)
    print(b)
    a = a*a
    b =b*b
    c = a+b
    print(a,"^2 +",b,"^2 =",c)




def pitagoras():
    funkcja_pitagoras(2,5)




# pitagoras()


# ZADANIE 4

def funkcja_ciag(a=1,ile=10,r=1):
    zmienna = 0
    for i in range(a,ile,r):
        zmienna= zmienna + r

    print(zmienna)






def ciag():
    funkcja_ciag(1,10,1)



   # ciag()


# ZADANIE 5
# def dodaj_znak(string1):
#     x = string1.replace(".","!")
#     print(x)
#
#
#
#
#
#
# def znak():
#     a =["audi.","bmw.","mercedes."]
#     dodaj_znak(a)
#
#
#
#
#
#
#
# znak()



# ZADANIE 6


def guess_the_number():
    x = random.randint(1, 10)
    print(x)







guess_the_number()

