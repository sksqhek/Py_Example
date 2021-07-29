import pygame

WHITE = (255,255,255)
RED = (255,0,0)

pygame.init()

SIZE = [500,300]

mpos=[]

mdown = False

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("마우스로 그림 그리기")
screen.fill((WHITE))

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mdown = True
        elif event.type == pygame.MOUSEMOTION:
            if mdown:
                mpos.append(event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            mdown = False


    for pos in mpos:
        pygame.draw.circle(screen, RED, pos, 2)

    pygame.display.update()
    clock.tick(60)
pygame.quit()