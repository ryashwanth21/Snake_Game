import pygame
import time
import random

# Initialize pygame
pygame.init()

# Window dimensions
width = 600
height = 400

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Create the game window
screen = pygame.display.set_mode((width, height))

# Set Title and Icon
pygame.display.set_caption('Enhanced Snake Game')

# Clock to control game speed
c = pygame.time.Clock()

snake_block = 10
snake_speed = 15

# Fonts
font_style = pygame.font.SysFont("calibri", 50)
score_font = pygame.font.SysFont("calibri", 20)

# Load sound effects
eat_sound = pygame.mixer.Sound("eat.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)  # Play background music in a loop


def Your_score(score):
    """Display the score on screen."""
    value = score_font.render(f"Your Score: {score}", True, black)
    screen.blit(value, [0, 0])


def snake(snake_block, snake_list):
    """Draw the snake on the screen."""
    for x in snake_list:
        pygame.draw.rect(screen, green, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    """Display a message in the center of the screen."""
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Global variable for snake speed
snake_speed = 15

# Function for game loop
def gameLoop():
    global snake_speed  # Access the global snake_speed variable
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Defining food parameters
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    # Game Loop
    running = True
    while running:

        while game_close:
            screen.fill((0, 0, 0))
            message("You Lost!", (255, 0, 0))
            pygame.display.update()

        # Event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change -= snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change += snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change -= snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change += snake_block
                    x1_change = 0

        # Setting boundaries
        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen.fill((255, 255, 255))

        # Drawing the food
        pygame.draw.rect(screen, (0, 0, 0), [foodx, foody, snake_block, snake_block])

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # Check if the snake hits itself
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # Check if the snake eats the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            # Increase the speed gradually, capped at 30
            snake_speed = min(30, snake_speed + 0.1 * Length_of_snake)

        c.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
