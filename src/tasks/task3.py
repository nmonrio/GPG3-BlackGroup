import numpy as np
import time
import easygopigo3 as easy

gpg = easy.EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor('AD2')

#Sentinel
n=int(input("Enter the number of scans required--->"))
while n<4:
    print("Minimum value admitted is 4")
    n=int(input("Enter the number of scans required--->"))
dist=int(input("Enter the minimum distance at which the obstacle is detected (between 10/20 cm)--->"))
while dist<10:
    print("Not valid entry")
    dist=int(input("Enter the minimum distance at which the obstacle is detected (between 10/20 cm)--->"))

def safety_distance():
    return (my_distance_sensor.read_mm() > 50)

def obstacle():
    return (my_distance_sensor.read_mm() <= dist*10)

def wall():
    return (my_distance_sensor.read_mm() <= l*10)



veryfying = False
detected = False
dgr=360/n
alpha=(180-90-dgr/2)
l=2*(dist+5)*np.cos(alpha)+12

while not detected:
    while safety_distance() and not veryfying:
        gpg.forward()
        if obstacle():
            gpg.stop()
            veryfying = True
            scans=1
    while safety_distance() and veryfying:
        gpg.turn_degrees(alpha)
        if wall():
            gpg.turn_degrees(90)
            veryfying = False
        elif not wall():
            gpg.turn_degrees(90-alpha) #right: to put gpg on circular path
            gpg.orbit(-dgr, dist+5)
            gpg.turn_degrees(-90) #left: to focus on obstacle direction
            if obstacle() and scans<n:
                scans+=1
                veryfying = True
            else:
                veryfying = False
    while not safety_distance():
        gpg.turn_degrees(90)
    if scans==n:
        detected = True
if detected:
    gpg.stop()
    print("Sentinel detected an obstacle")
