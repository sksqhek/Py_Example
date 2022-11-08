import timeit

import numpy as np
import cv2

width, height = 512, 512
x, y, xy, R = 256, 256, 256, 50
direction = 0  # right

prev = timeit.default_timer()
t_right = 0
t_left = 0
t_up = 0
t_down = 0

while True:
    key = cv2.waitKeyEx(30)


    if key == 0x1B:
        break
    # 방향키 방향전환
    elif key == 0x270000:  # right
        direction = 0
        t_right = timeit.default_timer()#키입력한 시간 저장

    elif key == 0x280000:  # down
        direction = 1
        t_down = timeit.default_timer()

    elif key == 0x250000:  # left
        direction = 2
        t_left = timeit.default_timer()

    elif key == 0x260000:  # up
        direction = 3
        t_up = timeit.default_timer()

    #대각선 조합 키를 누를때 동시에 눌렀는지 시간 차이 계산 0.1초 보다 작은 간격으로 누루면 작동
    if abs(t_up - t_left) < 0.1 and abs(t_up - t_left) > 0.0:
        direction = 4
    if abs(t_up - t_right) < 0.1 and abs(t_up - t_right) > 0.0:
        direction = 5
    if abs(t_down - t_left) < 0.1 and abs(t_down - t_left) > 0.0:
        direction = 6
    if abs(t_down - t_right) < 0.1 and abs(t_down - t_right) > 0.0:
        direction = 7

    print(direction)

    # 방향으로 이동
    if direction == 0:  # right
        x += 10

    elif direction == 1:  # down
        y += 10

    elif direction == 2:  # left
        x -= 10

    elif direction == 3:  # up
        y -= 10

    elif direction == 4:  # up left
        y -= 10
        x -= 10

    elif direction == 5:  # up right
        y -= 10
        x += 10

    elif direction == 6:  # down left
        y += 10
        x -= 10

    elif direction == 7:  # down right
        y += 10
        x += 10



    img = np.zeros((width, height, 3), np.uint8) + 255

    ##좌우
    if direction != 2 and x >= width + R * 2:
        x -= width

    elif direction != 0 and x <= -R:
        x += width

    if x + R > width and direction != 2:
        cv2.circle(img, (x - width, y), R, (0, 0, 255), -1)

    elif direction != 0 and x - R < 0:
        cv2.circle(img, (x + width, y), R, (0, 0, 255), -1)

    ##상하
    if direction != 3 and y >= width + R * 2:
        y -= width

    elif direction != 1 and y <= -R:
        y += width

    if x + R > width and direction != 3:
        cv2.circle(img, (x, y - width), R, (0, 0, 255), -1)

    elif direction != 1 and x - R < 0:
        cv2.circle(img, (x, y + width), R, (0, 0, 255), -1)

    cv2.circle(img, (x, y), R, (0, 0, 255), -1)
    cv2.imshow('img', img)

cv2.destroyAllWindows()