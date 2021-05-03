import easygopigo3 as easy
import numpy as np
from time import sleep

servo_delay = 0.4

gpg = easy.EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor('AD2')
gpg_servo = gpg.init_servo('SERVO1')

slow = 255
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


if __name__=="__main__":
    gpg_servo.rotate_servo(90)
    end=False
    while not end:
        forward_until_obstacle()
        gpg.set_speed(slow)
        if destination_free(180):
            gpg.orbit(90)
        elif destination_free(0):
            gpg.orbit(-90)
        else:
            gpg.orbit(180)
        gpg.set_speed(fast)
        gpg_servo.rotate_servo(90)
        sleep(servo_delay)
