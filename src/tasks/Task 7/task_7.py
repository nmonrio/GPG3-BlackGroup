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

p = 1
def hola(x, y):
    celda = 400//n
    position_x = x//celda+1
    i = 1
    for vector in range(n):
        for m in range(n):
            if grid[vector][m] == p:
                p += 1
    i = p
    position_y = n-y//celda
    print(position_x)
    print(position_y)
    grid[position_y-1][position_x-1] = p

def clicar():
    # while event.type != MOUSEBUTTONUP:
    a = pygame.mouse.get_pos()[0]
    b = pygame.mouse.get_pos()[1]
    hola(a, b)

def submit():
    print(grid)
    movement()
    time.sleep(10)
    running = False
    pygame.quit()
    sys.exit()


def movement(grid):
    k = 1
    gpg.set_speed(255)
    initial = [0,0]
    final = [0, 0]
    while True:
        n = len(grid)
        initial = final
        angle = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == k:
                    final = [j, i]
                    x_diff = (final[0]-initial[0])*100
                    y_diff = (final[1]-initial[1])*100
                    print("y_diff:",y_diff)
                    print("x_diff:",x_diff)
                    distance = (x_diff**2+y_diff**2)**0.5/10
                    if y_diff == 0: 
                        if x_diff < 0:
                            angle = -90
                        elif x_diff > 0:
                            angle = 90
                    elif x_diff == 0:
                        if y_diff > 0: angle = 0
                        elif y_diff < 0: angle = 180
                    else: angle = math.atan(x_diff/y_diff)*180/3.1415
                    print(round(angle,3))
                    print(distance)
                    gpg.orbit(angle,0)
                    #wait_seconds(2)
                    gpg.drive_cm(distance)
                    #gpg.forward()
                    #wait_seconds((i**2+j**2)**0.5/50*factor)
                    gpg.stop()
                    gpg.orbit(-angle,0)
                    print(-angle)
                    time.sleep(3)
                    #wait_seconds(5)
        k += 1


def wait_seconds(my_time):
    t0 = time.time()
    t_diff= 0
    while t_diff < my_time:
        t_diff = time.time()-t0
        gpg.forward()
        print(round(t_diff,5), end = "\r")
    print("Waited",t_diff,"seconds")

def string_to_list(string_list):
    l = string_list.split("[")
    l = [ [i.strip("],")] for i in l if i]
    for j in range(len(l)):
        l[j] = l[j][0].split(",")
        for k in range(len(l[j])):
            try:
                l[j][k] = int(l[j][k].strip("], "))
            except:
                l[j].remove(l[j][k])
    return l

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
