# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 20:52:30 2016

@author: HunT
"""

import numpy as np
import sympy as sy
#Your optional code here
#You can import some modules or create additional functions

# DO NOT CHANGE THE NAME OF gausslegendre() function
def gausslegendre(f, a, b, n=20):
    ans = 0
    # Edit here to implement your code
    x,y = np.polynomial.legendre.leggauss(n)
    x_transform = ((b-a)*x*0.5) + ((b+a)*0.5)    
    ans = sum(y*f(x_transform))*((b-a)*0.5)

    return ans

if __name__ == "__main__":
    def f(x):
        return (x**2 +7*x)/(1 +np.sqrt(x))**4
    
    def my_integral():
        x = sy.Symbol('x')
        ans = sy.integrate((x**2 +7*x)/(1 +sy.sqrt(x))**4, (x,0, 1))
        return ans
    
    print('Answer:                    I = ', my_integral())
    print('Your implementation gives: I = ', gausslegendre(f, 0,1))