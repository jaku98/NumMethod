# Implementacja aproksymacji wielomianowej metodą najmniejszych kwadratów
import numpy as np
import matplotlib.pyplot as plt

X = np.array([-5, -3, -1, 1, 3, 5])
Y = np.array([0.5, 6, 0.3, 12, 15, 8])
len_x = len(X)

def apro(stopien_wiel):
    x_mat = np.zeros([stopien_wiel+1, stopien_wiel +1])
    y_mat = np.zeros([stopien_wiel+1])
    for i in range(0, stopien_wiel+1):
        for j in range(0, stopien_wiel+1):
            if i == j == 0:
                    x_mat[i,j] = X.shape[0]
            elif (i == 1) and (j > 0):
                x_mat[i,j] = sum(X[s] ** (j + 1) for s in range(0, X.shape[0]))
            else:
                x_mat[i,j] = sum(X[s] ** (i+j) for s in range(0, X.shape[0]))

    for i in range(0, stopien_wiel+1):      
        y_mat[i] = sum(Y[s] * (X[s] ** i) for s in range(0, Y.shape[0]))
    print('Układ równań:', x_mat)
    print('Y', y_mat)
    wsp = np.linalg.solve(x_mat, y_mat)
    for i in range(0, stopien_wiel+1):
        wsp[i] = round(wsp[i], 2)
    print('Współczynniki a:', wsp)
    return wsp

######## WPISZ STOPIEN #########################################
stopien_wiel = 3
mac_A = apro(stopien_wiel)

dl_mac_A = len(mac_A)
mac_x = np.linspace(-5, 5, num = 100)
dl_x = len(mac_x)
mac_y =[]

for x in range(dl_x): # Sumowanie wielomianu, obliczonego z danych X
    y=0
    for a in range(dl_mac_A): # Przy danej potędze
        y = y + mac_A[a]*(mac_x[x]**a)
    mac_y.append(y)

plt.figure()
plt.plot(mac_x, mac_y, '-')
plt.plot(X, Y, 'o')
plt.show()
