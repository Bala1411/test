#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sympy import *
import sympy as sp
import numpy as np
import math
# import numpy as sp
# from sympy.physics.vector import init_vprinting
# init_vprinting(use_latex='mathjax', pretty_print=False)
# from sympy.physics.mechanics import dynamicsymbols
# theta1, theta2, theta3, theta4, theta5, theta6, l1, l2, l3, l4, theta, alpha, a, d = dynamicsymbols('theta1 theta2 theta3 theta4 theta5 theta6 l1 l2 l3 l4 theta alpha a d')
# theta = theta1,theta2,theta3,theta4,theta5,theta6
# rot = sp.Matrix([[sp.cos(theta), -sp.sin(theta)*sp.cos(alpha), sp.sin(theta)*sp.sin(alpha)],
#                  [sp.sin(theta), sp.cos(theta)*sp.cos(alpha), -sp.cos(theta)*sp.sin(alpha)],
#                  [0, sp.sin(alpha), sp.cos(alpha)]])

# trans = sp.Matrix([a*sp.cos(theta),a*sp.sin(theta),d])

# last_row = sp.Matrix([[0, 0, 0, 1]])

# t = sp.Matrix.vstack(sp.Matrix.hstack(rot, trans), last_row)
alpha1 = 90
alpha2 = 0
alpha3 = 90
alpha4 = 90
alpha5 = -90
alpha6 = 0

a1 = 0
a2 = 0
a3 = 409
a4 = 0
a5 = 0
a6 = 0

theta1 = 0
theta2 = 0
theta3 = 90
theta4 = 0
theta5 = 0
theta6 = 0

d1 = 155.5
d2 = 0
d3 = 0
d4 = 367
d5 = 0
d6 = 124

for i in range(0,36):

    t01 = sp.Matrix([[sp.cos(theta1), -sp.sin(theta1)*sp.cos(alpha1), sp.sin(theta1)*sp.sin(alpha1), a1*sp.cos(theta1)],
                    [sp.sin(theta1),  sp.cos(theta1)*sp.cos(alpha1), -sp.cos(theta1)*sp.sin(alpha1), a1*sp.sin(theta1)],
                    [0, sp.sin(alpha1), sp.cos(alpha1), d1],
                    [0, 0, 0, 1]])
    t12 = sp.Matrix([[sp.cos(theta2), -sp.sin(theta2)*sp.cos(alpha2), sp.sin(theta2)*sp.sin(alpha2), a2*sp.cos(theta2)],
                    [sp.sin(theta2),  sp.cos(theta2)*sp.cos(alpha2), -sp.cos(theta2)*sp.sin(alpha2), a2*sp.sin(theta2)],
                    [0, sp.sin(alpha2), sp.cos(alpha2), d2],
                    [0, 0, 0, 1]])
    t23 = sp.Matrix([[sp.cos(theta3), -sp.sin(theta3)*sp.cos(alpha3), sp.sin(theta3)*sp.sin(alpha3), a3*sp.cos(theta3)],
                    [sp.sin(theta3),  sp.cos(theta3)*sp.cos(alpha3), -sp.cos(theta3)*sp.sin(alpha3), a3*sp.sin(theta3)],
                    [0, sp.sin(alpha3), sp.cos(alpha3), d3],
                    [0, 0, 0, 1]])
    t34 = sp.Matrix([[sp.cos(theta4), -sp.sin(theta4)*sp.cos(alpha4), sp.sin(theta4)*sp.sin(alpha4), a4*sp.cos(theta4)],
                    [sp.sin(theta4),  sp.cos(theta4)*sp.cos(alpha4), -sp.cos(theta4)*sp.sin(alpha4), a4*sp.sin(theta4)],
                    [0, sp.sin(alpha4), sp.cos(alpha4), d4],
                    [0, 0, 0, 1]])
    t45 = sp.Matrix([[sp.cos(theta5), -sp.sin(theta5)*sp.cos(alpha5), sp.sin(theta5)*sp.sin(alpha5), a5*sp.cos(theta5)],
                    [sp.sin(theta5),  sp.cos(theta5)*sp.cos(alpha5), -sp.cos(theta5)*sp.sin(alpha5), a5*sp.sin(theta5)],
                    [0, sp.sin(alpha5), sp.cos(alpha5), d5],
                    [0, 0, 0, 1]])
    t56 = sp.Matrix([[sp.cos(theta6), -sp.sin(theta6)*sp.cos(alpha6), sp.sin(theta6)*sp.sin(alpha6), a6*sp.cos(theta6)],
                    [sp.sin(theta6),  sp.cos(theta6)*sp.cos(alpha6), -sp.cos(theta6)*sp.sin(alpha6), a6*sp.sin(theta6)],
                    [0, sp.sin(alpha6), sp.cos(alpha6), d6],
                    [0, 0, 0, 1]])

    t06 = t01*t12*t23*t34*t45*t56           
    # print(t06)      

    px = (t06[0,3].simplify())
    Px = trigsimp(px)
    print("px:", Px)
    py = (t06[1,3].simplify())
    print("py:", py)
    pz = (t06[2,3].simplify())
    print("pz:", pz)
    theta1 += 10    

# d01 = sp.Matrix([t01[0,3],
#                 t01[1,3],
#                 t01[2,3]])
# d12 = sp.Matrix([t12[0,3],
#                 t12[1,3],
#                 t12[2,3]])
# d23 = sp.Matrix([t23[0,3],
#                 t23[1,3],
#                 t23[2,3]])
# d34 = sp.Matrix([t34[0,3],
#                 t34[1,3],
#                 t34[2,3]])

# d45 = sp.Matrix([t45[0,3],
#                 t45[1,3],
#                 t45[2,3]])
# d56 = sp.Matrix([t56[0,3],
#                 t56[1,3],
#                 t56[2,3]])   
# d06 = d01+d12+d23+d34+d45+d56    
# print(d06)  

# # d01 = sp.Matrix([t01[0,3],
#                 t01[1,3],
#                 t01[2,3]])
# d02 = sp.Matrix([t02[0,3],
#                 t02[1,3],
#                 t02[2,3]])
# d03 = sp.Matrix([t03[0,3],
#                 t03[1,3],
#                 t03[2,3]])
# d04 = sp.Matrix([t04[0,3],
#                 t04[1,3],
#                 t04[2,3]])

# d05 = sp.Matrix([t05[0,3],
#                 t05[1,3],
#                 t05[2,3]]) 
# d06 = sp.Matrix([t06[0,3],
#                 t06[1,3],
#                 t06[2,3]])      
# p06 = d01+d02+d03+d04+d05+d06      
# print(p06)            
                        

# # P = sp.abs([[t06[0,3]],
# #               [t06[1,2]],
# #               [t06[2,3]]]) 
# # print(P)           
