from sympy import *
import sys

x = Symbol("x")
function = x**2 + x*2 + 4
derivative = function.diff(x)

print("Original Function = ", function)
print("Derivated Function = ", derivative) 
