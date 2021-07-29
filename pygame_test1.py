import pygame
import sys
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

arrow_y = 480

fpsClock = pygame.time.Clock()
FPS = 60

isArrowRun = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        #if target_rect.x > screen.get_width():
        #    target_rect.x = 0
        #else:
        #    target_rect.x += 5

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                    arrow_y = 480#화살의 시작 위치
                    isArrowRun = True#화살 움직이기 시작

    if isArrowRun:#True일때만
        arrow_y -= 10#움직이기
        if arrow_y < 0:#화면을 벗어나면
            isArrowRun = False#화살 움직이기끝

    screen.fill((WHITE))
    #screen.blit(target_img, target_rect)
    #screen.blit(arrow_img, (arrow_x, arrow_y))
    pygame.draw.circle(screen, BLACK, (320, arrow_y), 20)#화살 출력

    pygame.display.update()
    fpsClock.tick(FPS)
