import time
import math
from easygopigo3 import EasyGoPiGo3
import easygopigo3 as easy
gpg = easy.EasyGoPiGo3()

gpg = EasyGoPiGo3()  # Create object instance of the robot

# Drawing a square:
length = 30  # Side length

for i in range(4):
    gpg.drive_cm(length)  # Drive forward for length cm
    gpg.turn_degrees(90)  # Rotate 90 degrees to the right

time.sleep(5)  # Time delay between figures

# Drawing a circle:
# uses the .orbit(D, R) command where D is the degrees you'll be
# rotating and R the radius [cm] of said circle.
gpg.orbit(360, 40)

# Drawing a rectangle
short_side = 30
long_side = 60

for i in range(2):
    gpg.drive_cm(short_side)
    gpg.turn_degrees(90)
    gpg.drive_cm(long_side)
    gpg.turn_degrees(90)

time.sleep(5)

# Drawing triangles:
# 1. equilateral triangle of side length 'length'
for i in range(3):
    gpg.drive_cm(length)
    gpg.turn_degrees(120)

# 2. Rectangular triangle
length_one_side = 60
length_other_side = 30
if a > b:
    legnth_hypotenuse = math.sqrt((length_one_side**2)+(length_other_side**2)))
    gpg.drive_cm(length_one_side)
    gpg.turn_degrees(90)
    gpg.drive_cm(legnth_other_side)
    gpg.turn_degrees(180-math.atan(length_one_side/legnth_other_side)
    gpg.drive(length_hypotenuse)


# Drawing a n-sided polygon given the number of sides:
n = int(input("Introduce the number of sides of the polygon"))
length = int(input("Introduce the length of the sides in cm"))
security_distance = gpg.init_distance_sensor()
 
while security_distance.read_cm()>30:
    for v in range(n):
            gpg.drive_cm(length)
            gpg.turn_degrees(360/n)) 
    
while security_distance.read_cm() <=30:
    gpg.turn_degrees(90)
        

