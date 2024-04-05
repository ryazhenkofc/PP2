import pygame
import sys
import copy
import random
import time

# Initialize pygame
pygame.init()

# Set game parameters
resolution = 1000
scale = 50

score = 0
level = 0
SPEED = 10
food_x = 10
food_y = 10

# Set up display
display = pygame.display.set_mode((resolution, resolution))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Define colors
background = (81, 203, 94)
text_color = (0, 0, 0)
red = (255, 0, 0)
snake_colour = (81, 147, 203)
snake_head = (81, 86, 203)
food_colour = (255, 0, 0)


class Snake:
    """
    Represents a snake object in the game.

    Attributes:
    - x (int): The x-coordinate of the snake's head.
    - y (int): The y-coordinate of the snake's head.
    - w (int): The width of the snake's body.
    - h (int): The height of the snake's body.
    - x_dir (int): The direction of movement along the x-axis.
    - y_dir (int): The direction of movement along the y-axis.
    - history (list): A list of coordinates representing the snake's body.
    - length (int): The length of the snake's body.

    Methods:
    - reset(): Resets the snake's attributes to their initial values.
    - show(): Draws the snake on the game display.
    - check_eaten(): Checks if the snake has eaten the food.
    - level_up(): Checks if the snake should level up.
    - grow(): Increases the length of the snake.
    - death(): Checks if the snake has collided with itself.
    - update(): Updates the position of the snake's body.
    """

    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def reset(self):
        self.x = resolution / 2 - scale
        self.y = resolution / 2 - scale
        self.w = 10
        self.h = 10
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1

    def show(self):
        for i in range(self.length):
            color = snake_head if i == 0 else snake_colour
            pygame.draw.rect(
                display, color, (self.history[i][0], self.history[i][1], scale, scale)
            )

    def check_eaten(self):
        return (
            abs(self.history[0][0] - food_x) < scale
            and abs(self.history[0][1] - food_y) < scale
        )

    def level_up(self):
        global level
        if self.length % 5 == 0:
            return True

    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])

    def death(self):
        return any(
            abs(self.history[0][0] - self.history[i][0]) < self.w
            and abs(self.history[0][1] - self.history[i][1]) < self.h
            for i in range(1, self.length)
            if self.length > 2
        )

    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale


class Food:
    def new_location(self):
        global food_x, food_y
        food_x = random.randrange(1, resolution / scale - 1) * scale
        food_y = random.randrange(1, resolution / scale - 1) * scale

    def show(self):
        pygame.draw.rect(display, food_colour, (food_x, food_y, scale, scale))


def show_score():
    font = pygame.font.SysFont(None, 44)
    text = font.render(f"Score: {score}", True, text_color)
    display.blit(text, (50, 50))


def show_level():
    font = pygame.font.SysFont(None, 44)
    text = font.render(f"Level: {level}", True, text_color)
    display.blit(text, (200, 50))




def game_loop():
    global score, level, SPEED

    snake = Snake(resolution / 2, resolution / 2)
    food = Food()
    food.new_location()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                handle_keydown(event, snake)

        if not running:
            break

        update_game_state(snake, food)

        if snake.death():
            handle_game_over(snake)

        wrap_snake_position(snake)

        pygame.display.update()
        clock.tick(SPEED)

    pygame.quit()
    sys.exit()


def handle_keydown(event, snake):
    if event.key == pygame.K_q:
        pygame.quit()
        sys.exit()
    if snake.y_dir == 0:
        if event.key == pygame.K_w:
            snake.x_dir = 0
            snake.y_dir = -1
        elif event.key == pygame.K_s:
            snake.x_dir = 0
            snake.y_dir = 1
    if snake.x_dir == 0:
        if event.key == pygame.K_a:
            snake.x_dir = -1
            snake.y_dir = 0
        elif event.key == pygame.K_d:
            snake.x_dir = 1
            snake.y_dir = 0


def update_game_state(snake, food):
    global score, level, SPEED

    display.fill(background)
    snake.show()
    snake.update()
    food.show()
    show_score()
    show_level()

    if snake.check_eaten():
        food.new_location()
        score += random.randint(1, 5)
        snake.grow()

    if snake.level_up():
        food.new_location()
        level += 1
        SPEED += 3
        snake.grow()


def handle_game_over(snake):
    global score, level

    score = 0
    level = 0
    font = pygame.font.SysFont(None, 100)
    text = font.render("Game Over!", True, red)
    display.blit(text, (300, 500))
    pygame.display.update()
    time.sleep(3)
    snake.reset()


def wrap_snake_position(snake):
    if snake.history[0][0] > resolution:
        snake.history[0][0] = 0
    if snake.history[0][0] < 0:
        snake.history[0][0] = resolution
    if snake.history[0][1] > resolution:
        snake.history[0][1] = 0
    if snake.history[0][1] < 0:
        snake.history[0][1] = resolution


game_loop()
