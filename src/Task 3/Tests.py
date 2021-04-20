import easygopigo3 as easy
import numpy as np

gpg = easy.EasyGoPiGo3()

my_distance_sensor = gpg.init_distance_sensor('AD2')

n = 4
dgr = 360/n
dist = 15
alpha = (180-90-dgr/2)
l = 2*(dist+5)*np.cos(alpha)+12
end = False

def forward_until_obstacle():
    gpg.forward()
    while my_distance_sensor.read_mm()>120:
        pass
    gpg.stop()

def destination_free():
    gpg.turn_degrees(alpha)
    condition = (my_distance_sensor.read_mm() >= l*10)
    #gpg.turn_degrees(-alpha)
    return condition

def identify_obstacle():
    scans = 0
    while destination_free() and scans < n:
        gpg.turn_degrees(90-alpha)
        gpg.orbit(-dgr, dist+5)
        gpg.turn_degrees(-90) #left: to focus on obstacle direction
        if (my_distance_sensor.read_mm() <= dist*10):
            scans += 1
        else:
            break
    return scans == n
    
    

if __name__ == "__main__":
    while not end:
        forward_until_obstacle()
        if identify_obstacle():
            print("Object Identified")
            end = True
        else:
            gpg.turn_degrees(100)        