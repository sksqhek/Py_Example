import pygame, sys
from pygame.locals import *
from random import *

pygame.init()
size = [720, 480]  # 게임창 크기 (가로x세로)
screen = pygame.display.set_mode(size)
title = "Number Baseball Game"
pygame.display.set_caption(title)
background = pygame.image.load("baseball.jpg")
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
num_color = (50, 180, 50)  # 오른쪽에 출력되는 숫자색
bt_edge_color = (0, 0, 0)  # 버튼 테두리색
strike_color = (225, 225, 25)
ball_color = (0, 255, 0)
out_color = (255, 0, 0)  # 패배시 출력되는 OUT 문자열색
correct_color = (139, 0, 255)  # 승리시 출력되는 CONGRATUATION 문자열색
font = pygame.font.SysFont("LexiGulim.ttf", 40)
clicked = False


class button():
    button_color = (50, 205, 50)  # 버튼색
    hover_color = (46, 139, 87)  # 버튼에 마우스를 올렸을 때 변하는 색
    click_color = (105, 105, 105)  # 버튼을 눌렀을 때 변하는 색
    text_color = WHITE  # 버튼의 숫자색
    width = 50  # 버튼의 가로길이
    height = 50  # 버튼의 세로길이

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
                pygame.draw.rect(screen, self.click_color, button_rect)
            elif pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                clicked = False
                action = True
            else:
                pygame.draw.rect(screen, self.hover_color, button_rect)
                text_img = font.render(self.text, True, self.text_color)
                text_len = text_img.get_width()
                screen.blit(text_img, (self.x + int(self.width / 2) - int(text_len / 2), self.y + 20))
        else:
            pygame.draw.rect(screen, self.button_color, button_rect)

        pygame.draw.line(screen, bt_edge_color, (self.x, self.y), (self.x + self.width, self.y), 2)
        pygame.draw.line(screen, bt_edge_color, (self.x, self.y), (self.x, self.y + self.height), 2)
        pygame.draw.line(screen, bt_edge_color, (self.x, self.y + self.height),
                         (self.x + self.width, self.y + self.height), 2)
        pygame.draw.line(screen, bt_edge_color, (self.x + self.width, self.y),
                         (self.x + self.width, self.y + self.height), 2)
        text_img = font.render(self.text, True, self.text_color)
        text_len = text_img.get_width()
        screen.blit(text_img, ((self.x + int(self.width / 2) - int(text_len / 2), self.y + 20)))
        return action


def getAnswer():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    answer = sample(array, 4)
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


def print_hint(player, computer, count):
    strike = 0
    ball = 0
    for p in range(len(player)):
        for c in range(len(computer)):
            if p == c and player[p] == computer[c]:
                strike += 1
            if p != c and player[p] == computer[c]:
                ball += 1
    count = count - 1
    return (strike, ball, count)


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
count = 1#5
computerNumber = getAnswer()
playerNumber = []
while True:
    screen.blit(background, (0, 0))

    number = input_answer()
    if number != -1:
        if len(playerNumber) == 4:
            playerNumber.clear()
        check = False
        for i in range(len(playerNumber)):
            if playerNumber[i] == number:
                check = True
                break
        if check == False:
            playerNumber.append(number)
            if len(playerNumber) == 4:
                count -= 1


    for i in range(len(playerNumber)):
        pNum1 = font.render(str(playerNumber[i]), True, num_color)
        screen.blit(pNum1, (340 + i * 20, 250))
        # 오른쪽에 뜨는 입력한 숫자 출력 좌표: 550이랑 100만 바꾸면 됩니다 (x, y)

    ans1 = font.render(str(computerNumber[0]), True, BLACK)
    screen.blit(ans1, (550, 200))
    ans2 = font.render(str(computerNumber[1]), True, BLACK)
    screen.blit(ans2, (570, 200))
    ans3 = font.render(str(computerNumber[2]), True, BLACK)
    screen.blit(ans3, (590, 200))
    ans4 = font.render(str(computerNumber[3]), True, BLACK)
    screen.blit(ans4, (610, 200))

    cnt = font.render("cnt: " + str(count), True, BLACK)
    screen.blit(cnt, (550, 50))

    if len(playerNumber) == 4:
        result = print_hint(playerNumber, computerNumber, count)
        if (count == 0):
            fail = font.render("Failure", True, out_color)
            screen.blit(fail, (300, 50))
            if pygame.mouse.get_pressed()[0] == 1:
                pygame.quit()
                sys.exit()

        elif (result[0] == 0 and result[1] == 0):
            out = font.render("OUT", True, out_color)
            screen.blit(out, (315, 50))
            cnt = font.render("cnt: " + str(count), True, BLACK)
            screen.blit(cnt, (550, 50))
        elif result[0] == 4:
            victory = font.render("Congratulaions!", True, correct_color)
            screen.blit(victory, (230, 50))
        else:
            st_re = font.render(str(result[0]) + "strike  ", True, strike_color)
            bl_re = font.render(str(result[1]) + "ball", True, ball_color)
            screen.blit(st_re, (300, 50))
            screen.blit(bl_re, (400, 50))
            #cnt = font.render("cnt: " + str(count), True, BLACK)
            #screen.blit(cnt, (550, 50))
        if result[0] == 4 or result[2] == 0:
            if pygame.mouse.get_pressed()[0] == 1:
                break
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
pygame.quit()