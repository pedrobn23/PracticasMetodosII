# -*- coding: utf-8 -*-
import numpy as np

Threshold = 0.001
Root = 2

#Lectura del intervalo
a=int(input('Introduce el primer valor del intervalo: '))
b=int(input('Introduce el segundo valor del intervalo: '))

#Los valores asignados son irrelevantes, pero necesitamos tener las variables iniciadas
x1 = a
x2 = b

#Lectura de la función
funcion = input('Introduzca la función de la que quiere hallar una raiz en el \
intervalo anterior\nf(x) := ')
exec('f = lambda x:' + funcion)

sgnI = np.sign(f(a))
sgnD = np.sign(f(b))

n = 0
print(a)
print(b)

#Criterio de parada 1

def halt1(x,y):
    return True if abs(x-y) > Threshold else False

while(halt1(x1,x2)) :
    x2=x1
    x1 = (a+b)/2
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1
    print(a)
    print(b)

"""
#Criterio de parada 2

def halt2(x):
    return True if abs(f(x)) > Threshold else False

while(halt2(x1)) :
    x1 = (a+b)/2
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1
    print(a)
    print(b)
"""

"""
#Criterio de parada 3
def halt3():
     return True if abs(x1-Root) > Threshold else False

while(halt3(x1)) :
    x1 = (a+b)/2
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1
    print(a)
    print(b)

"""

"""
#Ejercicio 4
n = int(np.log2((b-a)/Threshold) +1)

for i in range(n):
    x1 = (a+b)/2
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1
    print(a)
    print(b)
"""
