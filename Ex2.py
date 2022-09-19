# Metoda Croute'a-Doolittle'a
import numpy as np

 
matrix_A = np.array([[1,2,-1,1],[-1,1,2,-1],[2,-1,2,2],[1,1,-1,2]])
matrix_B = np.array([[6],[3],[14],[8]])

lenA = len(matrix_A)

def LU(A, n):
    upper = np.zeros([n,n])
    lower = np.zeros([n,n])

    for i in range(n):
        for k in range(i, n): # Tworzenie U
            fctr = 0
            for j in range(i):
                fctr += lower[i,j] * upper[j,k]
            upper[i,k] = A[i,k] - fctr

        for k in range(i, n): # Tworzenie L
            fctr = 0
            for j in range(i):
                fctr += lower[k,j] * upper[j,i]
            lower[k,i] = (A[k,i]-fctr)/upper[i,i]
        lower[i,i] = 1 # 1 na przekątnej L

    print("U:\n", upper)
    print("L:\n", lower)
    return upper, lower

def solve(U, L, n, B):
    y = np.array([0.0]*n)
    x = np.array([0.0]*n)    
    y = np.linalg.solve(L, B) # Ly = B
    x = np.linalg.solve(U, y) # Ux = y
    print("Rozwiązanie:\n", x)

upper, lower = LU(matrix_A, lenA)
solve(upper, lower, lenA, matrix_B)