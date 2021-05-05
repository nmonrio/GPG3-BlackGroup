"""
Brief: Module for drawing and creating the grid pop-up.
"""
import pygame
import sys
import presets

#TODO: Create method for changing colour when mouse click on grid tile
#TODO: Create method for storing that position matrix wise as list

# IMPORTED GRID RELATED METHODS
def get_tile_colour(tile_contents):
    """
    Method for retrieving colour from a set of characters. Useful when implementing the task 7 on already created grids
    or paths.

    :param tile_contents: Specific ASCII character contained in each cell.
    :return tile_colour: RGB colour for that specific symbol.
    """
    if tile_contents == 'm':  # BORDER SIGN
        tile_colour = presets.BLACK
    else:
        tile_colour = presets.WHITE

    return tile_colour


def read_grid(gridfile):
    """
    Brief method for reading and segmenting the grid imported.
    :param gridfile: .txt file. Should be in same directory.
    :return: List with the different lines of the grid for its post-processing.
    """
    with open(gridfile, 'r') as f:
        grid_map = f.readlines()
    grid_map = [line.strip() for line in grid_map]
    return [grid_map]


def draw_map(surface, map_tiles):
    """

    :param surface: Surface instance from which the maps is being drawn.
    :param map_tiles:
    :return:
    """
    for j, tile in enumerate(map_tiles):
        for i, tile_contents in enumerate(tile):
            # print('{},{}: {}'.format(i, j, tile_contents))
            my_rect = pygame.Rect(i * presets.BLOCK_WIDTH, j * presets.BLOCK_HEIGHT, presets.BLOCK_WIDTH,
                                  presets.BLOCK_HEIGHT)
            pygame.draw.rect(surface, get_tile_colour(tile_contents), my_rect)


# GENERAL USE METHODS
def initialize_grid():
    """
    Method for initialising screen from pygame.
    :return surface: Surface instance as new screen pop-up.
    """
    pygame.init()
    surface = pygame.display.set_mode((presets.SCREEN_WIDTH, presets.SCREEN_HEIGHT))
    pygame.display.set_caption(presets.TITLE)
    surface.fill(presets.WHITE)
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
        draw_grid(surface)
        pygame.display.update()


def draw_grid(surface):
    """
    Method for drawing grid lines.
    :param surface: Surface instance from which the code will imprint the lines of the grid. Invoked from pygame settings.
    """
    for i in range(presets.NUMBER_OF_BLOCKS_WIDE):
        new_height = round(i * presets.BLOCK_HEIGHT)
        new_width = round(i * presets.BLOCK_WIDTH)
        pygame.draw.line(surface, presets.BLACK, (0, new_height), (presets.SCREEN_WIDTH, new_height), 2)
        pygame.draw.line(surface, presets.BLACK, (new_width, 0), (new_width, presets.SCREEN_HEIGHT), 2)


def main():
    # grid_map = read_grid(presets.GRIDFILE)
    surface = initialize_grid()
    grid_loop(surface)


if __name__ == '__main__':
    main()
