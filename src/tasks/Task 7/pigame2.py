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

    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP or event.type == MOUSEBUTTONDOWN:
            		print(pygame.mouse.get_pos())
            		pygame.display.update()

        pygame.display.update()


def drawGrid():
    blockSize = WINDOW_WIDTH//n #Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)

def paint():
	x, y = pygame.mouse.get_pos()
	print(x, y)
	return x, y

if __name__=="__main__":
	n = int(input("Tell me precission (5-50): "))
	while n > 50 or n < 5:
		n = int(input("Tell me precission (5-50): "))
	for i in range(n):
		rows.append(0)
	for i in range(n):
		grid.append(rows)
	print(grid)
	main()