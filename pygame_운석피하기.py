import pygame
import sys
import time

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

pygame.init()
pygame.display.set_caption('SpaceShuttle')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

imgShuttle = pygame.image.load('bang.png')#('ss.png')

clock = pygame.time.Clock()

img_width = imgShuttle.get_width()
img_height = imgShuttle.get_height()

loc_a = [[0, 200],
         [200, 10],
         [120, 20],
         [639, 74],
         [385, 479]]
vel = [[4, 4],
       [-4, -4],
       [4, 8],
       [-4, 4],
       [8, -4]]

size_rock = 10

myFont = pygame.font.SysFont("arial", 20, True, False)

loc_ship = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]
size_ship = 20
startTime = time.time()

while True:
    clock.tick(30)
    screen.fill((0, 0, 0))

    nowTime = round((time.time() - startTime), 2)
    time_diff = str(nowTime)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        loc_ship[0] -= 3

    if keys[pygame.K_RIGHT]:
        loc_ship[0] += 3

    if keys[pygame.K_UP]:
        loc_ship[1] -= 3

    if keys[pygame.K_DOWN]:
        loc_ship[1] += 3

    if keys[pygame.K_q]:
        pygame.quit()
        sys.exit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit

    for i in range(5):
        loc_a[i][0] = loc_a[i][0] + vel[i][0]
        loc_a[i][1] = loc_a[i][1] + vel[i][1]

        if loc_a[i][0] >= SCREEN_WIDTH:
            vel[i][0] = -vel[i][0]

        if loc_a[i][0] <= 0:
            vel[i][0] = -vel[i][0]

        if loc_a[i][1] >= SCREEN_HEIGHT:
            vel[i][1] = -vel[i][1]

        if loc_a[i][1] <= 0:
            vel[i][1] = -vel[i][1]

        dist_x = loc_a[i][0] - loc_ship[0]
        dist_y = loc_a[i][1] - loc_ship[1]
        dist = (dist_x ** 2 + dist_y ** 2) ** (0.5)

        if dist < (size_rock + size_ship):
            print("생존 시간" + time_diff + " 초")
            pygame.quit()
            sys.exit()

    for i in range(5):
        pygame.draw.circle(screen, (255, 255, 255), loc_a[i], size_rock, 10)

    currentTime_text = myFont.render(time_diff, 1, (255, 255, 255))

    pygame.draw.circle(screen, (255, 255, 255), loc_ship, size_ship, 1)
    loc_TL = [loc_ship[0] - img_width / 2, loc_ship[1] - img_height / 2]
    screen.blit(imgShuttle, loc_TL)

    screen.blit(currentTime_text, [SCREEN_WIDTH - 70, 20])

    pygame.display.update()