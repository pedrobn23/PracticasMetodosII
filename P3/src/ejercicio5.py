f = lambda t,y: -y+t+1
a = 0
b = 1
n = 5
y0= 1

h = (b-a) / n
t = [a + j*h for j in range(n+1)]


def rungeKutta():
    u = []
    for j in range(n+1):
        if j == 0:
            u.append(y0)
        else:
            K1 = f(t[j-1]      , u[j-1]         )
            K2 = f(t[j-1] + h/2, u[j-1] + h/2*K1)
            K3 = f(t[j-1] + h/2, u[j-1] + h/2*K2)
            K4 = f(t[j-1] + h  , u[j-1] + h  *K3)

            u.append( u[j-1] + h/6*( K1 + 2*K2 + 2*K3 + K4 )            )
    return u

result = rungeKutta()

print("\nEl valor aproximado es:",result)
