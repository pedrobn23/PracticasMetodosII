import scipy as sp
import numpy as np
from numpy.polynomial import polynomial as P


def intTrapecio( f, a, b, n ):
     h = (b-a)/n
     x=[ a+h*i for i in range(n+1)]

     
     if(n==0):
          resultado = (f(b) + f(a))*(b-a)/2
     else:
          resultado = ( h *( ( f(x[0]) + f(x[n]) )/2 + sum([f(x[i+1]) for i in range(n-1)]) ) )

     return resultado



# funcion = input('Introduzca la funcion de la que quiere hallar una raiz en el \
# intervalo anterior\nf(x) := ')
# exec('f = lambda x:' + funcion)
# a=('Introduce extremo izquierdo del intervalo := ')
# a=('Introduce extremo derecho del intervalo := ')

f = lambda x: np.log(x)
a=1
b=2
n=200

resultado = intTrapecio( f, a, b, n )
print('Resultado increible')
print(resultado)
