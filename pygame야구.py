import pygame, sys
from pygame.locals import *
from random import*
pygame.init()
size = [720, 480]
screen = pygame.display.set_mode(size)
title = "Number Baseball Game"
clock = pygame.time.Clock()
pygame.display.set_caption(title)
bgcolor = (100, 100, 255)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.SysFont('LexiGulim.ttf', 40)
clicked = False
class button():
    button_col = (255, 255, 255)
    hover_col = (180, 180, 180)
    click_col = (105, 105, 105)
    text_col = black
    width = 60
    height = 60
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text

    def draw_button(self):
        global clicked
        action = False
        pos = pygame.mouse.get_pos()
        button_rect = Rect(self.x, self.y, self.width, self.height)
        if button_rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked = True
                pygame.draw.rect(screen, self.click_col, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_col, button_rect)
        else:
            pygame.draw.rect(screen, self.button_col, button_rect)
            pygame.draw.line(screen, black, (self.x, self.y), (self.x + self.width, self.y), 2)
            pygame.draw.line(screen, black, (self.x, self.y), (self.x, self.y + self.height), 2)
            pygame.draw.line(screen, black, (self.x, self.y + self.height), (self.x + self.width, self.y + self.height), 2)
            pygame.draw.line(screen, black, (self.x + self.width, self.y), (self.x + self.width, self.y + self.height), 2)
            text_img = font.render(self.text, True, self.text_col)
            text_len = text_img.get_width()
            screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))
        return action

def getAnswer():
    array = [1,2,3,4,5,6,7,8,9,0]
    shuffle(array)#섞기
    answer = array[0:4]#4개만 추출

    return answer

def input_answer():
    if btn1.draw_button():
        return 1
    if btn2.draw_button():
        return 2
    if btn3.draw_button():
        return 3
    if btn4.draw_button():
        return 4
    if btn5.draw_button():
        return 5
    if btn6.draw_button():
        return 6
    if btn7.draw_button():
        return 7
    if btn8.draw_button():
        return 8
    if btn9.draw_button():
        return 9
    if btn0.draw_button():
        return 0

    return -1

def judgment(player, computer):
    strike = 0
    ball = 0
    for p in range(len(player)):
        for c in range(len(computer)):
            if p == c and player[p] == computer[c]:
                strike += 1
            if p != c and player[p] == computer[c]:
                ball += 1
    return (strike, ball)

btn1 = button(60, 120, '1')
btn2 = button(140, 120, '2')
btn3 = button(220, 120, '3')
btn4 = button(60, 200, '4')
btn5 = button(140, 200, '5')
btn6 = button(220, 200, '6')
btn7 = button(60, 280, '7')
btn8 = button(140, 280, '8')
btn9 = button(220, 280, '9')
btn0 = button(140, 360, '0')
answer = [0, 0, 0, 0]
pNum = [0, 0, 0, 0]
computerNumber = getAnswer()

playerNumber = []

while True:
    screen.fill(bgcolor)

    number = input_answer()

    if number != -1:#마우스로 버튼을 누룰때만

        if len(playerNumber) == 4:#입력 4개가 되어있다면
            playerNumber.clear()#처음 부터 다시 입력 받게

        isSame = False
        for i in range(len(playerNumber)):
            if playerNumber[i] == number:
                isSame = True#중복 된 숫자가 있으면
                break
        if isSame == False:#중복된 숫자가 없을때만 플레이어 숫자 추가
            playerNumber.append(number)

    for i in range(len(playerNumber)):#입력된 갯수 만큼 화면에 출력
        pNum1 = font.render(str(playerNumber[i]), True, black)
        screen.blit(pNum1, (550 + i * 20, 100))


    ans1 = font.render(str(computerNumber[0]), True, black)
    screen.blit(ans1, (550, 200))
    ans2 = font.render(str(computerNumber[1]), True, black)
    screen.blit(ans2, (570, 200))
    ans3 = font.render(str(computerNumber[2]), True, black)
    screen.blit(ans3, (590, 200))
    ans4 = font.render(str(computerNumber[3]), True, black)
    screen.blit(ans4, (610, 200))

    if len(playerNumber) == 4:
        result = judgment(playerNumber, computerNumber)
        re = font.render(str(result[0])+"strike  "+str(result[1])+"ball", True, black)
        screen.blit(re, (300, 50))

        if result[0] == 4:#다 맞추면
            if pygame.mouse.get_pressed()[0] == 1:#마우스 누루면 종료
                break

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

pygame.quit()