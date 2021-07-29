from random import randrange

import pygame
import sys

padWidth = 800
padHeight = 600

class Object:

    def __init__(self):
        self.targetPoint = [0, 0]
        self.currentPoint = [400, 300]
        self.isrun = False

    def setImage(self, img):
        self.img = img

objects = [Object(),Object(),Object(),Object(),Object()]

def initGame():
    global gamePad, player, clock
    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('Test')

    # 이미지 로딩
    #player = pygame.image.load('player.png')#64x64 크기의 이미지

    objects[0].setImage(pygame.image.load('player.png'))
    objects[1].setImage(pygame.image.load('1.gif'))
    objects[2].setImage(pygame.image.load('2.gif'))
    objects[3].setImage(pygame.image.load('player.png'))
    objects[4].setImage(pygame.image.load('player.png'))

    clock = pygame.time.Clock()

def runGame():
    global player, clock

    while True:
        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

        gamePad.fill((0, 0, 0))

        for ob in objects:

            if ob.isrun == False:#움직임이 끝나면
                ob.targetPoint[0] = randrange(0, padWidth - 64)
                ob.targetPoint[1] = randrange(0, padHeight - 64)#목표 위치 만들기
                ob.isrun = True
            else:
                if ob.targetPoint[0] - ob.currentPoint[0] > 0:#목표 위치로 이동
                    ob.currentPoint[0] += 1
                elif ob.targetPoint[0] - ob.currentPoint[0] < 0:
                    ob.currentPoint[0] -= 1

                if ob.targetPoint[1] - ob.currentPoint[1] > 0:#목표 위치로 이동
                    ob.currentPoint[1] += 1
                elif ob.targetPoint[1] - ob.currentPoint[1] < 0:
                    ob.currentPoint[1] -= 1

                if ob.targetPoint[0] - ob.currentPoint[0] == 0 and ob.targetPoint[1] - ob.currentPoint[1] == 0:
                    ob.isrun = False#목표 위치로 도착했다면

            gamePad.blit(ob.img, (ob.currentPoint[0], ob.currentPoint[1]))  # 이미지 화면에 출력

        pygame.display.update()
        clock.tick(60)


# 게임 실행
initGame()
runGame()