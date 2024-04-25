import pygame, sys, random
from pygame.math import Vector2

pygame.init() 
GREEN = (173, 204, 96)
DARK_GREEN = (43, 51, 24) 
cell_size = 30
number_of_cells = 25

class Food:
    def __init__(self):
       # self.position = Vector2(5,6)
       self.position = self.generate_random_pos()

    def draw(self):
      
       food_rect = pygame.Rect(self.position.x * cell_size, self.position.y * cell_size, cell_size, cell_size)

       screen.blit(food_surface, food_rect)

    def generate_random_pos(self):
        x = random.randint(0, number_of_cells - 1)
        y = random.randint(0, number_of_cells - 1)
        position = Vector2(x,y)
        return position 

class Snake: 
    def __init__(self):
        self.body = [Vector2(6,9), Vector2(5,9), Vector2(4,9)]
    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7) # make snake cells rounded - 7 as border radius of rect 
screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))# blank canvas

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock() # controls the frame rate of the game 

food = Food()
snake = Snake() 
food_surface = pygame.image.load("graphics/food.png")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    
    screen.fill(GREEN)
    food.draw()
    snake.draw()
    pygame.display.update()
    clock.tick(60)
# when run, the snack will appear rounded 