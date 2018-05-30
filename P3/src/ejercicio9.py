from scipy.integrate import quad
import numpy as np
import math as mth
from scipy import optimize

"""
Datos de entrada
"""

# Intervalo [a,b]
a = 0.0
b = 2.0

# Número de divisiones del intervalo
n = 10

# Número de pasos
k = 4

# Valor inicial y0 = y(a)
y0 = 0.5

# Función f de dos variables
def f(t, y):
    return y - t**2 + 1.0

# Función y solución exacta (si existe)
def y(t):
    return (t+1)**2 -0.5*np.exp(t)

'''
Método de Euler
'''
# Intervalo (a,b)
# n número de nodos
# f f(t, y(t)) = y'
# y0 valor de y en t_0

def eulerMejorado(a, b, n, f, y0):
    h = (b-a) / n
    t = [a + j*h for j in range(n+1)]

    u = []
    for j in range(n+1):
        if j == 0:
            u.append(y0)
        else:
            u.append(
                u[j-1]+
                h*f( t[j-1] + h/2,
                     u[j-1] + h*f(t[j-1],u[j-1]) )
            )
    return u

'''
Método de Adams Moulton
'''

def func(x, i):
    arr = []
    for j in range(i+1):
        arr.append(x+j-1)
    for j in range(i+2, k+1):
        arr.append(x+j-1)

    return np.prod(np.array(arr))

# (a,b) intervalo
# n número de nodos
# k número de pasos
# f f(t, y(t)) = y'
# u = vector con las primeras j aproximaciones u_0, ..., u_j
def adamsMoulton(a, b, k, j, f, u):
    h = (b-a) / n
    t = [a + j*h for j in range(n+1)]

    # Coeficientes b (b[0] = b_-1,  ..., b[k] = b_k-1
    b = []

    for i in range(-1,k):
        b.append( (-1)**(i+1)/(mth.factorial(i+1)*mth.factorial(k-i-1)) * quad(func, 0, 1, args=(i,) )[0] )

    sumatory = 0
    for i in range (0,k):
        sumatory = sumatory + b[i+1]*f(t[j-i],u[j-i])

    # Función que define a la ecuación implícita (si g(x) = 0 -> x = u_j+1)
    g = lambda x: x - u[j] - h*(sumatory + b[0]*f(t[j+1], x))

    a = 1e-7
    # Derivada de g aproximada
    dg = lambda x: (g(x+a) - g(x-a))/(2.0*a)

    # u_j+1
    u_j1 = optimize.newton(g, u[j], dg)
    return u_j1

'''
Programa principal
'''
h = (b-a) / n
t = [a + j*h for j in range(n+1)]

# valores_euler = eulerMejorado(a, b, n, f, y0)
u = []
for j in range(k):
    u.append(y(t[j]))

for j in range(k-1, n) :
    u.append(adamsMoulton(a, b, k, j, f, u))

print("Datos del problema: ")
print(" * Problema:")
print("     - y'(t) = y(t) - t^2 +1")
print("     - y(0) = ", y0)
print(" * Intervalo: (", a, ", ", b, ")" )
print(" * Numero de subintervalos: ", n)
print(" * Número de pasos: ", k)
print(" * Solución exacta: y(t) = (t + 1)^2 - 0.5 e^t")
print("Resultados: ")

for j in range(n+1):
    print("------")
    print("Punto: ", t[j])
    print("Aproximación: ", u[j])
    print("Valor exacto: ", y(t[j]) )
    print("Error: ", abs(y(t[j]) - u[j]))
