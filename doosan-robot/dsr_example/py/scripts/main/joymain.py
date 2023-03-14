#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import mqtt_msg_subscriber

def main():
  mqtt_msg_subscriber.start()

if __name__ == "__main__": 
  while not rospy.is_shutdown():
    main()
   
   
  