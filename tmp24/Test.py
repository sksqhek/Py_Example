import os
from random import randrange
from tkinter import Tk, Frame, Label, Entry, StringVar

import pygame
import sys

x = 500
y = 500
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

padWidth = 800
padHeight = 600
screen = pygame.display.set_mode((padWidth, padHeight))

pygame.mixer.pre_init(44100,-16,2,512)

pygame.init()

pygame.display.set_caption('다른 이미지 여러개 랜덤으로 움직이기')
clock = pygame.time.Clock()

top_score = []

class inputBox():

    def __init__(self, score):
        self.score = score
        self.root = Tk()
        self.f = Frame(self.root)
        self.f.pack()


        self.root.geometry("300x50+650+800")

        self.root.resizable(False, False)

        self.root.title('게임 점수 이름 입력')  # 타이틀

        self.lbnumber = Label(self.f, text='이름 : ')
        self.lbnumber.grid(row=1, column=1)
        self.number = StringVar()
        self.ennumber = Entry(self.f, textvariable=self.number, width=30)
        self.ennumber.grid(row=1, column=2, columnspan=10)
        self.ennumber.bind('<Return>', self.ProcessEnter)

        self.root.mainloop()

    def ProcessEnter(self, e):
        top_score.append([self.ennumber.get(), self.score])
        self.saveTopScore()

    def saveTopScore(self):
        try:
            #top = sorted(top_score, key=lambda top_score: top_score[1], reverse=True)
            top_score.sort(key=lambda top_score: top_score[1], reverse=True)

            fp = open("score.txt", "w")

            for t in top_score:
                str = "{0} {1}\n".format(t[0], t[1])
                fp.writelines(str)
            fp.close()

            self.f.destroy()
            self.root.destroy()
        except Exception as e:
            print("x",e)

