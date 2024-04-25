import pygame, sys

pygame.init() # make pygame available for 

screen = pygame.display.set_mode((750,750))# set blank canvas of size 750x750 pixels

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock() # controls the frame rate of the game 

#when run, this returns Hello from the Pygame community. There is a canvas,
# but we need the game loop for it to run.