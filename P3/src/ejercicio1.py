f = lambda t,y: -y+t+1
a = 0
b = 1
n = 10
y0= 1

h = (b-a) / n
t = [a + j*h for j in range(n+1)]


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
