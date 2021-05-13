import pygame
import sys
import math
from pygame.locals import *
import time
import socket


BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

rows = []

grid = []

HOST = '10.10.10.10'  # The server's hostname or IP address (this is the default)
PORT = 65432  # The port used by the server (this is the default)

#we create the grid, with the size given a
def main():
	global SCREEN, CLOCK
	pygame.init()
	SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
	#we could add an image to the screen, but for that we need to have that .png downloaded in the same destiny, so we are not doing it.
	#icon = pygame.image.load("robot.png")
	#pygame.display.set_icon(icon)
	CLOCK = pygame.time.Clock()
	SCREEN.fill(BLACK)
	#we set the possible events: clicking in the screen will append to the list of the grid the point, and clicking a in the keyboard will send the order of executing the grid
	running = True
	while running == True:
		drawGrid()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == MOUSEBUTTONDOWN: #or event.type == MOUSEBUTTONDOWN:
				print(pygame.mouse.get_pos())
				pygame.display.update()
				clicar(n)
				print(grid)
			elif event.type == pygame.KEYDOWN:
				print(event.key)
				if event.key == pygame.K_a:
					send()
					submit()
					#pygame.display.update()
		#pygame.display.update()


def drawGrid():
	blockSize = WINDOW_WIDTH//n #Set the size of the grid block
	for x in range(0, WINDOW_WIDTH, blockSize):
		for y in range(0, WINDOW_HEIGHT, blockSize):
			rect = pygame.Rect(x, y, blockSize, blockSize)
			pygame.draw.rect(SCREEN, WHITE, rect, 1)
#for corresponging the grid points to the list point we have created the hola() function
#it calculates how wide and tall each cell is, and then, given the position of the mouse when you click the grid, it computes which cell that is, and in which place it corresponds
#in the list
#to append natural numbers and not only 1, we are appending a 0 to a list that helps to count which number is next, by calculating the len of the list.
#it is a rather rude method, but is very reliable
def hola(x, y):
	celda = 400//n
	position_x = x//celda+1
	i = len(numbers)
	position_y = n - y//celda+1
	print(position_x)
	print(position_y)
	grid[position_y-1][position_x-1] = i
	numbers.append(0)

#here we obtain the possition of the mousse when you click the screen, and send it to hola()
#also we paint a circle in the point clicked, to have some sense of what you are drawing
def clicar(n):
	# while event.type != MOUSEBUTTONUP:
	a = pygame.mouse.get_pos()[0]
	b = pygame.mouse.get_pos()[1]
	pygame.draw.circle(SCREEN, (255, 255, 255), (a, b), 200*1.3//n)
	pygame.display.update()
	hola(a, b)


#once the grid is finished and you click -a-, the function submit() makes sure to close all the programs being used, and prints the last version of the grid
def submit():
	print(grid)
	running = False
	pygame.quit()
	sys.exit()
#we have to send the grid to the robot, by converting it to a string
def send():
	s.sendall(bytes(str(grid), 'utf-8'))
	#data = repr(s.recv(1024))
	#print('Received:', data)

if __name__=="__main__":
	numbers = [0]
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	print("Connected")
	#we ask for the precission, which means the numbers of cells we want. More than 50 makes too many lines (because lines don´t reduce their size) and it gets impossible to work with it
	#in any case, if needed that precission, by changing the screen width and height (at the beginning of the code) it could be done.
	n = int(input("Tell me precission (5-50): "))
	while n > 50 or n < 5:
		n = int(input("Tell me precission (5-50): "))
	#we create the grid: an empty list of n lists with n zeroes each. In the grid we will keep all the information necessary to send to the robot.
	for i in range(n):
		rows.append(0)
	for i in range(n):
		grid.append(rows.copy())
	main()
