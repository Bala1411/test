#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ##
# @brief    [py example simple] motion basic test for doosan robot
# @author   Kab Kyoum Kim (kabkyoum.kim@doosan.com)   
# TEST 2019-12-09
import rospy
import os
import threading, time
from threading import Thread
import sys
sys.dont_write_bytecode = True
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../../common/imp")) ) # get import path : DSR_ROBOT.py 

# for single robot 
ROBOT_ID     = "dsr01"
ROBOT_MODEL  = "a0509"
import DR_init
DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL
from DSR_ROBOT import *

def shutdown():
    print("shutdown time!")
    pub_stop.publish(stop_mode = STOP_TYPE_HOLD)
    return 0

def move():
   while not rospy.is_shutdown(): 
    #if i in range(0,2):
    movej(p2, vel=60, acc=30)
    movejx(x1, vel=60, acc=60, sol=2)
    movel(x2, velx, accx)
    movec(c1, c2, velx, accx)
    movesj(qlist, vel=100, acc=100)
    movesx(xlist, vel=100, acc=100)
    movej(p2, vel=60, acc=30)
    #move_spiral(rev=1.00, rmax=20.00, lmax=20.00, time=5.00, axis=DR_AXIS_Z, ref=DR_TOOL)
    #move_periodic(amp=[10.00, 0.00, 20.00, 0.00, 0.50, 0.00], period=[1.00, 0.00, 1.50, 0.00, 0.00, 0.00], atime=0.50, repeat=3, ref=DR_BASE)
    print('good bye!')
#t = threading.Thread(target=move)    

def start():
    i = input('enter s to start\n')
    if i == 's':
        move()
        
        #rospy.on_shutdown(shutdown)
def stop():
    while True:
        j = input('enter e to stop\n')
        if j == 'e':
            rospy.on_shutdown(shutdown)
            break
        #stop(DR_HOLD)
        #if t.is_alive():
        #sys.exit('stoped')     
 
if __name__ == "__main__":

    rospy.init_node('single_robot_simple_py')
    #rospy.on_shutdown(shutdown)
    set_robot_mode  = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/system/set_robot_mode', SetRobotMode)

    pub_stop = rospy.Publisher('/'+ROBOT_ID +ROBOT_MODEL+'/stop', RobotStop, queue_size=5)           

    set_robot_mode(ROBOT_MODE_AUTONOMOUS)

    velx=[50, 50]
    accx=[100, 100]

    p1= posj(0,0,0,0,0,0)                    #joint
    p2= posj(0.0, 0.0, 90.0, 0.0, 90.0, 0.0) #joint

    x1= posx(367, 37.6, 540.5, 45, 180, 45) #task
    x2= posx(367, 10, 540.5, 62.0, 180, 62.0) #task

    c1 = posx(367, 40, 540.5, 12, 180, 12)
    c2 = posx(367, 10, 490, 12, 180, 12)


    q0 = posj(0,0,90,0,90,0)
    q1 = posj(10,0,90,10,90,0)
    q2 = posj(0,10,90,10,90,0)
    q3 = posj(0,10,80,0,90,0)
    q4 = posj(0,0,100,0,90,0)
    q5 = posj(20,0,90,20,90,0)
    qlist = [q0, q1, q2, q3, q4, q5]

    x1 = posx(330, 185, 497, 110, 160, 90)
    x2 = posx(360, 185, 497, 110, 160, 90)
    x3 = posx(310, 185, 497, 110, 160, 90)
    x4 = posx(310, 185, 397, 110, 160, 90)
    x5 = posx(310, 185, 397, 110, 160, 90)
    xlist = [x1, x2, x3, x4, x5, x5]


    X1 =  posx(370, 670, 650, 0, 180, 0)
    X1a = posx(370, 670, 400, 0, 180, 0)
    X1a2= posx(370, 545, 400, 0, 180, 0)
    X1b = posx(370, 595, 400, 0, 180, 0)
    X1b2= posx(370, 670, 400, 0, 180, 0)
    X1c = posx(370, 420, 150, 0, 180, 0)
    X1c2= posx(370, 545, 150, 0, 180, 0)
    X1d = posx(370, 670, 275, 0, 180, 0)
    X1d2= posx(370, 795, 150, 0, 180, 0)


    seg11 = posb(DR_LINE, X1, radius=20)
    seg12 = posb(DR_CIRCLE, X1a, X1a2, radius=21)
    seg14 = posb(DR_LINE, X1b2, radius=20)
    seg15 = posb(DR_CIRCLE, X1c, X1c2, radius=22)
    seg16 = posb(DR_CIRCLE, X1d, X1d2, radius=23)
    b_list1 = [seg11, seg12, seg14, seg15, seg16] 

    
    Thread(target = start).start()
    Thread(target = stop).start()
