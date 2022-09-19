# Implementacja metody bisekcji, regula falsi, siecznych i stycznych
import numpy as np 
import math
import matplotlib.pyplot as plt

def f(x): # FUNKCJA
    return ((math.e)**(-2*x) - 2*x)

a = -2 # PRZEDZIAŁ FUNKCJI [a b]
b = 4
n = 4 # DOKŁADNOŚĆ WYŚWIETLANIA WYNIKU (ILOŚĆ CYFR PO ",")

# LISTY DO PLOTU
x_fig1, x_fig2, x_fig3, x_fig4 = [],[],[],[]
i_fig1, i_fig2, i_fig3, i_fig4 = [],[],[],[]

def bisek( a, b, n):
    print('Met. Bisekcji:\n')
    x = 0
    i = 1
    con = True
    while con:
        g = x
        x = (a + b) / 2
        if abs(f(x)) < 0:
            break
        else:
            if f(x) * f(a) < 0:
                b = x
            else:
                a = x
        m = x
        if g==m: # METODA SZUKA AZ UZYSKA WARUNEK POWTARZAJĄCEGO SIE WYNIKU
            break
        print(i + 1, "  x = ", x, "f(x) =", round(f(x),n))
        i+=1
        x_fig1.append(x)
        i_fig1.append(i)
    print('Rozwiązanie:  x= ', round(x, n), "f(x) =", round(f(x),n))


def fal(a, b, n):
    print('Met. Regula Falsi:\n')
    x = 0
    i = 1
    con = True 
    while con: # WARUNEK JAK W POPRZEDNIM
        g = x
        x = a-(f(a)*((b-a)/(f(b)-f(a))))
        if abs(f(x))<0:
            a = x
        else:
            b=x
        print(i, "  x = ", x, "f(x) =", round(f(x),n))
        m = x
        if m==g:
            con = False
        else:
            con = True
            i+=1
        x_fig2.append(x)
        i_fig2.append(i)
    print('Rozwiązanie:  x= ', round(x, n), "f(x) =", round(f(x),n))

def siecz(a, b, n):
    print('Met. siecznych:\n')
    x = 0
    i = 1
    con = True 
    while con: # WARUNEK JAK W POPRZEDNIM
        g = x
        x = a-(f(a)*((b-a)/(f(b)-f(a))))
        if abs(f(x))<0 and f(a)*f(x)>0:
            a = x
        else:
            b = x

        print(i, "  x = ", x, "f(x) =", round(f(x),n))
        m = x
        if m==g:
            con = False
        else:
            con = True
            i+=1
        x_fig3.append(x)
        i_fig3.append(i)
    print('Rozwiązanie:  x= ', round(x, n), "f(x) =", round(f(x),n))    

def newton(a, b, n):
    print('Met. Newtona-Raphsona:\n')
    x = (a + b) / 2 # Wybrana liczba z przedziału [a b]
    i = 1

    con = True
    while con:
        g = x
        dx = (f(x+(1/2*(b-a)))-f(x-(1/2*(b-a))))/(b-a)
        x = x - (f(x))/dx
        if abs(f(x)) < 0.0:
            break
        else:
            dx = (f(x+(1/2*(b-a)))-f(x-(1/2*(b-a))))/(b-a) # I POCHODNA Z ILORAZU RÓŻNICOWEGO
            x = x - (f(x))/dx
        print(i + 1, "  x = ", x, "f(x) =", round(f(x),n))
        m = x
        if m==g:
            con = False
        else:
            con = True
            i+=1
        x_fig4.append(x)
        i_fig4.append(i)
    print('Rozwiązanieeee:  x= ', round(x, n), "f(x) =", round(f(x),n))

if f(a) * f(b) >= 0:
    print('Test na obecnośc X0 nie jest spełniony\nWarunek: f(a) * (fb) < 0')
else:
    bisek(a, b, n)
    fal(a, b, n)
    siecz(a, b, n)
    newton(a, b, n)

plt.figure()
plt.plot(i_fig1, x_fig1, label ='Met. Bisekcji')
plt.plot(i_fig2, x_fig2, label ='Met. Regula Falsi')
plt.plot(i_fig3, x_fig3, label ='Met. Siecznych')
plt.plot(i_fig4, x_fig4, label ='Met. Newtona-Raphsona')
plt.xlabel('Liczba iteracji')
plt.ylabel('Rozwiązanie')
plt.legend()
plt.show()