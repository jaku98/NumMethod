import math
from matplotlib import pyplot as plt


road = int(input("\n Wybierz funkcję: \n SIN(x) - 1 \n COS(x) - 2 \n    e^x - 3  \n   plot - 4   "))
y_cos = 0.0
y_sin = 0.0
x_cos = 0.0
x_sin = 0.0

# SINUS
def sin():
    x_sin=float(input("Arg sin [st] = "))
    n=int(input("Ilość wyrazów szeregu n [l. całk.]= "))
    x_sin = math.radians(x_sin)
    y_sin = 0.0
    for k in range(n):
        y_sin += ((-1)**k)*(x_sin**(1+2*k)) / math.factorial(1+2*k)

    print("sin(x) = ", y_sin)

# COSINUS
def cos():
    x_cos=float(input("Arg cos [st] = "))
    n=int(input("Ilość wyrazów szeregu n [l. całk.]= "))
    x_cos = math.radians(x_cos)
    y_cos = 0.0
    for k in range(n):
        y_cos += ((-1)**k)*(x_cos**(2*k)) / math.factorial(2*k)

    print("cos(x) = ", y_cos)

# EULER
def euler():
    x_e=float(input("Arg e = "))
    n=int(input("Ilość wyrazów szeregu n [l. całk.]= "))    
    y_e = 0.0
    for k in range(n):
        y_e += x_e**k / math.factorial(k)

    print("E^",x_e, " = ",y_e)

def plot():
    zakr = int(input("\n Podaj zakres (0:) [st] ")) +1
    list_ox = list(range(0, zakr))
    n = int(input("Ilość wyrazów szeregu n [l. całk.]= "))
    global x_sin, x_cos, y_sin, y_cos
    array_sin = []
    array_cos = []
    
    for i in range(zakr):
        z = math.radians(i)
        y_sin = 0
        y_cos = 0

        for k in range(n):
            y_sin += ((-1)**k)*(z**(1+2*k)) / math.factorial(1+2*k)
            y_cos += ((-1)**k)*(z**(2*k)) / math.factorial(2*k)
        
        array_sin.append(y_sin)
        array_cos.append(y_cos)

    plt.plot(list_ox, array_sin, label='SIN(x)')
    plt.plot(list_ox, array_cos, label='COS(x)')
    plt.xlabel('x [st]')
    plt.ylabel('f(x)')
    plt.title('Rozwinięcię w szereg Taylora')
    plt.legend()
    plt.show()

if road == 1:
    sin()
elif road == 2:
    cos()
elif road == 3:
    euler()
else:
    plot()