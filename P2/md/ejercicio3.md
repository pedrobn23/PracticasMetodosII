
```python
import scipy as sp
import numpy as np
from numpy.polynomial import polynomial as P


def intTrapecio( f, a, b, n ):
     h = (b-a)/n
     x=[ a+h*i for i in range(n+1)]

     if(n<1):
          resultado=0     
     elif(n==1):
          resultado = (f(b) + f(a))*(b-a)/2
     else:
          resultado = ( h *( ( f(x[0]) + f(x[n]) )/2 + sum([f(x[i+1]) for i in range(n-1)]) ) )

     return resultado

f= lambda x: np.log(x) 
a=1
b=2
n=200

resultado = intTrapecio( f, a, b, n )
print("\nEl valor aproximado es:",resultado)
```