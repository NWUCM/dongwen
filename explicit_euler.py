#explicit_euler_1d
n = 10
T = 1
tn = 0
xn = 1
def f(tn, xn):
    return 4*tn*xn**0.5
for i in range(n):
    xn = xn + (T/n)*f(tn,xn)
    yn = (1+tn**2)**2
    error = xn-yn
    tn = tn + (T/n)
    print(error)
