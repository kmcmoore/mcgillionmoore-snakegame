import pygame, sys

pygame.init() # make pygame available for 

screen = pygame.display.set_mode((750,750))# blank canvas

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock() # controls the frame rate of the game 

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)
#when run, this presents a black screen.