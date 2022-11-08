import pygame
import os

############################################################################################################
pygame.init()  # 초기화 (나중에 따로 깊게 알아보자)

# 화면 크기 설정
screen_width = 640  # 화면 너비 설정
screen_height = 480  # 화면 높이 설정
screen = pygame.display.set_mode((screen_width, screen_height))  # 화면 설정의 구조

# 화면타이틀설정<=======게임을만들때무조건하는것
pygame.display.set_caption("Ratro Game")  # 게임 이름 설정

clock = pygame.time.Clock()
#############################################################################################################

current_path = os.path.dirname(__file__)  # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images")  # image 폴더의 위치 반환

# 배경 만들기
background = pygame.image.load(os.path.join(image_path, "background.png"))

# 스테이지 만들기
stage = pygame.image.load(os.path.join(image_path, "stage.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]  # 스테이지 위에 캐릭터를 올려놓기 위해서 높이를 설정
# 캐릭터 만들기
character = pygame.image.load(os.path.join(image_path, "character.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height - stage_height
# 캐릭터 이동 방향
character_to_x = 0
# 캐릭터 이동 속도
character_speed = 5
# 무기 만들기
weapon = pygame.image.load(os.path.join(image_path, "weapon.png"))
weapon_size = weapon.get_rect().size
weapon_width = weapon_size[0]
# 무기는 여러발 발사 가능 (즉 한번에 여러개의 weapon이 존재할수 있음)
weapons = []
# 무기 이동속도
weapon_speed = 10
# 공 만들기
ball_images = [
    pygame.image.load(os.path.join(image_path, "balloon1.png")),
    pygame.image.load(os.path.join(image_path, "balloon2.png")),
    pygame.image.load(os.path.join(image_path, "balloon3.png")),
    pygame.image.load(os.path.join(image_path, "balloon4.png"))]
# 공 크기에 따른 최초 스피드
ball_speed_y = [-18, -15, -12, -9]  # 공의 각 크기에 따른 y축의 속도 정의

balls = []

# 최초로 발생하는 큰 공 추가
balls.append({
    "pos_x": 50,
    "pos_y": 50,
    "img_idx": 0,
    "to_x": 3,  # 공이 x축으로 3만큼 이동한다
    "to_y": -6,  # 공이 y축으로 -6만큼 (위로) 이동한다
    "init_spd_y": ball_speed_y[0]})  # 공의 y축 스피드 즉 위로 올라가는 스피드

# 사라질 변수 ,공 정보 저장 변수
weapon_to_remove = -1
ball_to_remove = -1

running = True  # 게임이 진행중인가?를 확인하는 변수
while running:  # pygame에서 game이 진행 되기위해 반드시 필요한 구
    dt = clock.tick(30)

    for event in pygame.event.get():  # 어떤 이벤트(사건)이 발생하였는가?
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트가 발생하였는가?
            running = False  # 창이 닫히는 이벤트가 발생하였다면 게임 진행을 중단해라
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                character_to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                character_to_x += character_speed
            elif event.key == pygame.K_SPACE:  # 스페이스바를 누르면 무기 발사
                weapon_x_pos = (character_width - weapon_width) / 2 + character_x_pos
                weapon_y_pos = character_y_pos
                weapons.append([weapon_x_pos, weapon_y_pos])
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                character_to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += character_to_x
    # 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 무기 위치 조정
    weapons = [[w[0], w[1] - weapon_speed] for w in
               weapons]  # w 에 weapons의 값을 하나씩 넣어서 리스트를 만들고 w의 리스트의  1번째 값(y좌표)에 weapon_speed의 값을 뺸뒤 뺀 값을 다시 weapons 에 리스트 형태로 저장한다
    weapons = [[w[0], w[1]] for w in weapons if w[
        1] > 0]  # weapon의 y좌표가 0보다 클때(즉 아직 화면을 벗어나지 않았을때) weapons 에 값을 넣어라 만약 y좌표가 0보다 작다면(화면을 벗어났을떄) 값을 넣지 않는다

    # 공 위치 정의
    for ball_idx, ball_val in enumerate(balls):  # enumerate => ballon_idx 에는 index 번호를 ballon_val 에는 index에 해당하는 값을 넣는다
        ball_pos_x = ball_val["pos_x"]  # ball_x_pos 란 변수에 ballon_val란 딕셔너리에 pos_x에 해당하는 값을 넣는다
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]  # balls 에 있는 image_idx에 할당된 값 (0)을 불러온다

        ball_size = ball_images[
            ball_img_idx].get_rect().size  # ballon_images에 할당된 값들중 ball_image_inx(0)번째 에 있는 값(가장큰 공의 이미지)의 사이즈를 불러온다
        ball_width = ball_size[0]
        ball_height = ball_size[1]
        # 세로 벽에 닿을 경우 튕기는 효과
        if ball_pos_x < 0 or ball_pos_x > screen_width - ball_width:
            ball_val["to_x"] = ball_val["to_x"] * -1  # x축이동 방향을 반대로 바꾼다
        # 가로 벽에 닿을 경우 튕기는 효과
        if ball_pos_y >= screen_height - stage_height - ball_height:
            ball_val["to_y"] = ball_val["init_spd_y"]
        else:
            ball_val["to_y"] += 0.5  # 스테이지에 닿는 경우가 아니라면 공은 점점 내려간다
    ball_val["pos_x"] += ball_val["to_x"]
    ball_val["pos_y"] += ball_val["to_y"]

    # 충돌처리
    # 캐릭터 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    for ball_idx, ball_val in enumerate(balls):
        ball_pos_x = ball_val["pos_x"]
        ball_pos_y = ball_val["pos_y"]
        ball_img_idx = ball_val["img_idx"]

        # 공 rect 정보 업데이트
        ball_rect = ball_images[ball_img_idx].get_rect()
        ball_rect.left = ball_pos_x
        ball_rect.top = ball_pos_y

        # 공과 캐릭터 충돌 체크
        if character_rect.colliderect(ball_rect):
            running = False
            break
        # 공과 무기 충돌 처리
    for weapon_idx, weapon_val in enumerate(weapons):
        weapon_pos_x = weapon_val[0]
        weapon_pos_y = weapon_val[1]
        weapon_rect = weapon.get_rect()
        weapon_rect.left = weapon_pos_x
        weapon_rect.top = weapon_pos_y
        # 무기와 공 충돌 체크
        if weapon_rect.colliderect(ball_rect):
            weapon_to_remove = weapon_idx  # 공과 닿은 무기를 없애기 위해 그 무기의 idx 값을 저장
            ball_to_remove = ball_idx  # 무기와 닿은 공을 없애기 위해 그 공의 idx 값을 저장
            break

    # 충돌된 공 지우기 or 충돌된 무기 지우기
    if ball_to_remove > -1:  # 만약 무기와 닿은 공이 있다면 ball_to_idx에 양수 값이 저장될 것이고 그 값은 항상 -1 보다 크기 때문에 ball_to_remove가 -1 보다 크면공이 닿았다는 뜻
        del balls[ball_to_remove]  # balls에서 idx ball_to_remve 에 해당하는 값을 지운다
        ball_to_remove = -1  # ball_to_remove 는 계속 사용해야 하므로 값을 리셋 해준다
    if weapon_to_remove > -1:
        del weapons[weapon_to_remove]
        weapon_to_remove = -1

    screen.blit(background, (0, 0))  # 배경 그리기 (blit = Block image transfer)
    for weapon_x_pos, weapon_y_pos in weapons:
        screen.blit(weapon, (weapon_x_pos, weapon_y_pos))
    for idx, val in enumerate(balls):
        ball_pos_x = val["pos_x"]
        ball_pos_y = val["pos_y"]
        ball_img_idx = val["img_idx"]
        screen.blit(ball_images[ball_img_idx], (ball_pos_x, ball_pos_y))
    screen.blit(stage, (0, screen_height - stage_height))
    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()

# pygame 종료