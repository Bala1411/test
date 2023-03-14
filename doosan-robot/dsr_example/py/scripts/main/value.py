#!/usr/bin/env python3
import rospy
import mqtt_msg_subscriber 


def linearvalues():
    print('posx:',mqtt_msg_subscriber.robomovement2)

if __name__ == "__main__": 
  while not rospy.is_shutdown():
    linearvalues()
