import pygame, sys
from pygame.math import Vector2

pygame.init() 
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24) 
cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
        self.position = Vector2(5,6)

    def draw(self):
       # food_rect = pygame.Rect(x, y, w, h)
       food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)
       # pygame.draw.rect(surface, color, rect)
       # pygame.draw.rect(screen, DARK_GREEN, food_rect)
       screen.blit(food_surface, food_rect)
# screen = pygame.display.set_mode((750,750)) NOTICE: same size but with variables instead of values 
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))# blank canvas

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock() # controls the frame rate of the game 

food = Food()
food_surface = pygame.image.load("graphics/food.png")
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #fill screen with GREEN
    screen.fill(GREEN)
    food.draw()
    pygame.display.update()
    clock.tick(60)
# when run, this will show the food graphic. Problem now is that it is 
# always going to be created at the small spot 