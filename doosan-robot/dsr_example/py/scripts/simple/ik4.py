
# import sympy
from sympy import * 
  
x = symbols('x')
expr = sin(90) + cos(90)
  
print("Before Simplification : {}".format(expr))
    
# Use sympy.trigsimp() method
smpl = float(trigsimp(expr) )
    
print("After Simplification : {}".format(smpl)) 
