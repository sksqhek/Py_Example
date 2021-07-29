from random import randrange

import pygame
import sys

padWidth = 800
padHeight = 600
done = False
is_blue = True
x = padWidth* 0.45
y = padHeight * 0.9
screen = pygame.display.set_mode((padWidth, padHeight))
clock = pygame.time.Clock()

img = pygame.image.load("player.png")

rect = img.get_rect()
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
    pygame.display.set_caption('다른 이미지 여러개 랜덤으로 움직이기')

    # 이미지 로딩
 #player = pygame.image.load('player.png')#64x64 크기의 이미지

    objects[0].setImage(pygame.image.load('player.png'))
    objects[1].setImage(pygame.image.load('player.png'))
    objects[2].setImage(pygame.image.load('player.png'))
    objects[3].setImage(pygame.image.load('player.png'))
    objects[4].setImage(pygame.image.load('player.png'))

    clock = pygame.time.Clock()

def runGame():
    global player, clock, x

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

        #whilw문 제거
        rect.left = x
        rect.top = y

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            if x > 10:#왼쪽 벽 보다 클때만
                x -= 10
        if pressed[pygame.K_RIGHT]:
            if x < 800 - rect.w:#오른쪽 벽보다(이미지 크기만큼 빼줌) 작을때만
                x += 10

        screen.fill((0, 0, 0))
        screen.blit(img, rect)

        for ob in objects:#저장된 이미지 만큼
            gamePad.blit(ob.img, (ob.currentPoint[0], ob.currentPoint[1]))  # 이미지 화면에 출력

        pygame.display.update()
        clock.tick(60)

# 게임 실행
initGame()
runGame()