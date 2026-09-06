import scipy
from scipy.integrate import quad
from scipy.misc import derivative


def f(x):
    return x**3 + 2*x**2 + x + 1


x = 2

differentiation =  derivative (f,x,dx=1e-6)

integration,error = quad(f,0,2)


print("Funtion : f(x) = x^3 +2x^2 + x+1")
print("Numerical derivative at x =",x,":",differentiation)
print("Numerical integration from 0 to 2 :",integration)
print("estimated Integration error :",error)