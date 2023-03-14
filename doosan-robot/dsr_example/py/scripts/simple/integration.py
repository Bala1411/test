#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import os
from multiprocessing import Process
import threading, time
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
from DRFC import *
from dsr_msgs.msg import *
from dsr_msgs.srv import *


def shutdown():
    print("shutdown time!")
    print("shutdown time!")
    print("shutdown time!")

    pub_stop.publish(stop_mode=STOP_TYPE_QUICK)
    return 0
# def move_pause_service():
#     rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/motion/move_pause', MovePause)    
#     return 0
# s = socket.socket(socket)    
old = time.time()
 

def msgRobotState_cb(msg):
    msgRobotState_cb.count += 1

    if (0==(msgRobotState_cb.count % 300)): 
        rospy.loginfo("________ ROBOT STATUS ________")
        print("  robot_state           : %d" % (msg.robot_state))
        print("  robot_state_str       : %s" % (msg.robot_state_str))
        print("  actual_mode           : %d" % (msg.actual_mode))
        print("  actual_space          : %d" % (msg.actual_space))
        print("  current_posj          : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.current_posj[0],msg.current_posj[1],msg.current_posj[2],msg.current_posj[3],msg.current_posj[4],msg.current_posj[5]))
        print("  current_velj          : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.current_velj[0],msg.current_velj[1],msg.current_velj[2],msg.current_velj[3],msg.current_velj[4],msg.current_velj[5]))
        print("  joint_abs             : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.joint_abs[0],msg.joint_abs[1],msg.joint_abs[2],msg.joint_abs[3],msg.joint_abs[4],msg.joint_abs[5]))
        print("  joint_err             : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.joint_err[0],msg.joint_err[1],msg.joint_err[2],msg.joint_err[3],msg.joint_err[4],msg.joint_err[5]))
        print("  target_posj           : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.target_posj[0],msg.target_posj[1],msg.target_posj[2],msg.target_posj[3],msg.target_posj[4],msg.target_posj[5]))
        print("  target_velj           : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.target_velj[0],msg.target_velj[1],msg.target_velj[2],msg.target_velj[3],msg.target_velj[4],msg.target_velj[5]))    
        print("  current_posx          : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.current_posx[0],msg.current_posx[1],msg.current_posx[2],msg.current_posx[3],msg.current_posx[4],msg.current_posx[5]))
        print("  current_velx          : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.current_velx[0],msg.current_velx[1],msg.current_velx[2],msg.current_velx[3],msg.current_velx[4],msg.current_velx[5]))
        print("  task_err              : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.task_err[0],msg.task_err[1],msg.task_err[2],msg.task_err[3],msg.task_err[4],msg.task_err[5]))
        print("  solution_space        : %d" % (msg.solution_space))
        sys.stdout.write("  rotation_matrix       : ")
        for i in range(0 , 3):
            sys.stdout.write(  "dim : [%d]"% i)
            sys.stdout.write("  [ ")
            for j in range(0 , 3):
                sys.stdout.write("%d " % msg.rotation_matrix[i].data[j])
            sys.stdout.write("] ")
        print ##end line
        print("  dynamic_tor           : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.dynamic_tor[0],msg.dynamic_tor[1],msg.dynamic_tor[2],msg.dynamic_tor[3],msg.dynamic_tor[4],msg.dynamic_tor[5]))
        print("  actual_jts            : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.actual_jts[0],msg.actual_jts[1],msg.actual_jts[2],msg.actual_jts[3],msg.actual_jts[4],msg.actual_jts[5]))
        print("  actual_ejt            : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.actual_ejt[0],msg.actual_ejt[1],msg.actual_ejt[2],msg.actual_ejt[3],msg.actual_ejt[4],msg.actual_ejt[5]))
        print("  actual_ett            : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.actual_ett[0],msg.actual_ett[1],msg.actual_ett[2],msg.actual_ett[3],msg.actual_ett[4],msg.actual_ett[5]))
        print("  sync_time             : %7.3f" % (msg.sync_time))
        print("  actual_bk             : %d %d %d %d %d %d" % (msg.actual_bk[0],msg.actual_bk[1],msg.actual_bk[2],msg.actual_bk[3],msg.actual_bk[4],msg.actual_bk[5]))
        print("  actual_bt             : %d %d %d %d %d " % (msg.actual_bt[0],msg.actual_bt[1],msg.actual_bt[2],msg.actual_bt[3],msg.actual_bt[4]))
        print("  actual_mc             : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.actual_mc[0],msg.actual_mc[1],msg.actual_mc[2],msg.actual_mc[3],msg.actual_mc[4],msg.actual_mc[5]))
        print("  actual_mt             : %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f" % (msg.actual_mt[0],msg.actual_mt[1],msg.actual_mt[2],msg.actual_mt[3],msg.actual_mt[4],msg.actual_mt[5]))

        #print digital i/o
        sys.stdout.write("  ctrlbox_digital_input : ")
        for i in range(0 , 16):
            sys.stdout.write("%d " % msg.ctrlbox_digital_input[i])
        print ##end line
        sys.stdout.write("  ctrlbox_digital_output: ")
        for i in range(0 , 16):
            sys.stdout.write("%d " % msg.ctrlbox_digital_output[i])
        print
        sys.stdout.write("flange_digital_input  : ")
        for i in range(0 , 6):
            sys.stdout.write("%d " % msg.flange_digital_input[i])
        print       

        sys.stdout.write("  flange_digital_output : ")
        for i in range(0 , 6):
            sys.stdout.write("%d " % msg.flange_digital_output[i])
        print
        #print modbus i/o
        sys.stdout.write("  modbus_state          : " )
        if len(msg.modbus_state) > 0:
            for i in range(0 , len(msg.modbus_state)):
                sys.stdout.write("[" + msg.modbus_state[i].modbus_symbol)
                sys.stdout.write(", %d] " % msg.modbus_state[i].modbus_value)
        print

        print("  access_control        : %d" % (msg.access_control))
        print("  homming_completed     : %d" % (msg.homming_completed))
        print("  tp_initialized        : %d" % (msg.tp_initialized))
        print("  mastering_need        : %d" % (msg.mastering_need))
        print("  drl_stopped           : %d" % (msg.drl_stopped))
        print("  disconnected          : %d" % (msg.disconnected))
        
        rospy.loginfo("_________ROBOT LOG_________")
        level = get_last_alarm().level
        print("level:", str(level))
        group = get_last_alarm().group
        print("group:",  str(group))
        index = get_last_alarm().index
        print("index:",   str(index))
        param = get_last_alarm().param
        print("param:",  str(param))
        current = time.time()
        print(f'Time taken is {current-old}')      
    
msgRobotState_cb.count = 0 
def threadSubscriber():
    rospy.Subscriber('/'+ROBOT_ID +ROBOT_MODEL+'/state', RobotState, msgRobotState_cb)
    rospy.spin()
    #rospy.spinner(2) 
     
#sensor function
def sensor():
  print ("called")
  while True:
    
    if (get_digital_input(11) == 0):
            print("triggered")
            change_operation_speed(10)
            break
    else:
         print('normal')
         change_operation_speed(100)
         break 

#force command
def force_compliance():
    print('ok done')
    set_singularity_handling (DR_AVOID)
    set_ref_coord(DR_WORLD)
    task_compliance_ctrl(stx = [100, 100, 100, 10, 10, 10],time = 0.1)
    # set_stiffnessx([100, 100, 300, 100, 100, 100])
    fd = [0, 0, 10, 0, 0, 5]
    fctrl_dir= [1, 1, 1, 1, 1, 1]
    set_desired_force(fd, dir=fctrl_dir, time=1.0, mod=DR_FC_MOD_REL)

#motion command
def movement():
    # movej(p3, vel=60, acc=30)
    # movej(p4, vel=60, acc=30) 
    movel(x2, velx, accx)
    movel(x1, velx, accx)

if __name__ == "__main__":
    rospy.init_node('single_robot_simple_py')
    rospy.on_shutdown(shutdown)
    set_robot_mode  = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/system/set_robot_mode', SetRobotMode)
    # move_pause = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/motion/move_pause', MovePause)
    # move_resume = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/motion/move_resume', MoveResume)
    t1 = threading.Thread(target=threadSubscriber)
    t1.daemon = True
    t1.start()

    pub_stop = rospy.Publisher('/'+ROBOT_ID +ROBOT_MODEL+'/stop', RobotStop, queue_size=10)


    set_robot_mode(ROBOT_MODE_AUTONOMOUS)

    set_velx(30,20)  # set global task speed: 30(mm/sec), 20(deg/sec)
    set_accx(60,40)  # set global task accel: 60(mm/sec2), 40(deg/sec2)

    velx=[50, 50]
    accx=[100, 100]

    # p1= posj(0.0,0.0,90.0,0.0,0.0,0.0)      
    # x1= fkin(p1,DR_WORLD)   
    # print(x1)         #joint
    # p2= posj(50.0, 0.0, 45.0, 45.0, 0.0, 0.0) #joint

    p3 = posj(0.0,0.0,90.0,0.0,90.0,0)
    p4 = posj(60.0,0.0,90.0,0.0,90.0,0.0)
    

    x1= posx(377, -150, 493.0, 158.0, 180.0, -118.0) #task
    x2= posx(228, 320, 450.0, 30.0, -170.0, 35.0) #task
   
    # # x1= posx(409, 491, 155.5, 45, 180, 45) #task
    # x2= posx(350.9, 470.5, 485.5,0.0, 90.0, 0.0) #task
    # A1= ikin(x2,0)
    # print(A1)  
    # x1= posx(409, 491, 155.5, 45, 180, 45) #task
    # p1= ikin(x1,2) 
    # print(p1)   
    # x2= posx(346.9, 413.5, 432.5, 50.0, 120.0, 20.0)
    # p2 = ikin(x2,2)
    # print(p2)
    while rospy is not shutdown:
        P1 = Process(target= movement)
        P1.start()
        P2 = Process(target= force_compliance)
        P2.start()
        P3 = Process(target= sensor)
        P3.start()
        
        P1.join()
        P2.join()
        P3.join()
        


      

           

    

