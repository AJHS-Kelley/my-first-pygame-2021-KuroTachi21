# PyGame Practice, McDonald D'Vonte, 11/29/21 9:12am, v0.1

import pygame, sys
from pygame.locals import * 

# start PyGame
pygame.init()

# Create game window
windowSurface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Hello, world")

# Set Color Values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, , 0)
GREEN = (0, 0, 255)
BLUE = (0, 0, 255)

# Setup Fonts 
basicFont = pygame.font.Sys Font(None, 48)

