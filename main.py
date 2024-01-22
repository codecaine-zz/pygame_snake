import pygame
import time
import random

# Initialize Pygame
pygame.init()

# Define color constants
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display width and height
dis_width: int = 800
dis_height: int = 600

# Initialize display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Initialize clock for controlling game speed
clock = pygame.time.Clock()
snake_block: int = 10
snake_speed: int = 30

# Initialize fonts for displaying text
font_style = pygame.font.SysFont(None, 50)
score_font = pygame.font.SysFont(None, 35)

def our_snake(snake_block: int, snake_List: list):
    """
    Draw the snake on the game display.
    """
    for x in snake_List:
        pygame.draw.rect(dis, white, [x[0], x[1], snake_block, snake_block])

def message(msg: str, color: tuple):
    """
    Display a message on the game display.
    """
    mesg = font_style.render(msg, True, color)
    text_width = mesg.get_width()
    text_height = mesg.get_height()
    dis.blit(mesg, [(dis_width - text_width) / 2, (dis_height - text_height) / 2])

def gameLoop():
    """
    Main game loop.
    """
    game_over = False
    game_close = False

    # Initialize snake position
    x1: float = dis_width / 2
    y1: float = dis_height / 2

    # Initialize direction variables
    x1_change: float = 0
    y1_change: float = 0

    # Initialize snake list and length
    snake_List: list = []
    Length_of_snake: int = 1

    # Initialize food position
    foodx: float = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody: float = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

        # Check if snake is out of bounds
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        # Update snake position
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if snake has collided with itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        # Draw snake and update display
        our_snake(snake_block, snake_List)
        pygame.display.update()

        # Check if snake has eaten food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
gameLoop()