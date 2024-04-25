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
        self.direction = Vector2(1,0)

    def draw(self):
        for segment in self.body:
            segment_rect = (segment.x * cell_size, segment.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, DARK_GREEN, segment_rect, 0, 7)

    def update(self):
        self.body = self.body[:-1]
        self.body.insert(0, self.body[0] + self.direction)

screen = pygame.display.set_mode((cell_size * number_of_cells, cell_size * number_of_cells))# blank canvas

pygame.display.set_caption("560 Snake Game")

clock = pygame.time.Clock() # controls the frame rate of the game 

food = Food()
snake = Snake()
food_surface = pygame.image.load("graphics/food.png")

SNAKE_UPDATE = pygame.USEREVENT # create special event
pygame.time.set_timer(SNAKE_UPDATE, 200) # trigger SNAKE_UPDATE every 200 milliseconds 

#game loop
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:
            snake.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN: # if a key has been pressed 
            if event.key == pygame.K_UP: # if user pressed UP arrow 
                snake.direction = Vector2(0, -1)
            if event.key == pygame.K_DOWN: # if user pressed DOWN arrow
                snake.direction = Vector2(0, 1)
            if event.key == pygame.K_LEFT: # if user pressed LEFT arrow
                snake.direction = Vector2(-1,0)
            if event.key == pygame.K_RIGHT: # if user pressed RIGHT arrow 
                snake.direction = Vector2(1,0)

  
    screen.fill(GREEN)
    food.draw()
    snake.draw()
    pygame.display.update()
    clock.tick(60)
# when run, snake will now move in coordination with user keys 