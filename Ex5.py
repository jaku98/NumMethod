# MN10 24.01.2022 r.  Zaimplementować kwadratury Newtona Cotesa rzędów 1-6
# +++ zaimplementować złożoną metodę trapezów (użytkownik definiuje ilość przedziałów) oraz ekstrapolację Richardsona (użytkownik definiuje krok)
import matplotlib.pyplot as plt
import numpy as np

def func(x):
    return 2 * (x**2) - (x * (np.e) ** (x*2))
granice_cal = (-1,1)

### METODA KWADRATURY NEWTONA COTESA rz 1-6

x_mat = []
a_mat = []
rozw = []
sigm = [[1, 1], [1, 4, 1], [1, 3, 3, 1], [7, 32, 12, 32, 7], 
       [19, 75, 50, 50, 75, 19], [41, 216, 27, 272, 27, 216, 41]]
ns = [2, 6, 8, 90, 288, 840]

for i in range(0, 6):
    a_mat.append((granice_cal[1] - granice_cal[0]) / (i + 1))
    x_mat.append(np.linspace(-1,1,i+2))
for k in range(0, len(x_mat)):
    temp = func(np.array(x_mat[k]))
    x_mat[k] = temp
for j in range(0, len(x_mat)):
    x = ((granice_cal[1] - granice_cal[0]) / ns[j]) * sum(sigm[j][s] * x_mat[j][s] for s in range(0, len(x_mat[j])))
    rozw.append(x)

print(rozw)
plt.figure()
plt.plot(rozw, 'o', label = 'Rozwiązanie kwadratury NEWTONA-COTESA')
plt.xlabel('Rząd kwadratury NEWTONA-COTESA')
plt.ylabel('Rozwiązanie')


### METODA TRAPEZOW

n = 10 # ilość przedziałów
szer = (granice_cal[1] - granice_cal[0]) / n
rozw1 = 0.0
rozw1list = []

for i in range(n):
    rozw1 += szer*(func(granice_cal[0] + szer * i)+func(granice_cal[0] + szer * (i+1)))/2
    rozw1list.append(rozw1)

print('Rozwiązanie złożoną metodę trapezów:', rozw1list)
plt.scatter([0.0]*len(rozw1list), rozw1list, label = 'Kolejne etapy obl metody trapezów', 
             color = 'red', marker = 'x')
plt.scatter(0, rozw1, label = 'Rozwiązanie złożoną metodą trapezów', 
             color = 'red', marker = 'o', )


### Ekstrapolacja Richardsona

h = 0.1 # krok
ilosc_przedz = int((granice_cal[1] - granice_cal[0]) / h)
rozw2 = 0.0
rozw2list = []
for k in range(ilosc_przedz):
    rozw2 += h*(func(granice_cal[0] + k*h)+func(granice_cal[0] + (k+1)*h))/2
    rozw2list.append(rozw2) 

print('Rozwiązanie ekstrapolacją Richardsona', rozw2list)
plt.scatter([0.3]*len(rozw2list), rozw2list, label = 'Kolejne etapy obl metody ekstrapolacji Richardsona', 
             color = 'green', marker = 'x')
plt.scatter(0.3, rozw2, label = 'Rozwiązanie metodą ekstrapolacją Richardsona', 
             color = 'green', marker = 'o', )

plt.grid()
plt.legend(loc='lower right', framealpha=0.5)
plt.show() 