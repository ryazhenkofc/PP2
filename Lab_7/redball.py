import pygame
pygame.init()

size = (1280, 1024)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Red ball")

x = 640
y = 512
speed = 4

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, [x, y], 25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if x < 50:
        x = 50
    if x > 1230:
        x = 1230
    if y < 50:
        y = 50
    if y > 974:
        y = 974
 
    pygame.display.flip()
pygame.quit
