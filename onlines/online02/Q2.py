from sympy import *

x = Symbol("x")
f = (x - 4) * (x + 8)
f_prime = f.diff(x)
print(f)
print(f_prime)
f_prime = lambdify(x, f_prime)
print(f_prime(2))