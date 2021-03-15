#Zad1
'''A = [1-x for x in range(1, 10)]
B = [pow(4, x) for x in range(0, 7)]
C = [x for x in B if x % 2 == 0]
print(A)
print(B)
print(C)'''
#Zad2
'''import random
lista1 = []
for x in range(1,10):
    lista1.append(random.randint(1,100))
nowa = [y for y in lista1 if y % 2 == 0]
print(lista1)
print(nowa)'''
#Zad3
'''slownik = {"Grzesiek":"szt", "Ziemniaki":"kg", "Woda":"l","Monster":"szt"}
lista = [k for k,v in slownik.items() if v == "szt"]
print(slownik)
print(lista)'''
#Zad4
'''def prostokatny(a,b,d):
    if a*a+b*b == d*d:
        return True
    else:
        return False'''
#Zad5
'''def trapez(a = 3, b = 5, h = 2):
    return ((a*b)/2)*h'''
#Zad6
'''def ciag(a=1,b=4,ile=10):
    for x in range(1,ile):
        a=a*b
    return a'''
#Zad7
'''def ciag2(* liczby):
    if len(liczby)==0:
        return 0
    else:
        iloczyn = 0
        for i in liczby:
            iloczyn += i
    return iloczyn'''
#Zad8
'''def kasa(** zakupy):
    suma = 0
    print(len(zakupy)) #ilosc produktow
    lista = [v for k, v in zakupy.items()]
    #print(lista)
    for i in lista:
        suma+=i
    return suma
#kasa(maslo=2, kielbasa= 3)'''
#Zad9