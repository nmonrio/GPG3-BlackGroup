import pygame
import sys
import math
from pygame.locals import *
import time
import easygopigo

gpg = easy.EasyGoPiGo3()


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
    p = 1
    i = 1
    for vector in range(n):
        for m in range(n):
            if grid[vector][m] == p:
                p += 1
    i = p
    position_y = y//celda+1
    print(position_x)
    print(position_y)
    grid[position_x-1][position_y-1] = p

def clicar():
    # while event.type != MOUSEBUTTONUP:
    a = pygame.mouse.get_pos()[0]
    b = pygame.mouse.get_pos()[1]
    hola(a, b)

def submit():
    print(grid)
    movement()
    time.sleep(50)
    running = False
    pygame.quit()
    sys.exit()


def movement():
    k = 1
    gpg.set_speed(50)
    while k <= p:
        n = len(grid)
        final = 
        for i in range(n):
            for j in range(n):
                if grid[i][j] == k:
                    vector = (i, j)
                    initial = (0, 0)
                    x_diff = (initial[0]-final[0])*100
                    y_diff = (initial[1]-final[1])*100
                    gpg.orbit(math.atan(x_diff/y_diff))
                    t0 = time.time()
                    t_diff= 0
                    gpg.forward()
                    T = (i**2+j**2)**0.5/50
                    while t_diff < T:
                        t_diff = t0-time.time()
                    gpg.stop()    
        k += 1           

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
