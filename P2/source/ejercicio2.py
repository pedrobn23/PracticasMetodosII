import scipy as np
import numpy
from numpy.polynomial import polynomial as P

funcion = input('Introduzca la funcion de la que quiere hallar una raiz en el \
intervalo anterior\nf(x) := ')
exec('f = lambda x:' + funcion)


#Esto son las diferencias divididas calculadas a lo bruto, se puede optimizar
#por el metodo de la diapo 9
def AiNewt( f , pos, nodos, sumaAnt ): 
     lista = [] 

     #Calculamos el denominador
     for i in range( len(nodos) ):
          if( i != pos):
               lista.append(nodos[pos] - b[i])
     denom = np.prod( lista )

     #Lo sumamos a la anterios suma
     suma = suma_ant + f( nodos[pos] )


     
#Interpolacion de newton.
#Se le pasa una funcion y una lista de nodos
#devuelve los coeficientes de un polynomnio (son una lista)
def funcionNewton( f, a ):
     Ai = 0
     polyDef = []
     for i in range( len(a) ):
         Ai = AiNewt( f, i, a, Ai)
         b = []
         for j in range( len(a) ):
              b.append(a[i]) if j!=i
         lista = np.poly(b)
         pol = [ Ai*x for x in lista]

         polyDef = P.polyadd(poly, polyDef);

     return polyDef
