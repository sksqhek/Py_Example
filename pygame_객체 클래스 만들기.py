import pygame

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
        self.image = pygame.image.load('player.png')#pygame.Surface(size)
        #self.image.fill(white)
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


screen = pygame.display.set_mode(winSize)
myBlock = Block(pygame.K_LEFT, pygame.K_RIGHT)  # 객체생성

onGame = True
while onGame:
    df = clock.tick(FPS) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            onGame = False
    screen.fill(black)
    myBlock.update(df)
    screen.blit(myBlock.image, myBlock.rect)
    pygame.display.flip()
pygame.quit()
