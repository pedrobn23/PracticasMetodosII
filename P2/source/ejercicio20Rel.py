import scipy as sp
import numpy as np
from numpy.polynomial import polynomial as P

def intTrapecio( f, a, b, n ):
     if(n==1):
          resultado = (f(b) + f(a))*(b-a)/2
     else:
          h = (b-a)/n
          x=[ a+h*i for i in range(n+1)]
          resultado = ( h *( ( f(x[0]) + f(x[n]) )/2 + sum([f(x[i+1]) for i in range(n-1)]) ) )

     return resultado

#Rk = R_{k,j-1} RK1 = R_{k-1,j-1}
def rombergParcial( Rk, Rk1, j ):
     return Rk + (1/(4**j-1))*(Rk - Rk1)

def romberg(f, a, b, k):
      R=[]
      R.append( intTrapecio( f, a, b, 1 ) )
      for i in range(k):
           R.append( intTrapecio( f, a, b, 2**(i+1) ) )

      for i in range(k):
           for j in range(k-i):
               R[j]=rombergParcial( R[j+1], R[j], i+1 )

      return R[0]

f = (lambda x: x*x * np.log(x))
a=1
b=1.5
cont = 0
diff = 1

print("Función x^2*log(x)\n")
while diff >= 10**(-6):
    Rk = romberg(f, a, b, cont)
    Rk1 = romberg(f, a, b, cont+1)
    print("R{0},{0} =".format(cont), Rk )
    print("R{0},{0} =".format(cont+1), Rk1 )
    diff = abs(Rk-Rk1)
    print("|R{0},{0}-R{1},{1}| =".format(cont, cont+1), diff)
    print("\n")
    cont = cont+1

f = lambda x: x*x*x * np.exp(-x)
a=0
b=1
cont = 0
diff = 1

print("Función x^3*e^(-x)\n")
while diff >= 10**(-6):
    Rk = romberg(f, a, b, cont)
    Rk1 = romberg(f, a, b, cont+1)
    print("R{0},{0} =".format(cont), Rk )
    print("R{0},{0} =".format(cont+1), Rk1 )
    diff = abs(Rk-Rk1)
    print("|R{0},{0}-R{1},{1}| =".format(cont, cont+1), diff)
    print("\n")
    cont = cont+1

#Ejercicio grupo Saez
f = lambda x: 3*x/(x**2 - 4)
a=1
b=1.8
cont = 0
diff = 1

print("Función x^3*e^(-x)\n")
while diff >= 10**(-6):
    Rk = romberg(f, a, b, cont)
    Rk1 = romberg(f, a, b, cont+1)
    print("R{0},{0} =".format(cont), Rk )
    print("R{0},{0} =".format(cont+1), Rk1 )
    diff = abs(Rk-Rk1)
    print("|R{0},{0}-R{1},{1}| =".format(cont, cont+1), diff)
    print("\n")
    cont = cont+1
