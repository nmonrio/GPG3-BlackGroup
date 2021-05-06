import pygame
pygame.init()

screen = pygame.display.set_mode((800,600))

#TITLE AND STUFF
pygame.display.set_caption("Robot Movement")
icon = pygame.image.load("robot.png")
pygame.display.set_icon(icon)



if __name__=="__main__":
	n = int(input("Tell me precission: "))
	
	#this mixes red, green, blue; need valid combination, look in internet; white is 255 all, and black is all 0
	screen.fill((255, 255, 255))
	pygame.display.update()

	running = True
	while running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False