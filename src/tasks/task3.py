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
alpha = (180-90-dgr/2)
l = 2*(dist+5)*np.cos(alpha)+12
end = False

def forward_until_obstacle():
    gpg.forward()
    increase_speed()
    while my_distance_sensor.read_mm()>120:
        pass
    gpg.stop()

def destination_free():
    condition=True
    gpg_servo.rotate_servo(90+alpha)
    while condition:
        if my_distance_sensor.read_mm() < l*10:
            condition=False
    gpg_servo.rotate_servo(90)
        
    return condition

def identify_obstacle():
    scans = 0
    veryfy=True
    while destination_free() and scans < n and veryfy:
        gpg.turn_degrees(90) #right: to put gpg on circular track
        gpg.orbit(-dgr, dist+5)
        gpg_servo.rotate_servo(0) #left: to focus on obstacle direction
        if (my_distance_sensor.read_mm() <= dist*10):
            scans += 1
        else:
            gpg_servo.rotate_servo(90)
            veryfy=False
    return scans == n

if __name__ == "__main__":
    while not end:
        forward_until_obstacle()
        if identify_obstacle():
            print("Sentinel Identified Object")
            end = True
        else:
            gpg.turn_degrees(100) 