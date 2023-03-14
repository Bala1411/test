#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sympy as sp
import numpy as np 
from numpy.core import *
from sympy import *
from sympy.physics.mechanics import *


theta1, theta2, theta3, theta4, theta5, theta6,A,B,C,D,E,F= symbols('p, q, r, s, t, u,A,B,C,D,E,F', real = true)
init_printing(use_unicode=True)
from sympy.physics.vector import init_vprinting
init_vprinting(use_latex='mathjax', pretty_print=True)


r01 = sp.Matrix([[0, 0, -1],
                 [sp.cos(theta1),  -sp.sin(theta1), 0],
                 [sp.sin(theta1), sp.cos(theta1), 0]])

r12 = sp.Matrix([[sp.sin(theta2),sp.cos(theta2) ,0 ],
                 [sp.cos(theta2),  -sp.sin(theta2), 0],
                 [0, 0, 1]])

r02 = sp.simplify((r01*r12))

r23 = sp.Matrix([[0, 0, 1],
                 [sp.cos(theta3),-sp.sin(theta3),0],
                 [-sp.sin(theta3), -sp.cos(theta3), 0]])

r03 = sp.simplify((r02*r23))

r34 = sp.Matrix([[sp.cos(theta4),-sp.sin(theta4), 0 ],
                 [0, 0, -1],
                 [sp.sin(theta4),sp.cos(theta4), 0]])

r04 = sp.simplify((r03*r34))

r45 = sp.Matrix([[sp.cos(theta5),-sp.sin(theta5), 0 ],
                 [0, 0, 1],
                 [-sp.sin(theta5),-sp.cos(theta5), 0]])
            
r05 = sp.simplify((r04*r45))

r56 = sp.Matrix([[sp.cos(theta6),-sp.sin(theta6) ,0 ],
                 [sp.sin(theta6),  sp.cos(theta6), 0],
                 [0, 0, 1]])

r06 = sp.simplify((r05*r56))

h01 = sp.Matrix([[sp.cos(theta1), 0, sp.sin(theta1) ,0],
                 [sp.sin(theta1), 0, -sp.cos(theta1), 0],
                 [0, 1, 0, 155.5],
                 [0,0,0,1]])

h12 = sp.Matrix([[sp.cos(theta2),-sp.sin(theta2) ,0, 409*sp.cos(theta2)],
                 [sp.sin(theta2),sp.cos(theta2), 0, 409*sp.sin(theta2) ],
                 [0,0,1, 0],
                 [0,0,0,1]])

h02 = sp.simplify((h01*h12))

h23 = sp.Matrix([[sp.cos(theta3 + 90), 0, sp.sin(theta3 + 90) ,0],
                 [sp.sin(theta3 + 90), 0, -sp.cos(theta3 + 90), 0],
                 [0, 1, 0, 0],
                 [0,0,0,1]])

h03 = sp.simplify((h02*h23))

h34 = sp.Matrix([[sp.cos(theta4),0,sp.sin(theta4) ,0],
                 [sp.sin(theta4),0,-sp.cos(theta4), 0],
                 [0, 1, 0, 367],
                 [0,0,0,1]])

h04 = sp.simplify((h03*h34))

h45 = sp.Matrix([[sp.cos(theta5),0,sp.sin(theta5) ,0],
                 [sp.sin(theta5), 0, -sp.cos(theta5), 0],
                 [0, 1, 0, 0],
                 [0,0,0,1]])

h05 = sp.simplify((h04*h45))

h56 = sp.Matrix([[sp.cos(theta6),-sp.sin(theta6) ,0 , 0],
                 [sp.sin(theta6), sp.cos(theta6), 0, 0],
                 [0, 0, 1, 124],
                 [0,0,0,1]])

h06 = sp.simplify((h05*h56))

  
d01 = [[h01[0,3]],
       [h01[1,3]],
       [h01[2,3]]]     
d02 = [[h01[0,3]+h12[0,3]],
      [h01[1,3]+h12[1,3]],
      [h01[2,3]+h12[2,3]]]   
d03 = [[h01[0,3]+h12[0,3]+h23[0,3]],
      [h01[1,3]+h12[1,3]+h23[1,3]],
      [h01[2,3]+h12[2,3]+h23[2,3]]]            
d04 = [[h01[0,3]+h12[0,3]+h23[0,3]+h34[0,3]],
      [h01[1,3]+h12[1,3]+h23[1,3]+h34[1,3]],
      [h01[2,3]+h12[2,3]+h23[2,3]+h34[2,3]]]  
d05 = [[h01[0,3]+h12[0,3]+h23[0,3]+h34[0,3]+h45[0,3]],
      [h01[1,3]+h12[1,3]+h23[1,3]+h34[1,3]+h45[1,3]],
      [h01[2,3]+h12[2,3]+h23[2,3]+h34[2,3]+h45[2,3]]]    
d06 = np.array([[h01[0,3]+h12[0,3]+h23[0,3]+h34[0,3]+h45[0,3]+h56[0,3]],
                [h01[1,3]+h12[1,3]+h23[1,3]+h34[1,3]+h45[1,3]+h56[1,3]],
                [h01[2,3]+h12[2,3]+h23[2,3]+h34[2,3]+h45[2,3]+h56[2,3]]] )  

