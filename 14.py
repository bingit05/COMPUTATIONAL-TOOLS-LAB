import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit



x = np.array([1,2,3,4,5,6])
y = np.array([6,17,34,57,86,121])

def polynomial (x,a,b,c):

    return a *x**2 + b*x +c

coefficients,covariance = curve_fit(polynomial,x,y)

a,b,c  = coefficients

print("\nFItted polynomials:")
print(f"y = {a:.2f}x^2  + {b:.2f}x  + {c:.2f}")


x_fit = np.linspace(min(x),max(x),100)
y_fit = polynomial(x_fit,a,b,c)


plt.scatter(x,y,color='red',label="original data points")


plt.plot(x_fit,y_fit,color="blue",label="fitted quadratic curve")


plt.xlabel("x")
plt.ylabel("y")
plt.title("second degree polynomial curve fitting ")
plt.legend()
plt.grid(True)
plt.show()