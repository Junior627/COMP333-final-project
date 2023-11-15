import sys
import pygame

import constants

# initialize pygame
pygame.init()

# create game window
screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
pygame.display.set_caption("The Aurora Armada")

pygame.quit()
sys.exit()