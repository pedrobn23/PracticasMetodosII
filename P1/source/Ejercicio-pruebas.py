#Algoritmo de biseccion
#Realizadores:
#Pedro Bonilla, Johanna Capote y Guillermo Galindo
#Ejecucion:
#$ python3.5 Ejercicio1.py

#IMPORTANTE: para ejecutar este programa se requiere tener instalado "numpy"
#en su defecto, se puede sustituir por funciones de la libreria math

import numpy as np

Threshold = pow(10,-5)
Root = 0
counter = 0

#Lectura del intervalo
a=float(input('Introduce el primer valor del intervalo: '))
b=float(input('Introduce el segundo valor del intervalo: '))

a_init=a
b_init=b

#Los valores asignados son irrelevantes, pero necesitamos tener las variables iniciadas
x1 = a
x2 = b

#Lectura de la funcion
funcion = input('Introduzca la funcion de la que quiere hallar una raiz en el \
intervalo anterior\nf(x) := ')
exec('f = lambda x:' + funcion)

#Signo de los extremos del intervalo
sgnI = np.sign(f(a))
sgnD = np.sign(f(b))

n = 0

#Criterio de parada 1
n_iter=0
print ("Criterio 1:")
def halt1(x,y):
    return True if abs(x-y) > Threshold else False

while(halt1(x1,x2)) :
    n_iter+=1
    x2=x1
    x1 = (a+b)/2

    #Reducimos el intervalo a la mitad
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1
    #Descomentar la linea de abajo para mostrarlo en cada iteracion
    print(n_iter,"-",x1)

#Imprimimos la aproximacion final
print(x1)

a=a_init
b=b_init
x1 = a

#Criterio de parada 2
n_iter=0
print ("Criterio 2:")
def halt2(x):
    return True if abs(f(x)) > Threshold else False

while(halt2(x1)) :
    n_iter+=1
    x1 = (a+b)/2

    #Reducimos el intervalo a la mitad
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1

    #Descomentar la linea de abajo para mostrarlo en cada iteracion
    print(n_iter,"-",x1)

#Imprimimos la aproximacion final
print(x1)

a=a_init
b=b_init
x1 = a

#Criterio de parada 3
n_iter=0
Root=float(input('Introduce una raiz: '))

print ("Criterio 3:")
def halt3(x):
     return True if abs(x-Root) > Threshold else False

while(halt3(x1)) :
    n_iter+=1
    x1 = (a+b)/2

    #Reducimos el intervalo a la mitad
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1

    #Descomentar la linea de abajo para mostrarlo en cada iteracion
    print(n_iter,"-",x1)

#Imprimimos la aproximacion final
print(x1)

a=a_init
b=b_init
x1 = a

#Criterio de parada 4
n_iter=0
print ("Criterio 4:")
n = int(np.log2((b-a)/Threshold)-1)
print(n)
for i in range(n):
    n_iter+=1
    x1 = (a+b)/2

    #Reducimos el intervalo a la mitad
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
        b = x1

    #Descomentar la linea de abajo para mostrarlo en cada iteracion
    print(n_iter,"-",x1)

#Imprimimos la aproximacion final
print(x1)
