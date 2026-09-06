import numpy as np
from scipy.optimize import minimize 

def F(v):
    x,y = v
    return (x-2)**2 + (y-2)**2

initial_guess  = [0,0]


result =  minimize(F,initial_guess,method='BFGS')

print("optimal x=",result.x[0])
print("optimal y=",result.x[1])
print("Minimum value =",result.fun)
print("Optimization successful:",result.success)