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

    game_status = "homeGame"

    def initGame(self):
        self.img_1 = pygame.image.load('explode.png')
        self.img_player = pygame.image.load("player.png")
        self.img_player_bullet = pygame.image.load("fire.png")  #######총알 이미지
        self.img_enemy_bullet = pygame.image.load("fire2.png")  #######총알 이미지
        self.img_explode = pygame.image.load("explode.png").convert()  #######폭발 이미지

        self.img_enemys = [pygame.image.load('enemy1.png'),\
                           pygame.image.load('enemy2.png'),\
                           pygame.image.load('enemy3.png'),\
                           pygame.image.load('enemy4.png'),\
                           pygame.image.load('enemy5.png'),\
                           pygame.image.load('enemy6.png')]

        for i in range(0, len(self.img_enemys)):
            self.img_enemys[i] = pygame.transform.scale(self.img_enemys[i], (32, 16))

        self.img_enemys[5] = pygame.transform.scale(self.img_enemys[5],(256, 128))
        self.img_explode2 = pygame.transform.scale(self.img_explode, (256, 256))

        self.img_right_bottom = [pygame.image.load('1.jpg'), \
                                pygame.image.load('2.jpg'), \
                                pygame.image.load('3.jpg'), \
                                pygame.image.load('4.jpg'), \
                                pygame.image.load('5.jpg'),
                                pygame.image.load('enemy6.png')]

        self.img_back = pygame.image.load("back.png")

        self.player = Player(pygame.K_LEFT, pygame.K_RIGHT, self.img_player)

        #사운드 로딩
        self.sounds=[pygame.mixer.Sound('1.wav'), \
                     pygame.mixer.Sound('2.wav'), \
                     pygame.mixer.Sound('3.wav'), \
                     pygame.mixer.Sound('4.wav'), \
                     pygame.mixer.Sound('5.wav'),\
                     pygame.mixer.Sound('6.wav'),\
                     pygame.mixer.Sound('exp2.wav')]
        self.sound_shot = pygame.mixer.Sound('shot.wav')

        #파일에서 이름 로딩
        fp = open('name.txt','r')
        str = fp.read()
        self.name_list = str.split()
        fp.close()

        self.heal = Item(pygame.image.load('heart.png'))#heal
        self.shield = Item(pygame.image.load('shield.png'))  # heal
        self.power = Item(pygame.image.load('power.png'))  # power

        self.img_player_power_bullet = pygame.image.load("fire3.png")

        self.plane2000 = Item(pygame.image.load('2000.png'), 2)
        self.plane3000 = Item(pygame.image.load('3000.png'), 2)
        self.plane4000 = Item(pygame.image.load('4000.png'), 2)

    def drawText(self, text, pos, color):
        text = font1.render(text, True, color)  # 텍스트가 표시된 Surface 를 만듬
        screen.blit(text, pos)  # 화면에 표시

    def run(self):
        while True:
            if self.game_status == "homeGame":
                self.homeGame()
            elif self.game_status == "readyGame":
                self.readyGame()
            elif self.game_status == "shopGame":
                self.shopGame()
            elif self.game_status == "runGame":
                self.runGame()

    def shopGame(self):
        game_2000 = Button(screen, (100, 300), (100, 50), "구입")
        game_3000 = Button(screen, (300, 300), (100, 50), "구입")
        game_4000 = Button(screen, (500, 300), (100, 50), "구입")

        prev_btn = Button(screen, (10, 500), (100, 50), "이전")

        self.plane2000.rect.left = 100
        self.plane2000.rect.top = 200
        self.plane3000.rect.left = 300
        self.plane3000.rect.top = 200
        self.plane4000.rect.left = 500
        self.plane4000.rect.top = 200

        while True:
            money = (self.score / 20) * 100
            gold = "골드:{0}원".format(int(money))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 키를 누루면
                    if event.key == pygame.K_y:
                        self.game_status = "homeGame"
                        self.score = money * 20 / 100
                        return
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 좌클릭 감지
                    if game_2000.rect.collidepoint(event.pos):
                        if money < 2000:
                            break
                        money -= 2000
                        self.player.changePlane(self.plane2000.image)

                    elif game_3000.rect.collidepoint(event.pos):
                        if money < 3000:
                            break
                        money -= 3000
                        self.player.changePlane(self.plane3000.image)

                    elif game_4000.rect.collidepoint(event.pos):
                        if money < 4000:
                            break
                        money -= 4000
                        self.player.changePlane(self.plane4000.image)
                    elif prev_btn.rect.collidepoint(event.pos):
                        self.game_status = "homeGame"
                        self.score = money * 20 / 100
                        return

            screen.fill((0, 0, 0))

            self.drawText(gold, (20,10), (255, 255, 255))

            self.drawText("2000원", (100, 100), (255, 255, 255))
            self.drawText("3000원", (300, 100), (255, 255, 255))
            self.drawText("4000원", (500, 100), (255, 255, 255))
            self.plane2000.draw()
            self.plane3000.draw()
            self.plane4000.draw()
            game_2000.draw()
            game_3000.draw()
            game_4000.draw()

            prev_btn.draw()

            pygame.display.update()

    def homeGame(self):
        game_start = Button(screen, (250,250), (200, 50), "게임시작")
        game_shop = Button(screen, (700, 0), (100, 50), "상점")

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 좌클릭 감지
                    if game_start.rect.collidepoint(event.pos):  # button과 충돌한지 확인
                        self.game_status = "readyGame"
                        return
                    elif game_shop.rect.collidepoint(event.pos):  # button과 충돌한지 확인
                        self.game_status = "shopGame"
                        return

            screen.fill((0, 0, 0))

            money = (self.score / 20) * 100
            gold = "골드:{0}원".format(int(money))
            self.drawText(gold, (20, 10), (255, 255, 255))

            game_start.draw()
            game_shop.draw()
            pygame.display.update()


    def readyGame(self):
        # 처음 화면
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  # 키를 누루면
                    if event.key == pygame.K_SPACE:
                        self.game_status = "runGame"
            if self.game_status == "runGame":
                return

            screen.blit(img_start, img_start.get_rect())

            # 설명서 출력
            text = font1.render(descripts[0], True, (255, 64, 190))  # 텍스트가 표시된 Surface 를 만듬
            screen.blit(text, (200, 10))  # 화면에 표시

            for i in range(1, len(descripts)):
                text = font2.render(descripts[i], True, (190, 190, 190))  # 텍스트가 표시된 Surface 를 만듬
                screen.blit(text, (50, 250 + (i * 40)))  # 화면에 표시

            pygame.display.update()
        # 처음 화면 부분 끝

    def runGame(self):
        add_enemy_cnt = 0
        rnd = 0
        rnd2 = 0
        prev_tick = pygame.time.get_ticks()
        heal_tick = pygame.time.get_ticks()#heal
        shield_tick = pygame.time.get_ticks()#shield
        power_tick = pygame.time.get_ticks()  #power
        self.score = 0

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
                            self.player.player_life = 100
                            #self.score = 0
                            self.enemys.clear()
                            self.bullet_enemy.clear()
                            self.isInputName = False
                            self.game_status = "homeGame"
                            return

                #################################
                # 스페이스를 누루면 총알 발사
                if event.type == pygame.KEYDOWN:  # 키를 누루면
                    if event.key == pygame.K_SPACE:
                        self.sound_shot.play()

                        bullet_img = None
                        if self.player.bullet_demage == 1:
                            bullet_img = self.img_player_bullet
                        elif self.player.bullet_demage > 1:
                            bullet_img = self.img_player_power_bullet
                        self.bullet_player.append(Bullet(bullet_img, int(self.player.rect.left + (self.player.rect.width / 2)), self.player.rect.top, -5))

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
                rnd = randrange(0,5)
                #rnd2 = randrange(0,len(self.name_list))

                if self.killCount > 10:
                    self.killCount = 0
                    self.enemys.append(Enemy(self.img_enemys[5], 5, self.name_list[5], self.sounds[5]))
                else:
                    self.enemys.append(Enemy(self.img_enemys[rnd], rnd, self.name_list[rnd], self.sounds[rnd]))

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
                        e.life -= self.player.bullet_demage

                        if e.life <= 0:
                            self.killCount += 1

                            if e.type == 6:
                                self.explodes.append(Explode(self.img_explode2, e.rect.left, e.rect.top))
                            else:
                                self.explodes.append(Explode(self.img_explode, e.rect.left, e.rect.top))
                            #self.show_effect.append(Show_Effect(e.rect.left, e.rect.top, e.getName()))

                            self.enemys.remove(e)

                            if e.type == 5:
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
                    self.sounds[6].play()
                    self.bullet_enemy.remove(b)
                    if self.player.player_shield > 0:
                        self.player.player_shield -= 10
                    else:
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
                self.sounds[6].play()#exp2.wav파일 플레이
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
                if self.player.player_shield > 0:
                    pygame.draw.circle(screen, (255, 255, 0), [self.player.rect.left+32,self.player.rect.top+16], 32, 2)

            #적기 그리기
            for e in self.enemys:
                screen.blit(e.image, e.rect)

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
            screen.blit(self.img_right_bottom[rnd2], (700, 550))

            if pygame.time.get_ticks() - prev_tick > 10000:
                while True:
                    tmp = randrange(0,6)
                    if tmp != rnd2:
                        rnd2 = tmp
                        break

                prev_tick = pygame.time.get_ticks()

            #heart process
            if pygame.time.get_ticks() - heal_tick > 60000 and self.heal.isrun == False:#heal 60초마다
                self.heal.rect.left = randrange(0, 500-self.heal.rect.width)
                self.heal.rect.top = -self.heal.rect.height#맨위 생성
                self.heal.isrun = True
                heal_tick = pygame.time.get_ticks()#다음 생성을 위해 시간 저장

            if self.heal.isrun == True:
                self.heal.update(df)#하트 움직이기
                self.heal.draw()#하트 그리기
                if pygame.sprite.collide_rect(self.player, self.heal):#플레이어랑 하트 충돌 검사
                    self.player.player_life += 30#라이프를 30증가
                    if self.player.player_life > 100:#100보다 크면
                        self.player.player_life = 100
                    self.heal.isrun = False
            #shield process
            if pygame.time.get_ticks() - shield_tick > 90000 and self.shield.isrun == False:#shield 90초마다
                self.shield.rect.left = randrange(0, 500-self.shield.rect.width)
                self.shield.rect.top = -self.shield.rect.height#맨위 생성
                self.shield.isrun = True
                shield_tick = pygame.time.get_ticks()#다음 생성을 위해 시간 저장

            if self.shield.isrun == True:
                self.shield.update(df)
                self.shield.draw()
                if pygame.sprite.collide_rect(self.player, self.shield):
                    self.player.player_shield += 30#실드 30증가
                    self.shield.isrun = False

            #power process
            if pygame.time.get_ticks() - power_tick > 120000 and self.power.isrun == False:  # power 120초마다
                self.power.rect.left = randrange(0, 500 - self.power.rect.width)
                self.power.rect.top = -self.power.rect.height  # 맨위 생성
                self.power.isrun = True
                power_tick = pygame.time.get_ticks()  # 다음 생성을 위해 시간 저장

            if self.power.isrun == True:
                self.power.update(df)
                self.power.draw()
                if pygame.sprite.collide_rect(self.player, self.power):
                    self.player.bullet_demage += 5
                    self.power.isrun = False

            pygame.display.update()
            #clock.tick(60)
            add_enemy_cnt -= 1

