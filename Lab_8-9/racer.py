import pygame
import random
import time

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define screen 
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RACER")
clock = pygame.time.Clock()


# Load background image
road_image = pygame.image.load(r'/home/dmitriy/Documents/Code/PP2/Lab_8-9/etc/road.png')

# Define score display
score = 0 
score_list = []
score_font = pygame.font.SysFont(None, 50)
game_over_font = pygame.font.SysFont(None, 150)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/home/dmitriy/Documents/Code/PP2/Lab_8-9/etc/player.png").convert()
        self.surf = pygame.Surface((160, 240))
        self.rect = self.surf.get_rect(center=(400, 500))
        self.speed = 5

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.move_ip(0, -self.speed)
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, self.speed)
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.move_ip(-self.speed, 0)
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(self.speed, 0)

    def draw(self):
        self.surf.blit(pygame.transform.scale(self.image, (160, 240)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r'/home/dmitriy/Documents/Code/PP2/Lab_8-9/etc/enemy.png').convert() 
        self.surf = pygame.Surface((160, 240))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, SCREEN_WIDTH - 40), -100)
        )
        self.speed = random.randint(3, 5)
        if len(score_list) > 5:
            self.speed += 3

    def move(self):
        self.rect.move_ip(0, self.speed)

    def draw(self):
        self.surf.blit(pygame.transform.scale(self.image, (160, 240)), (0, 0))
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def remove(self):
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()


class Coin(pygame.sprite.Sprite):
    """
    Represents a coin in the game.

    Attributes:
        surf (pygame.Surface): The surface of the coin.
        rect (pygame.Rect): The rectangle that defines the position and size of the coin.
        speed (int): The speed at which the coin moves.
        is_supercoin (int): Indicates whether the coin is a supercoin (1) or a regular coin (0).
        images (list): A list of images for the coin.
    """

    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((80, 80))
        self.rect = self.surf.get_rect(
            center=(random.randint(0, SCREEN_WIDTH - 40), -100)
        )
        self.speed = random.randint(1, 5)
        self.is_supercoin = random.randint(0, 7)
        self.images = [
            pygame.image.load("/home/dmitriy/Documents/Code/PP2/Lab_8-9/etc/scoin.png").convert(),
            pygame.image.load("/home/dmitriy/Documents/Code/PP2/Lab_8-9/etc/coin.png").convert(),
        ]
        self.supcoin()

    def move(self):
        """
        Moves the coin vertically downwards based on its speed.
        """
        self.rect.move_ip(0, self.speed)

    def draw(self):
        """
        Draws the coin on the screen.
        """
        self.surf.blit(
            pygame.transform.scale(self.image, (80, 80)), (0, 0)
        )
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def remove(self):
        """
        Removes the coin from the game if it goes below the screen.
        """
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

    def supcoin(self):
        """
        Sets the image of the coin based on whether it is a supercoin or a regular coin.
        """
        if self.is_supercoin == 7:
            self.image = self.images[1]
        else:
            self.image = self.images[0]

    def is_sup_coin(self):
        """
        Checks if the coin is a supercoin.

        Returns:
            bool: True if the coin is a supercoin, False otherwise.
        """
        return self.is_supercoin == 7


# Initialize player, enemy, and coin groups
player = Player()
enemies = pygame.sprite.Group([Enemy() for _ in range(4)])
coins = pygame.sprite.Group([Coin() for _ in range(6)])

# Game loop
running = True

while running:
    clock.tick(FPS)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw background
    screen.fill(WHITE)
    screen.blit(pygame.transform.scale(road_image, (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0 % SCREEN_HEIGHT))

    # Update and draw game objects
    player.draw()
    player.move()

    for enemy in enemies:
        enemy.draw()
        enemy.move()
        enemy.remove()

    for coin in coins:
        coin.draw()
        coin.move()
        coin.remove()

    # Spawn new enemies and coins
    if len(enemies) < 4:
        enemies.add(Enemy())

    if len(coins) < 6:
        coins.add(Coin())

    # Check for collisions
    if pygame.sprite.spritecollide(player, enemies, False):
        # Game over
        screen.fill(BLACK)
        game_over_text = game_over_font.render("GAME OVER!", True, RED)
        score_text = score_font.render(f"Your score is {score}", True, RED)
        screen.blit(game_over_text, (65, 250))
        screen.blit(score_text, (100, 400))
        pygame.display.update()
        time.sleep(3)
        running = False

    # Handle coin collection
    for coin in pygame.sprite.spritecollide(player, coins, True):
        if coin.is_sup_coin():
            score += 25
        else:
            score += 5
        score_list.append(score)
        

    # Display score
    score_text = score_font.render(str(score), True, BLACK)
    screen.blit(score_text, (20, 20))

    # Update the display
    pygame.display.update()

pygame.quit()