# print(h06)
# d06 = ([h06[0,3], h06[1,3], h06[2,3]])
# print(d06)
# d01 = ([h01[0,3], h01[1,3], h01[2,3]])
# d02 = ([h02[0,3], h02[1,3], h02[2,3]])
# d03 = ([h03[0,3], h03[1,3], h03[2,3]])
# d04 = ([h04[0,3], h04[1,3], h04[2,3]])
# d05 = ([h05[0,3], h05[1,3], h05[2,3]])

d06_d01 = np.array(np.subtract(d06 , d01))
d06_d02 = np.array(np.subtract(d06 , d02))
d06_d03 = np.array(np.subtract(d06 , d03))
d06_d04 = np.array(np.subtract(d06 , d04))
d06_d05 = np.array(np.subtract(d06 , d05))

r00 =np.array([[0],
               [0],
               [1]])
r10 = np.array(np.matmul(r01,r00))
# r10 = ([r10[0,0],r10[1,0],r10[2,0]])
r20 =np.array( np.matmul(r02,r00))
# r20 = ([r20[0,0],r20[1,0],r20[2,0]])
r30 = np.array(np.matmul(r03,r00))
# r30 = ([r30[0,0],r30[1,0],r30[2,0]])
r40 = np.array(np.matmul(r04,r00))
# r40 = ([r40[0,0],r40[1,0],r40[2,0]])
r50 = np.array(np.matmul(r05,r00))
# r50 = ([r50[0,0],r50[1,0],r50[2,0]])
# r00 = ([0,0,1])
R1 = np.array([[(r00[1]*d06[2])-(r00[2]*d06[1])],[(r00[2]*d06[0])-(r00[0]*d06[2])],[(r00[0]*d06[1])-(r00[1]*d06[0])]])
R2 = np.array([[(r10[1]*d06_d01[2])-(r10[2]*d06_d01[1])],[(r10[2]*d06_d01[0])-(r10[0]*d06_d01[2])],[(r10[0]*d06_d01[1])-(r10[1]*d06_d01[0])]])
R3 = np.array([[(r20[1]*d06_d02[2])-(r20[2]*d06_d02[1])],[(r20[2]*d06_d02[0])-(r20[0]*d06_d02[2])],[(r20[0]*d06_d02[1])-(r20[1]*d06_d02[0])]])
R4 = np.array([[(r30[1]*d06_d03[2])-(r30[2]*d06_d03[1])],[(r30[2]*d06_d03[0])-(r30[0]*d06_d03[2])],[(r30[0]*d06_d03[1])-(r30[1]*d06_d03[0])]])
R5 = np.array([[(r40[1]*d06_d04[2])-(r40[2]*d06_d04[1])],[(r40[2]*d06_d04[0])-(r40[0]*d06_d04[2])],[(r40[0]*d06_d04[1])-(r40[1]*d06_d04[0])]])
R6 = np.array([[(r50[1]*d06_d05[2])-(r50[2]*d06_d05[1])],[(r50[2]*d06_d05[0])-(r50[0]*d06_d05[2])],[(r50[0]*d06_d05[1])-(r50[1]*d06_d05[0])]])
# # R = sp.simplify([[R1,R2,R3,R4,R5,R6],
# #                  [r00,r10,r20,r30,r40,r50]])
# #print(R)()
R = sp.Matrix(np.array([[R1.item(0), R2.item(0), R3.item(0), R4.item(0), R5.item(0), R6.item(0)],  
              [R1.item(1), R2.item(1), R3.item(1), R4.item(1), R5.item(1), R6.item(1)],
              [R1.item(2), R2.item(2), R3.item(2), R4.item(2), R5.item(2), R6.item(2)],
              [r00.item(0), r10.item(0), r20.item(0), r30.item(0), r40.item(0), r50.item(0)],
              [r00.item(1), r10.item(1), r20.item(1), r30.item(1), r40.item(1), r50.item(1)],
              [r00.item(2), r10.item(2), r20.item(2), r30.item(2), r40.item(2), r50.item(2)]]) )
# R = np.linalg.inv(R, np.array([[R1.item(0), R2.item(0), R3.item(0), R4.item(0), R5.item(0), R6.item(0)],  
#               [R1.item(1), R2.item(1), R3.item(1), R4.item(1), R5.item(1), R6.item(1)],
#               [R1.item(2), R2.item(2), R3.item(2), R4.item(2), R5.item(2), R6.item(2)],
#               [r00.item(0), r10.item(0), r20.item(0), r30.item(0), r40.item(0), r50.item(0)],
#               [r00.item(1), r10.item(1), r20.item(1), r30.item(1), r40.item(1), r50.item(1)],
#               [r00.item(2), r10.item(2), r20.item(2), r30.item(2), r40.item(2), r50.item(2)]]), out=R, casting="unsafe")               
print(det(R))
# RI = np.linalg.inv(R)
# print(RI)  

# print(det(R)) 


# G = np.array([[],
#               [B],
#               [C],
#               [D],
#               [E],
#               [F]])
# M = np.matmul(R,G)       
# print(M)       

