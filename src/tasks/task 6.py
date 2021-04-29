import easygopigo3 as easy
import numpy as np
#define right_rot_cmd   110     //Rotate Right by running both motors is opposite direction
#define left_rot_cmd    98      //Rotate left by running both motors is opposite direction


gpg = easy.EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor('AD2')

def forward_until_obstacle():
    gpg.forward()
    increase_speed()
    while my_distance_sensor.read_mm()>100:
        pass
    gpg.stop()

def destination_free():
    gopigo.set_speed(50)
    gopigo.right_rot() # Rotate left 90º with motors in opposite direction?
    condition = (my_distance_sensor.read_mm() >= 100)
    return condition

if __name__=="__main__":
    end=False
    while not end:
        forward_until_obstacle()
        if not destination_free():
            gpg.turn_degrees(180)
