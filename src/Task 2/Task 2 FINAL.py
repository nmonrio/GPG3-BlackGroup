import time
import math
from easygopigo3 import EasyGoPiGo3
import easygopigo3 as easy
gpg = easy.EasyGoPiGo3()
my_distance_sensor = gpg.init_distance_sensor('AD2')

actions = []

def movement(i, actions):
    gpg.drive_cm(i)
    actions.append("The robot has moved " + str(i) + "cm")

def turn(i, actions):
    gpg.turn_degrees(i, actions)
    actions.append("The robot has turned " + str(i) + "degrees")
   
def orbita(i,j,actions):
    gpg.orbit(i,j)
    actions.append("The robot has orbited " + str(i) + "degrees")
  
def print_actions(actions):
    print("Velocity has not changed")
    for i in range(len(actions)):
        print("You have: " + str(actions[i]))


def destination_free(l_cm):
    condition = (my_distance_sensor.read_mm() >= l_cm*10)
    return condition

print("Square ---> 1 \nCircle ---> 2 \nRectangle ---> 3 \nEquilateral triangle ---> 4 \nRectangular triangle ---> 5  \nn-sided polygon ---> 6")
gpg_servo.rotate_servo(90)
command = int(input("Enter your command"))

# Drawing a square:
if command == 1:
    length = int(input("Enter the length of the side"))  # Side length
    for i in range(4):
        movement(length, actions)  # Drive forward for length cm
        turn(90, actions)  # Rotate 90 degrees to the right

# Drawing a circle:
# uses the .orbit(D, R) command where D is the degrees you'll be
# rotating and R the radius [cm] of said circle.
elif command == 2: #circle
    radius = int(input("Enter the radius"))
    orbita(360,40, actions)

#Rectangle
elif command == 3:
    short_side = int(input("Enter the  length of the short side"))
    long_side = int(input("Enter the length of the long side"))
    for i in range(2):
        movement(short_side, actions) 
        turn(90, actions)
        movement(long_side, actions) 
        turn(90, actions)


# Drawing triangles:
# 1. equilateral triangle of side length 'length'
elif command == 4:
    length = int(input("Enter the length of the side"))
    for i in range(3):
        movement(length, actions)
        turn(120, actions)


                
# 2. Rectangular triangle
elif command == 5:
    length_one_side = int(input("Enter the length of one side"))
    length_other_side = int(input("Enter length of one side"))
    length_hypotenuse = math.sqrt((length_one_side**2)+(length_other_side**2))
    movement(length_one_side, actions)
    turn(90, actions)
    movement(length_other_side, actions)
    turn(180-(math.atan(length_one_side/length_other_side))*180/np.pi)
    movement(length_hypotenuse, actions)

                     
# Drawing a n-sided polygon given the number of sides:
                     
elif command == 6:                  
    n = int(input("Introduce the number of sides of the polygon"))
    length = int(input("Introduce the length of the sides in cm"))
    alpha = 360/n
    for v in range(n):
        if destination_free(length, actions):
            movement(length, actions)
            turn(alpha, actions)
        else:
            turn(alpha, actions)

else:
    print("Your input was not valid")
        
print_actions(actions)   
