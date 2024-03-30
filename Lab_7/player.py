import pygame
import os


pygame.init()

screen = pygame.display.set_mode((1000, 250))
clock = pygame.time.Clock()

path = r'/home/dmitriy/Music/'
songs = [os.path.join(path, name) for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]

current_song_index = 0
pygame.mixer.music.load(songs[current_song_index])

font = pygame.font.Font(None, 30)
pygame.mixer.music.set_volume(0.5)

is_running = True
is_playing = False

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        pygame.mixer.music.play()
        is_playing = True
    if pressed[pygame.K_DOWN]:
        pygame.mixer.music.stop()
        is_playing = False
    if pressed[pygame.K_LEFT]:
        current_song_index = (current_song_index - 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        if is_playing:
            pygame.mixer.music.play()
    if pressed[pygame.K_RIGHT]:
        current_song_index = (current_song_index + 1) % len(songs)
        pygame.mixer.music.load(songs[current_song_index])
        if is_playing:
            pygame.mixer.music.play()

    pygame.mixer.music.set_volume(0.1)

    if is_playing:
        text = font.render("Currently playing: " + songs[current_song_index], False, (255, 255, 0))
    else:
        text = font.render("Currently NOT playing: " + songs[current_song_index], False, (255, 255, 0))
    screen.fill((0, 0, 0))
    screen.blit(text, (500 - text.get_width() // 2, 125 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(15)
