import pygame
import random
import sys


## 함수 선언 부분 ##
# 기능 :객채를 화면에 그리는 기능
def paintEntity(entity, x, y):
    monitor.blit(entity, (x, y))


# 기능:점수를 화면에 나타내는 기능
def writeScore(score):
    myfont = pygame.font.Font('NanumGothic.ttf', 20)
    txt = myfont.render(u'파괴한 우주괴물 수: ' + str(score), True, (255 - r, 255 - g, 255 - b))
    monitor.blit(txt, (10, sheight - 40))


def playGame():
    global monitor, ship, monster, missile

    r = random.randrange(0, 256)
    g = random.randrange(0, 256)
    b = random.randrange(0, 256)

    # 우주선의 이동량을 정하기
    shipX = swidth / 2
    shipY = sheight * 0.8
    dx, dy = 0, 0

    # 기능:우주괴물을 랜듬으로 스폰하고 크기 위치 설정
    monster = pygame.image.load(random.choice(monsterImage))
    monsterSize = monster.get_rect().size
    monsterX = 0
    monsterY = random.randrange(0, int(swidth * 0.3))
    monsterSpeed = random.randrange(1, 5)

    # 기능:미사일 좌표
    missileX, missileY = None, None

    # 기능:맞춘 우주괴물 숫자를 저장
    fireCount = 0

    # 반복
    while True:
        (pygame.time.Clock()).tick(50)
        monitor.fill((r, g, b))

        # 키보드나 아무스가 들어오는지 체크
        for e in pygame.event.get():
            if e.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            # 기능:방향키로 조작
            if e.type in [pygame.KEYDOWN]:
                if e.key == pygame.K_LEFT:
                    dx = -5
                elif e.key == pygame.K_RIGHT:
                    dx = +5
                elif e.key == pygame.K_UP:
                    dx = -5
                elif e.key == pygame.K_DOWN:
                    dx == +5

                # 스페이스바를 누른다면 미사일을 발사하기
                elif e.key == pygame.K_SPACE:
                    if missileX == None:
                        missileX = shipX + shipSize[0] / 2

                        # 우주선의 위치에서 미사일을 발사
                        missileY = shipY

            # 방향키를 떼면 우주선이 멈추는 기능
            if e.type in [pygame.KEYUP]:
                if e.key == pygame.K_LEFT or e.key == pygame.K_RIGHT \
                        or e.key == pygame.K_UP or e.key == pygame.K_DOWN: dx, dy = 0, 0

        # 기능:우주선이 화면 안에서만 이동
        if (0 < shipX + dx and shipX + dx <= swidth - shipSize[0]) \
                and (sheight / 2 < shipY + dy and shipY + dy <= sheight - shipSize[1]):
            shipX += dx
            shipY += dy
        paintEntity(ship, shipX, shipY)

        # 기능:우주괴물이 자동으로 나타나 이동한다.
        monsterX += monsterSpeed
        if monsterX > swidth:
            monsterX = 0
            monsterY = random.randrange(0, int(swidth * 0.3))
            # 우주괴물의 이미지를 랜덤으로 선택
            monster = pygame.image.load(random.choice(monsterImage))
            monsterSize = monster.get_rect().size
            monsterSpeed = random.randrange(1, 5)

        paintEntity(monster, monsterX, monsterY)

        # 기능:미사일을 화면에 나타내게 하기.
        if missileX != None:
            missileY -= 10
            if missileY < 0:
                missileX, missileY = None, None
        if missileX != None:
            paintEntity(missile,missileX, missileY)
            # 명중체크
            if (monsterX < missileX and missileX < monsterX + monsterSize[0]) and \
                    (monsterY < missileY and missileY < monsterY + monsterSize[1]):
                fireCount += 1

                # 이미지를 다시 준비하기
                monster = pygame.image.load(random.choice(monsterImage))
                monsterSize = monster.get_rect().size
                monsterY = random.randrange(0, int(swidth * 0.3))
                monsterSpeed = random.randrange(1, 5)

                # 미사일 초기화
                missileX, missileY = None, None

        writeScore(fireCount)

        pygame.display.update()


# 전역 변수 선언
r, g, b = [0] * 3
swidth, sheight = 500, 700
monitor = None
ship, shipSize = None, 0

monsterImage = ['monster01.png', 'monster02.png', 'monster03.png', 'monster04.png', \
                'monster05.png', 'monster06.png', 'monster07.png', 'monster08.png', \
                'monster09.png', 'monster10.png']

monster = None
missile = None

# 메인 코드 부분 #
pygame.init()
monitor = pygame.display.set_mode((swidth, sheight))
pygame.display.set_caption('우주괴물 무찌르기')

ship = pygame.image.load('ship02.png')
shipSize = ship.get_rect().size

missile = pygame.image.load('missile.png')

playGame()