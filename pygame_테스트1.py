import random
from math import sqrt

import pygame
import sys

padWidth = 800
padHeight = 600

enemys = []
player_pos = [0, 300, 64, 32]
fires = []

key_status = {"UP":False,"DOWN":False,"LEFT":False,"RIGHT":False}

def drawObject(obj, x, y):
    global gamePad
    gamePad.blit(obj, (x, y))#이미지 화면에 출력

def initGame():
    global gamePad, clock, background, player, enemy, fire

    pygame.init()
    gamePad = pygame.display.set_mode((padWidth, padHeight))
    pygame.display.set_caption('PyShooting')

    #이미지 로딩
    background = pygame.image.load('bgimage2.png')
    player = pygame.image.load('player.png')
    enemy = pygame.image.load('enemy.png')
    fire = pygame.image.load('fire.png')

    clock = pygame.time.Clock()

def createEnemy():
    enemy_pos = [800]
    enemy_pos.append(random.randint(0,600))
    enemys.append(enemy_pos)

def moveEnemy():
    for e in enemys:
        e[0] -= 2
        if e[0] < -64:
            enemys.remove(e)

def createFire():
    fire_pos = [player_pos[0], player_pos[1]]
    fires.append(fire_pos)

def moveFire():
    for f in fires:
        f[0] += 5
        if f[0] > 800:
            fires.remove(f)

def drawAllObject():
    drawObject(background, 0, 0)#배경
    drawObject(player, player_pos[0], player_pos[1])#플레이어

    for e in enemys:#적기
        drawObject(enemy, e[0], e[1])

    for f in fires:#총알
        drawObject(fire, f[0], f[1])

def collisionObject():
    for e in enemys:#플레이어와 적기와 충돌 검사
        dis = (player_pos[0] - e[0]) * (player_pos[0] - e[0]) + \
              (player_pos[1] - e[1]) * (player_pos[1] - e[1])
        dis = sqrt(dis)
        if dis < 32:#두 오브젝트의 거리가 32보다 작으면
            pass#Game Over

    for e in enemys:#총알과 적기 출돌 검사
        for f in fires:
            dis = (f[0] - e[0]) * (f[0] - e[0]) + \
                  (f[1] - e[1]) * (f[1] - e[1])
            dis = sqrt(dis)
            if dis < 32:#두 오브젝트의 거리가 32보다 작으면
                fires.remove(f)#총알 삭제
                enemys.remove(e)#적기 삭제

def runGame():
    onGame = False
    rand_create_fire = random.randint(10,50)
    loof_count = 0;

    while not onGame:

        for event in pygame.event.get():
            if event.type in [pygame.QUIT]:
                pygame.quit()
                sys.exit()

            #키 입력 처리 시작
            if event.type == pygame.KEYDOWN:#키를 누루면
                if event.key == pygame.K_SPACE:
                    createFire()

                if event.key == pygame.K_UP:
                    key_status["UP"] = True
                if event.key == pygame.K_DOWN:
                    key_status["DOWN"] = True
                if event.key == pygame.K_LEFT:
                    key_status["LEFT"] = True
                if event.key == pygame.K_RIGHT:
                    key_status["RIGHT"] = True

            if event.type == pygame.KEYUP:#키를 놓으면면
                if event.key == pygame.K_UP:
                    key_status["UP"] = False
                if event.key == pygame.K_DOWN:
                    key_status["DOWN"] = False
                if event.key == pygame.K_LEFT:
                    key_status["LEFT"] = False
                if event.key == pygame.K_RIGHT:
                    key_status["RIGHT"] = False

        if key_status["UP"]:#해당 키가 눌러져 있다면 플레이어 움직이기
            player_pos[1] -= 1
        if key_status["DOWN"]:
            player_pos[1] += 1
        if key_status["LEFT"]:
            player_pos[0] -= 1
        if key_status["RIGHT"]:
            player_pos[0] += 1
        #키입력 처리 끝

        moveEnemy()#적기 움직이기
        moveFire()#총알 움직이기

        collisionObject()#충돌검사

        drawAllObject()#모든 오브젝트 화면에 그리기

        #적기 생성
        if len(enemys) < 20:#적기가 20개 보다 적으면
            if rand_create_fire == loof_count:#loof_count가 랜덤 숫자와 같아지면
                createEnemy()#적기 생성
                rand_create_fire = random.randint(10,50)#다음 적기 생성될 타이밍
                loof_count = 0
        #적기 생성끝
            loof_count += 1


        pygame.display.update()
        clock.tick(60)
        
#게임 실행
initGame()
runGame()