import pygame
pygame.init()

size = (1280, 1024)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Red ball")

x = 640
y = 512
speed = 2

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [x, y], 25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if x < 50:
        x = 50
    if x > 950:
        x = 950
    if y < 50:
        y = 50
    if y > 950:
        y = 950
 
    pygame.display.flip()
pygame.quit
