#!/usr/bin/env python3

import rospy
import os
import threading, time
import sys

sys.dont_write_bytecode = True
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../../common/imp")) ) # get import path : DSR_ROBOT.py 


# for single robot 
ROBOT_ID     = "dsr07"
ROBOT_MODEL  = "a0509"
import DR_init
DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL
from DSR_ROBOT import *



def move_joint_service(pos,vel,acc,time,radius,mode,blendType,syncType):
    
  while not rospy.is_shutdown():
     try:
        move_joint =rospy.ServiceProxy("/dsr01a0509/motion/move_joint", MoveJoint)
        response =  move_joint(pos,vel,acc,time,radius,mode,blendType,syncType)
        #rospy.loginfo(response.result)
     except rospy.ServiceException as e: 
        print("service call failed",e) 
                                             
               
       
            
    
                             

if __name__== '__main__': 
  
   
   #for i in range(0,5): 
     rospy.init_node("arm_controller_client_py")
     rospy.wait_for_service("/dsr01a0509/motion/move_joint")
     pos=(0.0,0.0,0.0+10,0.0,0.0,0.0)
     move_joint_service(pos, vel=(0.0), acc=(0.0), time=(5.0), radius=(0.0), mode=(0), blendType=(0), syncType=(0))
     #time.sleep(0)
    # rospy.wait_for_service("/dsr01a0509/motion/move_joint")
    # pos=(0.0,0.0,0.0,0.0,0.0,0.0)
     #move_joint_service(pos, vel=(0.0), acc=(0.0), time=(2.0), radius=(0.0), mode=(0), blendType=(0), syncType=(0))
     
     #1
    
