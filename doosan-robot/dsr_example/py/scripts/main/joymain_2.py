#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import rospy
import mqtt_2

def main():
  mqtt_2.start()

if __name__ == "__main__": 
  while not rospy.is_shutdown():
    main()
   
   
  