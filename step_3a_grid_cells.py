import pygame, sys

pygame.init() # make pygame available for 
#add Green and Dark Green
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24) 
#add cell size and number of cells 
cell_size = 30
number_of_cells = 25

# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values 
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))# blank canvas

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
#when run, this looks the same as the previous because it is only a
# structural change 