class Button:
    def __init__(self, screen, pos, size, text):
        self.screen = screen
        self.rect = pygame.Rect(pos[0], pos[1], size[0],size[1])
        self.text = text
    def draw(self):
        pygame.draw.rect(self.screen, (255,255,255), self.rect)
        text = font1.render(self.text, True, (0, 0, 0))  # 텍스트가 표시된 Surface 를 만듬
        screen.blit(text, self.rect)  # 화면에 표시

class Item(pygame.sprite.Sprite):#heal
    def __init__(self, img_heal, scale = 1):
        self.image = img_heal  # 적기 그림
        self.rect = self.image.get_rect()
        self.isrun = False
        self.scale = scale

    def update(self, df):
        if self.isrun == True:
            self.rect.top += int(100 * df)
            if self.rect.top > 500:
                self.isrun = False

    def draw(self):
        if self.scale == 1:
            screen.blit(self.image, self.rect)
        else:
            img1 = pygame.transform.rotozoom(self.image, 0, self.scale)
            rect2=pygame.Rect(self.rect.left, self.rect.top, img1.get_rect().width,img1.get_rect().height)
            screen.blit(img1, rect2)

class Player(pygame.sprite.Sprite):
    def __init__(self, key_left, key_right, img_player):
        super().__init__()

        self.player_shield = 0
        self.player_life = 100
        self.image = img_player
        self.rect = self.image.get_rect()

        self.rect.left = int(padWidth * 0.45)
        self.rect.top = int(padHeight * 0.9)

        self.key_left = key_left
        self.key_right = key_right
        self.bullet_demage = 1

    def changePlane(self, img_player):
        self.image = img_player

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

    def __init__(self, img_enemy, type, name, sound):
        self.targetPoint = [0, 0]
        self.isrun = False

        self.image = img_enemy  # 적기 그림
        self.rect = self.image.get_rect()

        self.rect.left = randrange(0, padWidth - 64)
        self.rect.top = -64

        self.rect.height =  int(self.rect.height * 0.5)#충돌 부분을 줄임

        self.add_bullet_cnt = 0

        self.type = type
        self.name = name

        self.sound = sound

        self.life = 5

        if type == 6:
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

game = Game()
game.initGame()
game.run()
