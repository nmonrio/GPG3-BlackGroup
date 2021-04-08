import time
from easygopigo3 import EasyGoPiGo3

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
    gpg.turn_degrees(60)

# 2. Rectangular triangle
# 3. Another one maybe???

# Drawing a n-sided polygon given the number of sides:
n = 3
