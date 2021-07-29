import pygame
from random import randint

pygame.init()
white = 230, 230, 230
black = 25, 25, 25
winSize = width, height = 400, 300
clock = pygame.time.Clock()
FPS = 60

class Block(pygame.sprite.Sprite):
    def __init__(self, key_left, key_right):  # 왼쪽키, 오른쪽키를 받음....
        super().__init__()
        size = [80, 10]  # 기본블록 가로80, 세로10 (튜플로 정의해도 되고, 생성자때 변환해도 됨)
        self.image = pygame.Surface(size)
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = width // 2 - self.image.get_width()  # 기본 x좌표.. 화면의 중앙
        self.rect.y = height - 30  # 기본 y좌표.. 아래쪽에서 조금 떨어진곳
        self.key_left = key_left
        self.key_right = key_right

    def update(self, speed):  # 블록의 이동
        if pygame.key.get_pressed()[self.key_left]:
            if self.rect.left > 0:
                self.rect.x -= (int)(500 * speed)  # speed에 따른 x좌표 수정
        if pygame.key.get_pressed()[self.key_right]:
            if self.rect.right < width:
                self.rect.left += (int)(500 * speed)


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        size = [10, 10]
        self.image = pygame.Surface(size)
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = randint(10, width - 10)
        self.rect.y = 10
        self.directionx = 1
        self.directiony = 1
        self.speed = 5

    def update(self):
        if self.rect.y >= height or self.rect.y <= 0:
            self.directiony *= -1

        if self.rect.x >= width or self.rect.x <= 0:
            self.directionx *= -1
        self.rect.x += (int)(self.directionx * self.speed)
        self.rect.y += (int)(self.directiony * self.speed)


screen = pygame.display.set_mode(winSize)

# 객체생성
myBlock = Block(pygame.K_LEFT, pygame.K_RIGHT)
myBall = Ball()

# life

life = 3

posText = 'Life : ' + str(life)

# GameLoop

onGame = True

while onGame:
    df = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            onGame = False
    screen.fill(black)
    myBlock.update(df)
    myBall.update()

    # 충돌처리
    if pygame.sprite.collide_rect(myBlock, myBall):
        myBall.directionx = (myBall.rect.center[0] - myBlock.rect.center[0]) / 25
        myBall.directiony *= -1
        myBall.speed += 0.5

    # 바닥에 닿았는지 처리
    if myBall.rect.y >= height - 12:
        if (life > 0):
            life -= 1
            myBall.rect.x = randint(10, width - 10)
            myBall.rect.y = 10
            myBall.speed = 5
        else:
            # life가 0이면 게임종료...
            onGame = False
    screen.blit(myBlock.image, myBlock.rect)
    screen.blit(myBall.image, myBall.rect)

    posText = 'Life : ' + str(life)
    font = pygame.font.SysFont("comicsansms", 15)
    text = font.render(posText, True, white)
    textrect = text.get_rect(center=(width - text.get_width() + 15, 15))

    screen.blit(text, textrect)
    pygame.display.flip()
pygame.quit()
