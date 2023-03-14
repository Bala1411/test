#!/usr/bin/env python3

import rospy
import os
import threading, time 
import sys
import rosservice
#import socket
#from multiprocessing import Process
import keyboard
sys.dont_write_bytecode = True
sys.path.append( os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../../common/imp")) ) # get import path : DSR_ROBOT.py 

# for single robot 
ROBOT_ID     = "dsr01"
ROBOT_MODEL  = "a0509"
import DR_init
DR_init.__dsr__id = ROBOT_ID
DR_init.__dsr__model = ROBOT_MODEL
from DSR_ROBOT import *
from dsr_msgs.srv import *

old = time.time()

# def shutdown():
#     print("shutdown time!")
#     pub_stop.publish(stop_mode=STOP_TYPE_HOLD)
#     return 0

#is_paused = False

#def toggle_pause():
    #code.interact(banner='Paused. Press r to continue.', local = globals())

#while True:
    #global is_paused
#if keyboard.read_key() == "e":
 #   if is_paused == True:
  #     is_paused = False
   # else:
 #   is_paused = True

#wn = __name__
#wn.listen() 
#KeyboardInterrupt.(toggle_pause,"p") 
          

 #   toggle_pause() 
# def move_pause_service():
#     rospy.wait_for_service('/dsr01a0509/motion/move_pause')
#     move_pause = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/motion/move_pause', MovePause) 
#     response = move_pause()

# def move_resume_service():
#     rospy.wait_for_service('/dsr01a0509/motion/move_resume')
#     move_resume = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/motion/move_resume', MoveResume) 
#     response = move_resume
def movement():
    change_operation_speed(100) 
    movej(p1, vel=80, acc=50)
    movej(p2, vel=80, acc=50)
    moveresume()
    movejx(x1, vel=80, acc=80, sol=2)
    movel(x2, velx, accx)
    movec(c1, c2, velx, accx)
    movesj(qlist, vel=100, acc=100)
    movesx(xlist, vel=100, acc=100)
    movej(p2, vel=60, acc=30)
    current = time.time()
    print(f'Time taken is {current-old}')
# def pause_service():
#     move_pause=rospy.ServiceProxy('/dsr01a0509/motion/move_pause',MovePause)
#     response= move_pause({})
# def resume_service():
#     move_resume= rospy.ServiceProxy('/dsr01a0509/motion/move_resume',MoveResume)        
#     response= move_resume({})

if __name__ == "__main__":

    # rospy.init_node('first_control_py')
    # rospy.on_shutdown(shutdown)
    # set_robot_mode  = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/system/set_robot_mode', SetRobotMode)
    # pub_stop = rospy.Publisher('/'+ROBOT_ID +ROBOT_MODEL+'/stop', RobotStop, queue_size=10)
    # set_robot_mode(ROBOT_MODE_AUTONOMOUS)
    #rospy.wait_for_service('/dsr01a0509/motion/move_pause')
   # move_pause = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'/motion/move_pause', MovePause)         
   # move_resume = rospy.ServiceProxy('/'+ROBOT_ID +ROBOT_MODEL+'motion/move_resume', MoveResume) 
   # move_pause()
    #move_resume()

    set_velx(30,20)  # set global task speed: 30(mm/sec), 20(deg/sec)
    set_accx(60,40)  # set global task accel: 60(mm/sec2), 40(deg/sec2)

    velx=[50, 50]
    accx=[100, 100]

    p1= posj(0,0,0,0,0,0)                    #joint
    p2= posj(20, 0.0, 90.0, 0.0, 90.0, 0.0) #joint

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
    movement()
            
    
    
    

                

                
            
    
                


    #p.listen()

    #p.run()
    #a =input( 'press p')
    #os.wait(a)
    #if p.is_alive():
       #p.kill()
        

    


    

     


         
                           
                
        #finally:
            #if keyboard.is_pressed("r"):
               #rospy.wait_for_service('/dsr01a0509/motion/move_resume')
        #finally:
            #if keyboard.is_pressed("s"):
           # movement()    

            

            

        


        
        
  
        #keyboard.wait('space')
        #os.system("pause") 
        #os.system("""bash -c 'read -s -n 1 -p "Press any Key to continue..."'""")
#while True:
           #if keyboard.is_pressed("p"):
              #print("Pause is pressed")
             # wait.input(keyboard.is_pressed("p"))
             # print("Resume is pressed")
             # movement()
             #continue
           #else:
           # movement()
           # continue          
