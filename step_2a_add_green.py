import pygame, sys

pygame.init() # make pygame available for 
#add Green and Dark Green
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24) 

screen = pygame.display.set_mode((750,750))# blank canvas

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock() # controls the frame rate of the game 

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fill screen with GREEN
    screen.fill(GREEN)
    pygame.display.update()
    clock.tick(60)
#when run, this presents a green screen