#!/usr/bin/env python3

import rospy
import sys
import os
import threading
from mqtt_bridge.msg import msgMqttSub
sys.dont_write_bytecode = True
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../../common/imp")) ) 

ROBOT_ID     = "dsr01"        
ROBOT_MODEL  = "a0509"  

import DR_init
DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL
from DSR_ROBOT import *
from DRFC import *
from dsr_msgs.msg import *
from dsr_msgs.srv import *

nameSpaceObj = CDsrRobot(ROBOT_ID, ROBOT_MODEL)
non_linear_robomovement = [0,0,0,0,0,0]
linear_robomovement = [0,0,0,0,0,0]
button_list = [0,0,0,0]
initial_pos = [8.38,3.13,91.75,-1.58,70.29,30]
second_pos = [83.72,36.56,76.01,3.06,71.17,267.66]

rx = 0
ry = 90
rz = 0
new_movement = [0,0,0,0,0,0]
added_movement = [0,0,0,0,0,0]
# get_current_tool_flange_posx() = values

# last_position = get_desired_posj()

# def shutdown():
#     print("shutdown time!")
#     print("shutdown time!")
#     print("shutdown time!")

#     pub_stop.publish(stop_mode=STOP_TYPE_QUICK)
#     return 0

def mqtt_msg_callback(msg_mqtt_sub):

    # getting values from the rosmsg msgMqttSub
    joy_1= round(msg_mqtt_sub.message[0],1)
    joy_2= round(msg_mqtt_sub.message[1],1)
    joy_3= round(msg_mqtt_sub.message[2],1)

    joy_4= 0 #round(msg_mqtt_sub.message[3],1)
    joy_5= 90 #(msg_mqtt_sub.message[4],1)
    joy_6= 0 #round(msg_mqtt_sub.message[5],1)

    button_1 = msg_mqtt_sub.button[0]
    button_2 = msg_mqtt_sub.button[1]
    button_3 = msg_mqtt_sub.button[2]
    button_4 = msg_mqtt_sub.button[3]

    # assingning values to the global varaiables
    new_movement[0] = joy_1
    new_movement[1] = joy_2
    new_movement[2] = joy_3
    new_movement[3] = joy_4
    new_movement[4] = joy_5
    new_movement[5] = joy_6

    button_list[0] = button_1
    button_list[1] = button_2
    button_list[2] = button_3
    button_list[3] = button_4

def msgRobotState_cb(msg):
    msgRobotState_cb.count += 1

    if (0==(msgRobotState_cb.count % 200)): 
        rospy.loginfo("________ ROBOT STATUS ________")
        print("  robot_state           : %d" % (msg.robot_state))
        print("  robot_state_str       : %s" % (msg.robot_state_str))
        print("  solution_space        : %d" % (msg.solution_space))
        print("  current_posx          : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.current_posx[0],msg.current_posx[1],msg.current_posx[2],msg.current_posx[3],msg.current_posx[4],msg.current_posx[5]))
        print("  current_posj          : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.current_posj[0],msg.current_posj[1],msg.current_posj[2],msg.current_posj[3],msg.current_posj[4],msg.current_posj[5]))
      
        rospy.loginfo("_________ROBOT LOG_________")
        level = get_last_alarm().level
        print("level:", str(level))
        group = get_last_alarm().group
        print("group:",  str(group))
        index = get_last_alarm().index
        print("index:",   str(index))
        param = get_last_alarm().param
        print("param:",  str(param))     
    
msgRobotState_cb.count = 0 


def threadSubscriber():
    rospy.Subscriber('/'+ROBOT_ID +ROBOT_MODEL+'/state', RobotState, msgRobotState_cb)
    rospy.spin()


def start():
    rospy.init_node('mqtt_msg_subscriber')
    rospy.Subscriber('/mqtt_sub' , msgMqttSub , callback=mqtt_msg_callback)  
    # pub_stop = rospy.Publisher('/'+ROBOT_ID +ROBOT_MODEL+'/stop', RobotStop, queue_size=10)           


    t1 = threading.Thread(target=threadSubscriber)
    t1.daemon = True
    t1.start()
    # if button_list[1] == 1:
    #     nameSpaceObj.amovejx(linear_robomovement,vel = 5,acc = 5,sol=6)  
    if button_list[1] == 1:
        nameSpaceObj.movej(initial_pos,vel = 50,acc = 50) 

    elif button_list[0] == 1:
        values = list(get_current_tool_flange_posx())
        print("position")
        # print(get_current_tool_flange_posx())

        added_movement[0] = values[0]+new_movement[0]
        added_movement[1] = values[1]+new_movement[1]
        added_movement[2] = values[2]+new_movement[2]
        added_movement[3] = values[3]#+linear_robomovement[0]
        added_movement[4] = values[4]#+linear_robomovement[0]
        added_movement[5] = values[5]#+linear_robomovement[0]
        nameSpaceObj.amovel(added_movement,vel = 80,acc = 80,ref= DR_BASE)   

    elif button_list[2] == 1:
        values = list(get_current_tool_flange_posx())
        print("orientation")
        # print(get_current_tool_flange_posx())

        added_movement[0] = values[0]#+new_movement[0]
        added_movement[1] = values[1]#+new_movement[1]
        added_movement[2] = values[2]#+new_movement[2]
        added_movement[3] = values[3]+(new_movement[0]/4)
        added_movement[4] = values[4]+(new_movement[1]/4)
        added_movement[5] = values[5]#+(new_movement[2]/4)
        nameSpaceObj.amovel(added_movement,vel = 0.5,acc = 0.5,ref= DR_BASE)      
       



    

