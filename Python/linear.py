from sympy import symbols, Eq, solve

# Symbolic variables
x, y, z = symbols('x, y, z')

# Equations 
eq1 = Eq(3*x + 2*y - 1*z, 15)
eq2 = Eq(1*x - 3*y - 1*z, 17)

# Solve
solution = solve((eq1, eq2), (x, y, z))
print(solution)
