import math


"""
Solves linear equation a * x + b == 0
"""
def solve_linear(a,b):
  return -b/a


"""
Solves quadratic equation a * x^2 + b * x + c == 0
"""  
def solve_quadratic(a,b,c):
  D = b*b - 4 * a * c
  if D<0:
    return "No real roots"
  sqrt_D = math.sqrt(D)
  x1 = (-b + sqrt_D) / (2 * a)
  x2 = (-b - sqrt_D) / (2 * a)
  return (x1,x2)
  

  