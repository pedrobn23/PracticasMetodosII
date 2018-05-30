import math
"""
Datos de entrada
"""

# Intervalo [a,b]
a = 0.0
b = 1.0

# Número de divisiones del intervalo
n = 10

# Número de pasos
k = 3

# Valor inicial y0 = y(a)
y0 = 3

# Función f de dos variables
f = lambda t,y: y-t**2

# h = (b-a) / n
h = 0.2
t = [a + j*h for j in range(n+1)]

# Función exacta
f_exacta = lambda t: t**2 + 2*t + math.exp(t) + 2

# error
error = []

'''
Método de Euler Mejorado
'''
# Intervalo (a,b)
# n número de nodos
# f f(t, y(t)) = y'
# y0 valor de y en t_0

def eulerMejorado(err):
    u = []

    for j in range(n+1):
        if j == 0:
            u.append(y0)
            err.append(y0 - f_exacta(0))
        else:
            u.append(
                u[j-1]+
                h*f( t[j-1] + h/2,
                     u[j-1] + h*f(t[j-1],u[j-1]) )
            )

            err.append( math.fabs(u[j] - f_exacta(t[j])))
    return u

result = eulerMejorado(error)

print("\nEl valor aproximado es:",result)
print("\nEl error es:",error)
