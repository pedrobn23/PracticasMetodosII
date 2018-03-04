import numpy as np

Threshold = 0.001
Root = 2

a=1
b=4
x1 = a
x2 = b

f = lambda x: x-2

sgnI = np.sign(f(a))
sgnD = np.sign(f(b))

n = 0
print(a)
print(b)
    
"""
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


#Criterio de parada 4
n = int(np.log2((b-a)/Threshold) +1)

for i in range(n):
    x1 = (a+b)/2
    if(np.sign(f(x1)) == sgnI):
        a = x1
    else:
	b = x1
    print(a)
    print(b)


print(x1)




        b = x1
    print(a)
    print(b)
