#!/usr/bin/env python3

import rospy
from dsr_msgs.srv import Movejoint , Movejointresponse

def callback(request):
    return Movejointresponse(request.pos,request.vel,request.acc,request.time,request.radius,request.mode,request.blendType,request.syncType)



def movejoint():
    rospy.init_node("arm_controller_server_py")
    service = rospy.Service("/dsr01a0509/motion/move_joint", Movejoint, callback)



if __name__== '__main__':
    movejoint()