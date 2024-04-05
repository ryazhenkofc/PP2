import pygame

# Define constants and variables
WIDTH, HEIGHT = 1200, 800
draw = False
lastPos = (0, 0)
radius = 6
color = "black"
mode = "pen"

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Paint")
clock = pygame.time.Clock()
screen.fill(pygame.Color("white"))
font = pygame.font.SysFont("None", 40)


def draw_line(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, pygame.Color(color), (x, y), width)


def draw_circle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    radius = abs(x1 - x2) / 2
    pygame.draw.circle(screen, pygame.Color(color), (x, y), radius, width)


def draw_rectangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    widthr = abs(x1 - x2)
    height = abs(y1 - y2)
    
    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, widthr, height), width)
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, widthr, height), width)
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, widthr, height), width)
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, widthr, height), width)


def draw_square(screen, start, end, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    mn = min(abs(x2 - x1), abs(y2 - y1))

    if x2 > x1 and y2 > y1:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y1, mn, mn))
    if y2 > y1 and x1 > x2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y1, mn, mn))
    if x1 > x2 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x2, y2, mn, mn))
    if x2 > x1 and y1 > y2:
        pygame.draw.rect(screen, pygame.Color(color), (x1, y2, mn, mn))


def draw_right_triangle(screen, start, end, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    if x2 > x1 and y2 > y1:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if y2 > y1 and x1 > x2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x1, y2)))
    if x1 > x2 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))
    if x2 > x1 and y1 > y2:
        pygame.draw.polygon(screen, pygame.Color(color), ((x1, y1), (x2, y2), (x2, y1)))


def draw_eq_triangle(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]

    width_b = abs(x2 - x1)
    height = (3**0.5) * width_b / 2

    if y2 > y1:
        pygame.draw.polygon(
            screen,
            pygame.Color(color),
            ((x1, y2), (x2, y2), ((x1 + x2) / 2, y2 - height)),
            width,
        )
    else:
        pygame.draw.polygon(
            screen,
            pygame.Color(color),
            ((x1, y1), (x2, y1), ((x1 + x2) / 2, y1 - height)),
        )


def draw_rhombus(screen, start, end, width, color):
    x1 = start[0]
    x2 = end[0]
    y1 = start[1]
    y2 = end[1]
    pygame.draw.lines(
        screen,
        pygame.Color(color),
        True,
        (
            ((x1 + x2) / 2, y1),
            (x1, (y1 + y2) / 2),
            ((x1 + x2) / 2, y2),
            (x2, (y1 + y2) / 2),
        ),
        width,
    )


def render_text(WIDTH, radius, color, mode, screen, font):
    pygame.draw.rect(screen, pygame.Color("white"), (WIDTH - 25, 5, 50, 40))
    pygame.draw.rect(screen, pygame.Color("white"), (0, 0, 350, 50))
    text_size = font.render(str(radius), False, pygame.Color(color))
    current_color = font.render(f"{color} {mode}", False, pygame.Color(color))
    screen.blit(text_size, (WIDTH - 25, 5))
    screen.blit(current_color, (0, 5))

    instructions = [
        "Q - clear",
        "1 - black",
        "2 - green",
        "3 - red",
        "4 - blue",
        "5 - yellow",
        "P - pen",
        "E - eraser",
        "R - rectangle",
        "C - circle",
        "S - square",
        "T - right triangle",
        "U - equilateral triangle",
        "H - rhombus",
        "+ - increase size",
        "- - decrease size",
        "S - Save image",
    ]

    for i, instruction in enumerate(instructions):
        text = font.render(instruction, False, pygame.Color("black"))
        screen.blit(text, (0, 30 + i * 30))

def save_image(screen):
    pygame.image.save(screen, "image.png")


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                mode = "rectangle"
            if event.key == pygame.K_c:
                mode = "circle"
            if event.key == pygame.K_p:
                mode = "pen"
            if event.key == pygame.K_e:
                mode = "erase"
            if event.key == pygame.K_s:
                mode = "square"
            if event.key == pygame.K_q:
                screen.fill(pygame.Color("white"))

            if event.key == pygame.K_1:
                color = "black"
            if event.key == pygame.K_2:
                color = "green"
            if event.key == pygame.K_3:
                color = "red"
            if event.key == pygame.K_4:
                color = "blue"
            if event.key == pygame.K_5:
                color = "yellow"
            if event.key == pygame.K_t:
                mode = "right_tri"
            if event.key == pygame.K_u:
                mode = "eq_tri"
            if event.key == pygame.K_h:
                mode = "rhombus"
            if event.key == pygame.K_KP_PLUS:
                radius = min(200, radius + 1)
            if event.key == pygame.K_KP_MINUS:
                radius = max(1, radius - 1)
            if event.key == pygame.K_s:  
                save_image(screen)

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
            if mode == "pen":
                pygame.draw.circle(screen, pygame.Color(color), event.pos, radius)
            prevPos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if mode == "rectangle":
                draw_rectangle(screen, prevPos, event.pos, radius, color)
            elif mode == "circle":
                draw_circle(screen, prevPos, event.pos, radius, color)
            elif mode == "square":
                draw_square(screen, prevPos, event.pos, color)
            elif mode == "right_tri":
                draw_right_triangle(screen, prevPos, event.pos, color)
            elif mode == "eq_tri":
                draw_eq_triangle(screen, prevPos, event.pos, radius, color)
            elif mode == "rhombus":
                draw_rhombus(screen, prevPos, event.pos, radius, color)
            draw = False

        if event.type == pygame.MOUSEMOTION:
            if draw and mode == "pen":
                draw_line(screen, lastPos, event.pos, radius, color)
            elif draw and mode == "erase":
                draw_line(screen, lastPos, event.pos, radius, "white")
            lastPos = event.pos

    render_text(WIDTH, radius, color, mode, screen, font)
    pygame.display.flip()
