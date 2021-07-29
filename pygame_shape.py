import pygame
import sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((640, 480))

sel = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_1:
            sel = 1
        if event.type == pygame.KEYDOWN and event.key == pygame.K_2:
            sel = 2
        if event.type == pygame.KEYDOWN and event.key == pygame.K_3:
            sel = 3
        if event.type == pygame.KEYDOWN and event.key == pygame.K_4:
            sel = 4
        if event.type == pygame.KEYDOWN and event.key == pygame.K_5:
            sel = 5

    screen.fill((WHITE))

    if sel == 1:
        pygame.draw.rect(screen, BLACK, [200, 100, 200, 200], 5)
    elif sel == 2:
        pygame.draw.circle(screen, BLACK, [300, 200], 100, 5)
    elif sel == 3:
        pygame.draw.ellipse(screen, BLACK, [150, 150, 300, 100], 10)
    elif sel == 4:
        pygame.draw.line(screen, BLACK, [200, 100], [400, 300], 10)
    elif sel == 5:
        pygame.draw.polygon(screen, BLACK, [[200, 100], [300, 100],
                                            [350,200], [250,300], [210,200]], 10)

    pygame.display.update()