class Game:
    enemys = []#적기 저장
    bullet_player = []#플레이어의 총알 저장
    bullet_enemy = []  # 적기의 총알을 저장할 변수
    explodes = []

    show_effect = []#점수 효과

    name_list = []
    gameover = False
    score = 0
    isInputName = False

    killCount = 0

    def initGame(self):
        self.img_1 = pygame.image.load('explode.png')
        self.img_player = pygame.image.load("player.png")
        self.img_player_bullet = pygame.image.load("fire.png")  #######총알 이미지
        self.img_enemy_bullet = pygame.image.load("fire2.png")  #######총알 이미지
        self.img_explode = pygame.image.load("explode.png").convert()  #######폭발 이미지

        self.img_enemy = pygame.image.load('enemy.png')

        self.img_enemys = pygame.transform.scale(self.img_enemy, (32, 16))

        self.img_boss = pygame.transform.scale(self.img_enemys,(256, 128))

        self.img_explode2 = pygame.transform.scale(self.img_explode, (256, 256))

        self.img_right_bottom = pygame.image.load('target.jpg')

        self.img_back = pygame.image.load("back.png")

        self.player = Player(pygame.K_LEFT, pygame.K_RIGHT, self.img_player)

        #사운드 로딩
        self.sounds=[pygame.mixer.Sound('1.wav'), \
                     pygame.mixer.Sound('2.wav'), \
                     pygame.mixer.Sound('3.wav'), \
                     pygame.mixer.Sound('4.wav'), \
                     pygame.mixer.Sound('5.wav'),\
                     pygame.mixer.Sound('6.wav')]
        self.sound_shot = pygame.mixer.Sound('shot.wav')

    def runGame(self):
        add_enemy_cnt = 0
        rnd = 0
        rnd2 = randrange(0,11)
        prev_tick = pygame.time.get_ticks()

        while True:
            df = clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type in [pygame.QUIT]:
                    pygame.quit()
                    sys.exit()

                if self.gameover == True:#게임 오바일 경우
                    if event.type == pygame.KEYDOWN:  # 키를 누루면
                        if event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        elif event.key == pygame.K_y:
                            self.gameover = False
                            self.player.player_life = 100;
                            self.score = 0
                            self.enemys.clear()
                            self.bullet_enemy.clear()
                            self.isInputName = False

                #################################
                # 스페이스를 누루면 총알 발사
                if event.type == pygame.KEYDOWN:  # 키를 누루면
                    if event.key == pygame.K_SPACE:
                        self.sound_shot.play()
                        self.bullet_player.append(Bullet(self.img_player_bullet,int(self.player.rect.left + (self.player.rect.width / 2)), self.player.rect.top, -5))
                #################################

            if self.gameover == True:
                font = pygame.font.Font('TaeFont TSTJktB.ttf', 50)
                text = font.render("Game Over", True, (155, 155, 155))
                screen.blit(text, (250,250))

                font = pygame.font.Font('TaeFont TSTJktB.ttf', 20)
                text = font.render("'y' key press again game", True, (155, 155, 155))
                screen.blit(text, (260, 300))

                font = pygame.font.Font('TaeFont TSTJktB.ttf', 20)
                text = font.render("[ESC] key press   exit game", True, (155, 155, 155))
                screen.blit(text, (250, 330))


                if self.isInputName == False:
                    inputBox(self.score)
                    self.isInputName = True
                else:
                    font = pygame.font.Font('TaeFont TSTJktB.ttf', 30)
                    text = font.render(">Top Score<", True, (0, 155, 155))
                    screen.blit(text, (550, 150))
                    for i in range(0,len(top_score)):
                        if i == 10:
                            break
                        str = "{0}. {1} {2}".format(i+1, top_score[i][0], top_score[i][1])
                        font = pygame.font.Font('TaeFont TSTJktB.ttf', 20)
                        text = font.render(str, True, (0, 155, 155))
                        screen.blit(text, (570, 185+(i*25)))

                pygame.display.update()
                clock.tick(60)

                continue

            #############적기가 5개 보다 작다면 적기 생성##############
            if add_enemy_cnt < 0 and len(self.enemys) < 5 + int(self.score / 100):#100점마다 1개더 생성
                rnd = randrange(0,10) + 1
                #rnd2 = randrange(0,len(self.name_list))

                if self.killCount >= 10:
                    self.killCount = 0
                    self.enemys.append(Enemy(self.img_boss, 0, self.sounds[5]))
                else:
                    self.enemys.append(Enemy(self.img_enemys, rnd, self.sounds[rnd%5]))

                if self.score != 0:
                    level_value = self.score / 10#점수가 많아질수혹 생성시간 줄어듬
                else:
                    level_value = 0

                add_enemy_cnt = randrange(int(50 - level_value), int(100 - level_value))
            ######################################################

            #pressed = pygame.key.get_pressed()
            #if pressed[pygame.K_LEFT]:
            #    if self.player.rect.left > 10:  # 왼쪽 벽 보다 클때만
            #        self.player.rect.left -= 10
            #if pressed[pygame.K_RIGHT]:
            #    if self.player.rect.left < 800 - self.player.rect.width:  # 오른쪽 벽보다(이미지 크기만큼 빼줌) 작을때만
            #        self.player.rect.left += 10
            self.player.update(df)

            #################################
            for b in self.bullet_player:  #플레이어 총알 움직이기
                b.update(df)
                if b.rect.top < 0:
                    self.bullet_player.remove(b)

            for b in self.bullet_enemy:  # 적기의 총알 움직이기
                b.update(df)
                if b.rect.top > padWidth:
                    self.bullet_enemy.remove(b)
            ###################################

            ##########총알 적 충돌검사#############
            for e in self.enemys:
                if(e.update(df) == True):#적기 움직이기
                    self.bullet_enemy.append(
                        Bullet(self.img_enemy_bullet,int(e.rect.left + (e.rect.width / 2)), e.rect.top, 3))

                for b in self.bullet_player:  # 총알과 적기 충돌 검사
                    if pygame.sprite.collide_rect(e, b):
                        e.sound.play()
                        self.bullet_player.remove(b)
                        e.life -= 1

                        if e.life <= 0:
                            self.killCount += 1

                            if e.type == 0:
                                self.explodes.append(Explode(self.img_explode2, e.rect.left, e.rect.top))
                            else:
                                self.explodes.append(Explode(self.img_explode, e.rect.left, e.rect.top))
                            #self.show_effect.append(Show_Effect(e.rect.left, e.rect.top, e.getName()))

                            self.enemys.remove(e)

                            if e.type == 0:
                                if e.type == rnd2:
                                    self.score += 100
                                    self.show_effect.append(Show_Effect(e.rect.left, e.rect.top, "+100"))
                                else:
                                    self.score -= 100
                                    self.show_effect.append(Show_Effect(e.rect.left, e.rect.top, "-100"))
                            else:
                                if e.type == rnd2:
                                    self.score += 20
                                    self.show_effect.append(Show_Effect(e.rect.left, e.rect.top, "+20"))
                                else:
                                    self.score -= 10
                                    self.show_effect.append(Show_Effect(e.rect.left, e.rect.top, "-10"))

            for b in self.bullet_enemy:  # 적기의 총알과 플레이어 충돌 검사
                if pygame.sprite.collide_rect(self.player, b):
                    self.sounds[1].play()
                    self.bullet_enemy.remove(b)
                    self.player.player_life -= 10

            for e in self.explodes:#폭발 에니메이션이 끝나면 리스트에서 제거
                e.update()
                if e.EXPLODE_COUNT < 0:
                    self.explodes.remove(e)

            for s in self.show_effect:#점수 이펙트 에니메이션이 끝나면 리스트에서 제거
                s.update()
                if s.count < 0:
                    self.show_effect.remove(s)
            ###################################
            if self.player.player_life <= 0:  # 플레이어의 체력이 0보다 작으면 종료
                self.explodes.append(Explode(self.img_explode, self.player.rect.left, self.player.rect.top))
                self.sounds[0].play()
                self.gameover = True

            screen.fill((0, 0, 0))
            
            # 배경 그리기
            screen.blit(self.img_back, self.img_back.get_rect())

            #점수 출력
            str = "score:{0}".format(self.score)
            font = pygame.font.Font('TaeFont TSTJktB.ttf', 30)  # 폰트 설정
            text = font.render(str, True, (190, 190, 190))  # 텍스트가 표시된 Surface 를 만듬
            screen.blit(text, (10,10))  # 화면에 표시

            # 플레이어의 라이프 그려주기
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(550, 10, int(self.player.player_life / 100 * 200), 30))

            str = "100/{0}".format(self.player.player_life)
            font = pygame.font.Font('TaeFont TSTJktB.ttf', 30)  # 폰트 설정
            text = font.render(str, True, (255, 0, 255))  # 텍스트가 표시된 Surface 를 만듬
            screen.blit(text, (600, 10))  # 화면에 표시

            if self.player.player_life > 0:
                screen.blit(self.player.image, self.player.rect)

            #적기 그리기
            for e in self.enemys:
                screen.blit(e.image, e.rect)
                if e.type != 0:
                    str = "{0}".format(e.type)
                    font = pygame.font.Font('TaeFont TSTJktB.ttf', 15)  # 폰트 설정
                    text = font.render(str, True, (255, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
                    screen.blit(text, (e.rect.left+10, e.rect.top))  # 화면에 표시

            #폭발 그리기
            for e in self.explodes:
                e.image.set_colorkey((255,255,255))  # 투명색
                e.image.set_alpha(e.EXPLODE_COUNT * 2)  # 투명도
                screen.blit(e.image, e.rect)

            #점스 이펙트 그리기
            for s in self.show_effect:
                s.draw()

            #플레이어의 총알 그리기
            for b in self.bullet_player:
                screen.blit(b.image, b.rect)

            #적기의 총알 그리기
            for b in self.bullet_enemy:
                screen.blit(b.image, b.rect)

            #오른쪽 하단 이미지(생성되는 적기 출력)
            #screen.blit(self.img_enemys[rnd2], (700, 550))

            if rnd2 == 0:
                screen.blit(self.img_enemy, (700, 550))
            else:
                screen.blit(self.img_right_bottom, (700, 550))
                str = "{0}".format(rnd2)
                font = pygame.font.Font('TaeFont TSTJktB.ttf', 30)  # 폰트 설정
                text = font.render(str, True, (255, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
                screen.blit(text, (720, 560))  # 화면에 표시



            if pygame.time.get_ticks() - prev_tick > 10000:
                while True:
                    tmp = randrange(0,11)
                    if tmp != rnd2:
                        rnd2 = tmp
                        break

                prev_tick = pygame.time.get_ticks()

            pygame.display.update()
            #clock.tick(60)
            add_enemy_cnt -= 1


class Player(pygame.sprite.Sprite):
    def __init__(self, key_left, key_right, img_player):
        super().__init__()

        self.player_life = 100
        self.image = img_player
        self.rect = self.image.get_rect()

        self.rect.left = int(padWidth * 0.45)
        self.rect.top = int(padHeight * 0.9)

        self.key_left = key_left
        self.key_right = key_right

    def update(self, df):
        if pygame.key.get_pressed()[self.key_left]:
            if self.rect.left > 0:
                #self.rect.x -= 10
                self.rect.x -= int(300 * df)
        if pygame.key.get_pressed()[self.key_right]:
            if self.rect.right < padWidth:
                #self.rect.left += 10
                self.rect.x += int(300 * df)



class Enemy(pygame.sprite.Sprite):

    def __init__(self, img_enemy, type, sound):
        self.targetPoint = [0, 0]
        self.isrun = False

        self.image = img_enemy  # 적기 그림
        self.rect = self.image.get_rect()

        self.rect.left = randrange(0, padWidth - 64)
        self.rect.top = -64

        self.rect.height =  int(self.rect.height * 0.5)#충돌 부분을 줄임

        self.add_bullet_cnt = 0

        self.type = type

        self.sound = sound

        self.life = 5

        if type == 0:
            self.life = 10

    def update(self, df):

        if self.isrun == False:  # 움직임이 끝나면
            self.targetPoint[0] = randrange(0, padWidth - 64)
            self.targetPoint[1] = randrange(0, padHeight - 64)  # 목표 위치 만들기
            self.isrun = True
        else:
            if self.targetPoint[0] - self.rect.left > 0:  # 목표 위치로 이동
                #self.rect.left += 1
                self.rect.left += int(100*df)
            elif self.targetPoint[0] - self.rect.left < 0:
                #self.rect.left -= 1
                self.rect.left -= int(100*df)

            if self.targetPoint[1] - self.rect.top > 0:  # 목표 위치로 이동
                #self.rect.top += 1
                self.rect.top += int(100 * df)
            elif self.targetPoint[1] - self.rect.top < 0:
                #self.rect.top -= 1
                self.rect.top -= int(100 * df)

            if self.targetPoint[0] - self.rect.left == 0 and self.targetPoint[1] - self.rect.top == 0:
                self.isrun = False  # 목표 위치로 도착했다면

        self.add_bullet_cnt -= 2

        if self.add_bullet_cnt < 0:#랜덤 시간마다 총알 생성(발사)
            self.add_bullet_cnt = randrange(100,200)
            return True

        return False

    def getName(self):
        return "적{0}이름:{1}".format(self.type + 1, self.name)

class Explode(pygame.sprite.Sprite):

    EXPLODE_COUNT = 100  # 폭발 그림 지속 시간

    def __init__(self, img_explode, x, y):
        super().__init__()

        self.image = img_explode
        self.rect = self.image.get_rect()

        self.rect.left = x
        self.rect.top = y

    def update(self):
        self.EXPLODE_COUNT -= 1  # 폭발 시간 감소

class Bullet(pygame.sprite.Sprite):
    def __init__(self, img_bullet, x, y, vely):
        super().__init__()

        self.image = img_bullet
        self.rect = self.image.get_rect()

        self.rect.left = x
        self.rect.top = y

        self.vely = vely

    def update(self, df):
        self.rect.top += int(self.vely * 100 *df)

class Show_Effect():
    def __init__(self, x, y, name):
        #str = "적{0}이름:{1}".format(type + 1, type + 1)
        font = pygame.font.Font('TaeFont TSTJktB.ttf', 30)  # 폰트 설정
        self.text = font.render(name, False, (255, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
        self.text.set_colorkey((255, 255, 255))  # 투명색
        self.count = 250
        self.x = x
        self.y = y

    def update(self):
        self.text.set_alpha(self.count)  # 투명도
        self.count -= 1
        self.y -= 1

    def draw(self):
        screen.blit(self.text, (self.x, self.y))  # 화면에 표시

def loadTopScore():
    try:
        fp = open("score.txt", "r")

        for s in fp.readlines():
            tok = s.split()
            top_score.append([tok[0],int(tok[1])])

        fp.close()
    except:
        pass

# 게임 실행
loadTopScore()


#처음 화면 시작
gameStart = False
img_start = pygame.image.load('start.png')

fp = open("Description.txt", "r")
descripts = []

for li in fp:
    descripts.append(li.strip())

font1 = pygame.font.Font('TaeFont TSTJktB.ttf', 50)  # 폰트 설정
font2 = pygame.font.Font('TaeFont TSTJktB.ttf', 18)  # 폰트 설정


#처음 화면
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:  # 키를 누루면
            if event.key == pygame.K_SPACE:
                gameStart = True
    if gameStart == True:
        break

    screen.blit(img_start, img_start.get_rect())

    #설명서 출력
    text = font1.render(descripts[0], True, (255, 64, 190))  # 텍스트가 표시된 Surface 를 만듬
    screen.blit(text, (200, 10))  # 화면에 표시

    for i in range(1, len(descripts)):
        text = font2.render(descripts[i], True, (190, 190, 190))  # 텍스트가 표시된 Surface 를 만듬
        screen.blit(text, (50, 250+(i*40)))  # 화면에 표시

    pygame.display.update()
#처음 화면 부분 끝


game = Game()
game.initGame()
game.runGame()
