import sys
import pygame

width = 700
height = 700


def draw_grid(screen, n):
    row = col = n
    row_width = width // row
    col_height = height // col
    x = y = 0
    # Draw vertical and horizontal lines:
    for i in range(row):
        x += row_width
        pygame.draw.line(screen, pygame.color("black"), (x, 0), (x, height))

    for i in range(col):
        y += col_height
        pygame.draw.line(screen, pygame.color("black"), (0, y), (width, y))


def initialize_grid(n):
    """
    Method for initialising screen from pygame.
    :return surface: Surface instance as new screen pop-up.
    """
    pygame.init()
    surface = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Grid 2 Motion')
    surface.fill(pygame.color('white'))
    draw_grid(surface, n)
    return surface


def grid_loop(surface):
    """
    Initialises screen loop.
    :param surface: Surface instance from pygame.
    """
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


def main():
    width = 700
    height = 700
    fps = 60
    fps_clock = pygame.time.Clock()
    n = int(input('Select grid size: '))
    surface = initialize_grid(n)
    grid_loop(surface)

if


