# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sympy as sp
import numpy as np 
from sympy import *
from sympy.physics.mechanics import *
theta1, theta2, theta3, theta4, theta5, theta6, theta,l1,l2,l3,l4, alpha, a, d = dynamicsymbols('theta1, theta2, theta3, theta4, theta5, theta6, l1, l2, l3, l4, theta, alpha, a, d')
init_printing(use_unicode=True)
from sympy.physics.vector import init_vprinting
init_vprinting(use_latex='mathjax', pretty_print=False)

r01 = sp.Matrix([[sp.cos(theta1), 0, sp.sin(theta1)],
                 [sp.sin(theta1),  0, -sp.cos(theta1)],
                 [0, 1, 0]])
r12 = sp.Matrix([[sp.cos(theta2),-sp.sin(theta2) ,0 ],
                 [sp.sin(theta2),  sp.cos(theta2), 0],
                 [0, 0, 1]])
r02 = sp.simplify((r01*r12))
r23 = sp.Matrix([[0,sp.cos(theta3),-sp.sin(theta3)],
                 [0,sp.sin(theta3),  sp.cos(theta3)],
                 [1, 0, 0]])
r03 = sp.simplify((r02*r23))
r34 = sp.Matrix([[sp.sin(theta4),0,-sp.cos(theta4) ],
                 [-sp.cos(theta4), 0, -sp.sin(theta4)],
                 [0, 1, 0]])
r04 = sp.simplify((r03*r34))
r45 = sp.Matrix([[-sp.cos(theta5),0,sp.sin(theta5) ],
                 [-sp.sin(theta5),0,  sp.cos(theta5)],
                 [0, -1, 0]])
r05 = sp.simplify((r04*r45))
r56 = sp.Matrix([[sp.cos(theta6),-sp.sin(theta6) ,0 ],
                 [sp.sin(theta6),  sp.cos(theta6), 0],
                 [0, 0, 1]])
r06 = sp.simplify((r05*r56))

h01 = sp.Matrix([[sp.cos(theta1),-sp.sin(theta1) ,0 ,0],
                 [sp.sin(theta1),  sp.cos(theta1), 0,0],
                 [0, 0, 1, 155.5],
                 [0,0,0,1]])
h12 = sp.Matrix([[sp.cos(theta2),0,-sp.sin(theta2) ,0 ],
                 [sp.sin(theta2), 0, sp.cos(theta2), 0],
                 [0, -1, 0, 0],
                 [0,0,0,1]])
h02 = sp.simplify((h01*h12))
h23 = sp.Matrix([[sp.cos(theta3),-sp.sin(theta3) ,0 ,409*sp.cos(theta3)],
                 [sp.sin(theta3),  sp.cos(theta3), 0,409*sp.sin(theta3)],
                 [0, 0, 1, 0],
                 [0,0,0,1]])
h03 = sp.simplify((h02*h23))
print(h03)
# h34 = sp.Matrix([[sp.cos(theta4),0,sp.sin(theta4) ,0],
#                  [sp.sin(theta4),0,-sp.cos(theta4), 0],
#                  [0, 1, 0, 367],
#                  [0,0,0,1]])
# h04 = sp.simplify((h03*h34))
# h45 = sp.Matrix([[sp.cos(theta5),0,-sp.sin(theta5) ,0],
#                  [sp.sin(theta5), 0, sp.cos(theta5), 0],
#                  [0, -1, 0, 0],
#                  [0,0,0,1]])
# h05 = sp.simplify((h04*h45))
# h56 = sp.Matrix([[sp.cos(theta6),0,sp.sin(theta6) ,0],
#                  [sp.sin(theta6), 0, -sp.cos(theta6), 0],
#                  [0, 1, 0, 124],
#                  [0,0,0,1]])
# h36 = sp.simplify((h34*h45*h56))    
# # print(h36)             
# h06 = sp.simplify((h05*h56))
# print(h06[1,2])
# d6 = 124*sp.cos(theta5)+367
# M2 = (sin(theta1 + theta2)*cos(theta3 + theta4)*cos(theta5) + sin(theta5)*cos(theta1 + theta2))*sin(theta6) + sin(theta1 + theta2)*sin(theta3 + theta4)*cos(theta6)
# M1 = -sp.sin(theta5)*sp.sin(theta1+theta2) - sp.cos(theta1+theta2)*sp.cos(theta3+theta4)*sp.cos(theta5)*sp.sin(theta6) + sp.sin(theta3+theta4)*sp.cos(theta1+theta2)*sp.cos(theta6)        
# Sol1 = (d6*M1)
# Sol2 = (d6*M1)
# # print(Sol2)   
# P = 491
# ox = P-Sol1
# # print(ox) 
# Q = 0
# oy = Q - Sol2     
# # print(oy) 

# T = np.arctan2(Q,P) 
# print(T)
# d06 = ([h06[0,3], h06[1,3], h06[2,3]])
# d01 = ([h01[0,3], h01[1,3], h01[2,3]])
# d02 = ([h02[0,3], h02[1,3], h02[2,3]])
# d03 = ([h03[0,3], h03[1,3], h03[2,3]])
# d04 = ([h04[0,3], h04[1,3], h04[2,3]])
# d05 = ([h05[0,3], h05[1,3], h05[2,3]])

# d06_d01 = np.subtract(d06 , d01)
# d06_d02 = np.subtract(d06 , d02)
# d06_d03 = np.subtract(d06 , d03)
# d06_d04 = np.subtract(d06 , d04)
# d06_d05 = np.subtract(d06 , d05)

# r00 = ([[0],
#         [0],
#         [1]])
# r10 = np.matmul(r01,r00)
# r10 = ([r10[0,0],r10[1,0],r10[2,0]])
# r20 = np.matmul(r02,r00)
# r20 = ([r20[0,0],r20[1,0],r20[2,0]])
# r30 = np.matmul(r03,r00)
# r30 = ([r30[0,0],r30[1,0],r30[2,0]])
# r40 = np.matmul(r04,r00)
# r40 = ([r40[0,0],r40[1,0],r40[2,0]])
# r50 = np.matmul(r05,r00)
# r50 = ([r50[0,0],r50[1,0],r50[2,0]])
# r00 = ([0,0,1])
R1 = np.cross(r00,d06, axisc=0)
R2 = np.cross(r10,d06_d01, axisc=0)
R3 = np.cross(r20,d06_d02, axisc=0)
R4 = np.cross(r30,d06_d03, axisc=0)
R5 = np.cross(r40,d06_d04, axisc=0)
R6 = np.cross(r50,d06_d05, axisc=0)
# # R = sp.simplify([[R1,R2,R3,R4,R5,R6],
# #                  [r00,r10,r20,r30,r40,r50]])
# #print(R)
# R = np.array([[R1[0], R2[0], R3[0], R4[0], R5[0], R6[0]],
#               [R1[1], R2[1], R3[1], R4[1], R5[1], R6[1]],
#               [R1[2], R2[2], R3[2], R4[2], R5[2], R6[2]],
#               [r00[0], r10[0], r20[0], r30[0], r40[0], r50[0]],
#               [r00[1], r10[1], r20[1], r30[1], r40[1], r50[1]],
#               [r00[2], r10[2], r20[2], r30[2], r40[2], r50[2]]])
# angle = ([[theta1],[theta2],[theta3],[theta4],[theta5],[theta6]])
# final_r = sp.simplify(np.dot(R,angle))
# t01 = final_r.subs({theta1:a, theta2:b,  theta3:c, theta4:d, theta5:e, theta6:f})
# print(sp.simplify(t01))
