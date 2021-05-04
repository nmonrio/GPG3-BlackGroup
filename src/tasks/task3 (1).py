#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  4 17:04:27 2021

@author: hvpboy
"""

import easygopigo3 as easy
import numpy as np

gpg = easy.EasyGoPiGo3()
gpg_servo = gpg.init_servo('SERVO1')

my_distance_sensor = gpg.init_distance_sensor('AD2')

n=int(input("Enter the number of scans required--->"))
while n<4:
    print("Minimum value admitted is 4")
    n=int(input("Enter the number of scans required--->"))
    
dist=int(input("Enter the minimum distance at which the obstacle is detected (between 10/20 cm)--->"))
while dist<10:
    print("Not valid entry")
    dist=int(input("Enter the minimum distance at which the obstacle is detected (between 10/20 cm)--->"))
    
dgr = 360/n
end = False

def forward_until_obstacle():
    gpg.forward()
    while my_distance_sensor.read_mm()>120:
        pass
    gpg.stop()

def destination_free():
    condition = my_distance_sensor.read_mm()>dist*10
    return condition
 
def surround():
    i=1
    while i<21 and destination_free():
        gpg.orbit(-dgr/20, dist+5)
        gpg_servo.rotate_servo(90+i*90/20)
        i+=1
    gpg_servo.rotate_servo(0) #izquierda mirando objeto
    

def identify_obstacle():
    scans = 0
    verify=True
    gpg.turn_degrees(90) #circular path
    while destination_free() and scans < n and verify:
        surround()
        if (my_distance_sensor.read_mm() <= dist*10):
            scans += 1
        else:
            verify=False
    return scans == n

if __name__ == "__main__":
    while not end:
        forward_until_obstacle()
        if identify_obstacle():
            print("Sentinel Identified Object")
            end = True
        else:
            gpg.turn_degrees(100)
            gpg_servo.rotate_servo(90)