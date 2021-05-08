import time
import math
from easygopigo3 import EasyGoPiGo3
import easygopigo3 as easy
gpg = easy.EasyGoPiGo3()
my_distance_sensor = gpg.init_distance_sensor('AD1')

list = []

def movement(i):
    gpg.drive_cm(i)
    actions.append("The robot has moved " + str(i) + "cm")

def turn(i):
    gpg.turn_degrees(i)
    actions.append("The robot has turned " + str(i) + "degrees")
   
def orbit(i,j):
    gpg.orbit(i,j)
    actions.append("The robot has orbited " + str(i) + "degrees")
  
def print_actions():
    print("Velocity has not changed")
    for i in range(len(list)):
        print("You have" + str(actions[i]))


def destination_free(l_cm):
    condition = (my_distance_sensor.read_mm() >= l_cm*10)
    return condition

# Drawing a square:
length = 30  # Side length

for i in range(4):
    movement(length)  # Drive forward for length cm
    turn(90)  # Rotate 90 degrees to the right

time.sleep(5)  # Time delay between figures

# Drawing a circle:
# uses the .orbit(D, R) command where D is the degrees you'll be
# rotating and R the radius [cm] of said circle.
orbit(360,40)

time.sleep(5)  # Time delay between figures

# Drawing a rectangle
short_side = 30
long_side = 60

for i in range(2):
    movement(short_side) 
    turn(90)
    movement(long_side) 
    turn(90)

time.sleep(5)

# Drawing triangles:
# 1. equilateral triangle of side length 'length'
for i in range(3):
    movement(length) 
    turn(120)
    
time.sleep(5)

# 2. Rectangular triangle
length_one_side = 40
length_other_side = 30
length_hypotenuse = math.sqrt((length_one_side**2)+(length_other_side**2))
movement(length_one_side)
turn(90)
movement(length_other_side)
turn(180-(math.atan(length_one_side/length_other_side))*180/np.pi)
movement(length_hypotenuse)

time.sleep(5)
                     
# Drawing a n-sided polygon given the number of sides:
                     
                    
n = int(input("Introduce the number of sides of the polygon"))
length = int(input("Introduce the length of the sides in cm"))
alpha = 360/n
                     
for v in range(n):
    if destination_free(length):
        movement(length)
        turn(alpha)
    else:
        turn(alpha)
        
print_actions()       
        
