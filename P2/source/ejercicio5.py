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

def ampliaIntegral( f, a, b, Rk, k):
     index = 2**(k)
     h = (b-a)/(index * 2)
     resultado=0
     
          resultado= Rk/2 + ( sum( [f(a +(2i+1)h) for i in range(index)] ) )

     return resultado

def rombergParcial( Rk, Rk1, j ):
     return Rk + (1/(4**j-1))*(Rk - Rk1)
          
def romberg(f, a, b, n):
     R=[]
     R.append( intTrapecio( f, a, b, 0 ) )
     for i in range(n):
          R.append( ampliaIntegral( f, a, b, R[i], i ) )

     for i in range(n):
          for j in range(n-i):
               


     
     
