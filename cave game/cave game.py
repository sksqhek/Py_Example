import sys
from random import randint
import pygame
from pygame.locals import QUIT, Rect, KEYDOWN, K_SPACE

pygame.init()
pygame.key.set_repeat(5, 5)

SURFACE = pygame.display.set_mode((800, 600))
FPSCLOCK = pygame.time.Clock()


def main():
    '''메인 루틴'''
    walls = 80
    ship_y = 250
    velocity = 0
    score = 0
    slope = randint(1, 6)
    sysfont = pygame.font.SysFont("나눔스퀘어extra", 36)
    ship_image = pygame.image.load("ship.png")
    bang_image = pygame.image.load("bang.png")
    remsg_image = pygame.image.load("remsg.png")
    holes = []
    for xpos in range(walls):
        holes.append(Rect(xpos * 10, 100, 10, 400))
    game_over = False
    remsg_image_check = False

    while True:
        is_space_down = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True
                    # ***추가 시작***
                    if game_over:  # 게임 오버라면 게임 데이터 초기화
                        walls = 80
                        ship_y = 250
                        velocity = 0
                        score = 0
                        slope = randint(1, 6)
                        holes = []
                        for xpos in range(walls):
                            holes.append(Rect(xpos * 10, 100, 10, 400))
                        game_over = False
                        remsg_image_check = False
                    # ***추가 종료***

                    # ***새로 추가 시작***
            elif event.type == pygame.MOUSEBUTTONDOWN:#마우스를 누루면
                if game_over:#게임 오버일 경우
                    reRect = Rect(220,194,360, 190)#다시 시작 사각형 만들기
                    if reRect.collidepoint(event.pos):#마우스가 다시 시작 사각형에 들어오면 게임 초기화
                        walls = 80
                        ship_y = 250
                        velocity = 0
                        score = 0
                        slope = randint(1, 6)
                        holes = []
                        for xpos in range(walls):
                            holes.append(Rect(xpos * 10, 100, 10, 400))
                        game_over = False
                        remsg_image_check = False
                    # ***새로 추가 종료***

        # 내 캐릭터를 이동
        if not game_over:
            score += 10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            # 동굴 스크롤
            edge = holes[-1].copy()
            test = edge.move(0, slope)
            if test.top <= 0 or test.bottom >= 600:
                slope = randint(1, 6) * (-1 if slope > 0 else 1)
                edge.inflate_ip(0, -20)
            edge.move_ip(10, slope)
            holes.append(edge)
            del holes[0]
            holes = [x.move(-10, 0) for x in holes]

            # 충돌?
            if holes[0].top > ship_y or \
                    holes[0].bottom < ship_y + 80:
                game_over = True
                remsg_image_check = True

        # 그리기
        SURFACE.fill((0, 255, 255))
        for hole in holes:
            pygame.draw.rect(SURFACE, (30, 30, 30), hole)
        SURFACE.blit(ship_image, (0, ship_y))
        score_image = sysfont.render("현재 점수: {}".format(score), True, (106, 120, 255))
        SURFACE.blit(score_image, (500, 10))

        if game_over and remsg_image_check:
            SURFACE.blit(bang_image, (0, ship_y - 40))
            SURFACE.blit(remsg_image, (220, 194))

        pygame.display.update()
        FPSCLOCK.tick(15)


if __name__ == '__main__':
    main()
