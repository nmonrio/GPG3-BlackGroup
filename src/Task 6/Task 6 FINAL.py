import easygopigo3 as easy
import numpy as np
import time
from time import sleep

servo_delay = 0.4

gpg = easy.EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor('AD2')
gpg_servo = gpg.init_servo('SERVO1')

fast = 255

def forward_until_obstacle():
    gpg.forward()
    while my_distance_sensor.read_mm()>100:
        pass
    gpg.stop()
    

def destination_free(angle):
    gpg_servo.rotate_servo(angle)
    sleep(servo_delay)
    return (my_distance_sensor.read_mm() >= 100)

start = time.time()
I_may_be_wrong = False

if __name__=="__main__":
    gpg_servo.rotate_servo(90)
    gpg.set_speed(fast)
    finished = False
    while not finished:
        forward_until_obstacle()
        end = time.time()
        if end - start < 2 and I_may_be_wrong == True:
            gpg.orbit(180) # I was wrong
            I_may_be_wrong = False #Now I am not wrong
                     
        elif destination_free(180):
            gpg.orbit(90)
            start = time.time()
            I_may_be_wrong = True
            
        else:
            gpg.orbit(-90)
            
        gpg.set_speed(fast)
        gpg_servo.rotate_servo(90)
        sleep(servo_delay)
