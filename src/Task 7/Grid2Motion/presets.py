"""
Brief: Module for storing the constants of the grid maker.
"""
# SCREEN & BLOCKS PRESETS
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
NUMBER_OF_BLOCKS_WIDE = int(input('Number of blocks high: '))
NUMBER_OF_BLOCKS_HIGH = int(input('NUmber of blocks wide: '))
BLOCK_HEIGHT = round(SCREEN_HEIGHT/NUMBER_OF_BLOCKS_HIGH)
BLOCK_WIDTH = round(SCREEN_WIDTH/NUMBER_OF_BLOCKS_WIDE)

# USEFUL COLOURS
GREY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (55, 55, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)

TITLE = 'Grid 2 Motion'
GRIDFILE = 'grid.txt'