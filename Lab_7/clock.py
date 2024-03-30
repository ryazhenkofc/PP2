import pygame
from datetime import datetime

pygame.init()

SIZE = (1280, 1024)
CLOCK_IMG_PATH = r'/home/dmitriy/Documents/Code/PP2/Lab_7/clock.png'
LEFT_HAND_IMG_PATH = r'/home/dmitriy/Documents/Code/PP2/Lab_7/hand1.png'
RIGHT_HAND_IMG_PATH = r'/home/dmitriy/Documents/Code/PP2/Lab_7/hand2.png'

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Clock")

clock_img = pygame.image.load(CLOCK_IMG_PATH)
left_hand_img = pygame.image.load(LEFT_HAND_IMG_PATH)
right_hand_img = pygame.image.load(RIGHT_HAND_IMG_PATH)

done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    now = datetime.now()
    hours = now.hour
    minutes = now.minute

    left_hand_rotated = pygame.transform.rotate(left_hand_img, minutes * -6)
    right_hand_rotated = pygame.transform.rotate(right_hand_img, hours * -30 + minutes * -0.5)

    screen.blit(clock_img, (0, 0))
    screen.blit(left_hand_rotated, (705 - left_hand_rotated.get_width() // 2, 525 - left_hand_rotated.get_height() // 2))
    screen.blit(right_hand_rotated, (705 - right_hand_rotated.get_width() // 2, 525 - right_hand_rotated.get_height() // 2))

    pygame.display.flip()

pygame.quit()
