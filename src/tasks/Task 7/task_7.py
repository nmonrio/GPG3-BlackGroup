import pygame
import sys
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

rows = []

grid = []


def main():
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    icon = pygame.image.load("robot.png")
    pygame.display.set_icon(icon)

    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    running = True
    while running == True:
        drawGrid()
        for event in pygame.event.get():
            print("g")
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN: #or event.type == MOUSEBUTTONDOWN:
            	print(pygame.mouse.get_pos())
            	pygame.display.update()
                clicar()
            	print(grid)
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                if event.key == pygame.K_a:
                    print("h")
                    submit()
                    pygame.display.update()
        pygame.display.update()


def drawGrid():
    blockSize = WINDOW_WIDTH//n #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def hola(x, y):
	celda = 400//n
	position_x = x//celda+1
	i = 1
	position_y = y//celda+1
	print(position_x)
	print(position_y)
	grid[position_x-1][position_y-1] = i

def clicar():
   # while event.type != MOUSEBUTTONUP:
    a = pygame.mouse.get_pos()[0]
    b = pygame.mouse.get_pos()[1]
    hola(a, b)

def submit():
    print(grid)
    running = False
    pygame.quit()
    sys.quit()
    

if __name__=="__main__":
	n = int(input("Tell me precission (5-50): "))
	while n > 50 or n < 5:
		n = int(input("Tell me precission (5-50): "))
	for i in range(n):
		rows.append(0)
	for i in range(n):
		grid.append(rows.copy())
	print(grid)
	main()