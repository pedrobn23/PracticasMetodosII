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
y0 = 1

# Función f de dos variables
f = lambda t,y: -y+t+1


h = (b-a) / n
t = [a + j*h for j in range(n+1)]

'''
Método de Euler
'''
# Intervalo (a,b)
# n número de nodos
# f f(t, y(t)) = y'
# y0 valor de y en t_0
def euler():
    u = []
    for j in range(n+1):
        if j == 0:
            u.append(y0)
        else:
            u.append(u[j-1]+h*f(t[j-1],u[j-1]))
    return u

result = euler()

print("\nEl valor aproximado es:",result)
