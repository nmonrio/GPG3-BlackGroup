import pygame as pg
import sys
from pygame.locals import *
import numpy as np

height = 1000
width = 600

pg.init()



if __name__=="__main__":
	n = int(input("Tell  me precission (5-50): "))
	while n < 5 or n > 50:
		n = int(input("Tell  me precission (5-50): "))
	if n > 5 and n < 50:
		robot = pg.image.load("robot.png")



		screen = pg.display.set_mode((height, width))
		pg.display.set_caption("Movement")
		pg.display.set_icon(robot)


		screen.fill(pg.Color("black"))

		pg.display.update()
		clock = pg.time.Clock()

		i = 0
		running = True
		while running == True:
			clock.tick(60) 
			for event in pg.event.get(): 
				if event.type == pg.QUIT: sys.exit()
				elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
					#running = False

					#x, y = 128, 128
					robot = pg.transform.scale(robot, (128, 128))
					screen.blit(robot, (64, 64))
					pg.display.update()
				pg.display.update()
			pg.display.update()
		pg.display.update()
