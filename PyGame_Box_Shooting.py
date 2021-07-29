import pygame
from random import randint

s, f = pygame.init()
print(f'{s}--{f}')

SIZE = WIDTH, HEIGHT = 400, 600
COLOR = WHITE, BLACK, GRAY, RED = (255, 255, 255), (0, 0, 0), (125, 125, 125), (255, 0, 0)

pygame.display.set_caption('Box Shooting!!')
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
FPS = 30


class Pen:
    def __init__(self, font, size):
        self.obj = pygame.font.SysFont(font, size)
        self.rect = pygame.Rect(0, 0, 0, 0)

    def write(self, text='default', color=BLACK, pos=(100, 100)):
        content = self.obj.render(text, True, color)
        self.rect = content.get_rect()
        self.rect.center = pos
        screen.blit(content, self.rect)


class Effect:
    def __init__(self, pos, sort):
        self.pos = self.x, self.y = pos
        self.sort = sort
        self.r = 0

    def update(self):
        self.r += 1
        r = randint(50, 200)
        g = randint(50, 200)
        b = randint(50, 200)
        if self.sort == 1:
            pygame.draw.circle(screen, (r, g, b), self.pos, self.r, 1)
        if self.sort == 2:
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0] + self.r, self.pos[1] + self.r), 1)
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0] + self.r, self.pos[1] - self.r), 1)
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0] - self.r, self.pos[1] + self.r), 1)
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0] - self.r, self.pos[1] - self.r), 1)

            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0], self.pos[1] + self.r), 1)
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0], self.pos[1] - self.r), 1)
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0] + self.r, self.pos[1]), 1)
            pygame.draw.line(screen, (r, g, b), self.pos, (self.pos[0] - self.r, self.pos[1]), 1)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos=(WIDTH // 2, 0), color=(255, 0, 0), speed=200):
        super().__init__()
        self.image = pygame.Surface((5, 15)).convert()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image.fill(color)
        self.speed = speed


class EBullet(Bullet):
    def update(self, dt):
        self.rect.y += int(dt * self.speed)
        screen.blit(self.image, self.rect)
        self.speed *= 1.02


class MBullet(Bullet):
    def update(self, dt):
        self.rect.y -= int(dt * self.speed)
        screen.blit(self.image, self.rect)
        self.speed *= 1.02


class Plane(pygame.sprite.Sprite):
    def __init__(self, size=(30, 45), color=[255, 0, 0], pos=(WIDTH // 2, HEIGHT - 10), speed=200):
        super().__init__()
        self.image = pygame.Surface(size).convert()
        self.rect = self.image.get_rect()
        self.rect.midbottom = pos
        self.color = color
        self.speed = speed
        self.epen = Pen('Arial', 15)
        self.life = 3


class MainPlane(Plane):
    def update(self, dt):
        self.image.fill(self.color)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if self.rect.left > 0:
                self.rect.x -= int(dt * self.speed)
        if keys[pygame.K_RIGHT]:
            if self.rect.right < WIDTH:
                self.rect.x += int(dt * self.speed)
        if keys[pygame.K_UP]:
            if self.rect.top > HEIGHT // 2:
                self.rect.y -= int(dt * self.speed)
        if keys[pygame.K_DOWN]:
            if self.rect.bottom < HEIGHT:
                self.rect.y += int(dt * self.speed)
        screen.blit(self.image, self.rect)
        self.epen.write(str(self.life), BLACK, self.rect.center)


class EnemyPlane(Plane):
    def update(self, dt, posx):
        self.image.fill(self.color)
        self.rect.y += int(dt * self.speed)
        if self.rect.x < posx:
            self.rect.x += 1
        else:
            self.rect.x -= 1

        screen.blit(self.image, self.rect)


class MainWin:
    def __init__(self):

        self.main = MainPlane((30, 45), [255, 0, 0])
        self.bullet = pygame.sprite.Group()
        self.enemy = pygame.sprite.Group()
        self.ebullet = pygame.sprite.Group()
        self.effect = []

        self.timer = 0
        self.btimer = 0
        self.score = 0
        self.scoretime = 0
        self.espeed = 100
        self.etime = 3

        self.scorePen = Pen('Arial', 15)

    def start(self):
        running = True
        while running:
            screen.fill(WHITE)
            dt = clock.tick(FPS) / 1000

            self.scorePen.write(f'Score : {self.score}', BLACK, (WIDTH - 100, 20))

            self.timer += dt
            if self.timer > self.etime:
                self.timer = 0
                if self.etime > 0.3:
                    self.etime -= 0.1
                else:
                    self.espeed += 5

                self.enemy.add(EnemyPlane((15, 30), (0, 255, 0), (randint(30, WIDTH - 30), 15), self.espeed))

            self.btimer += dt
            if self.btimer > 0.5:
                self.btimer = 0
                if len(self.enemy) > 0:
                    self.ebullet.add(
                        EBullet(self.enemy.sprites()[randint(0, len(self.enemy) - 1)].rect.midbottom, (255, 0, 0)))

            self.score += 1
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                    if e.key == pygame.K_SPACE:
                        self.bullet.add(MBullet(self.main.rect.midtop, (0, 0, 255)))

            for b in self.bullet:
                b.update(dt)
                if b.rect.top < 0:
                    self.bullet.remove(b)

            for b in self.ebullet:
                b.update(dt)
                if b.rect.bottom > HEIGHT:
                    self.ebullet.remove(b)

            for e in self.enemy:
                e.update(dt, self.main.rect.x)
                if e.rect.top > HEIGHT:
                    self.enemy.remove(e)
                    self.main.life -= 1
                    self.effect.append(Effect(e.rect.center, 1))

            for unit in pygame.sprite.groupcollide(self.bullet, self.ebullet, True, True):
                self.effect.append(Effect(unit.rect.center, 2))
                self.score += 100

            for unit in pygame.sprite.groupcollide(self.bullet, self.enemy, True, True):
                self.score += 1000
                self.effect.append(Effect(unit.rect.center, 1))

            if pygame.sprite.spritecollide(self.main, self.ebullet, True):
                self.main.life -= 1
                self.main.color[1] += 80
                self.main.color[2] += 80
                self.effect.append(Effect(self.main.rect.center, 1))

            if pygame.sprite.spritecollide(self.main, self.enemy, True):
                self.main.color[1] += 80
                self.main.color[2] += 80
                self.main.life -= 1
                self.effect.append(Effect(self.main.rect.center, 1))

            if self.main.life < 1:
                return self.score

            for e in self.effect:
                e.update()
                if e.sort == 1:
                    if e.r > 16:
                        self.effect.remove(e)
                elif e.sort == 2:
                    if e.r > 8:
                        self.effect.remove(e)
            self.main.update(dt)
            pygame.display.flip()
        return -1


class Scene:
    def __init__(self):
        self.mainPen = Pen('Arial Black', 30)
        self.startPen = Pen('Arial', 20)
        self.timer = 0
        self.textcolor = 1


class Intro(Scene):
    def start(self):
        running = True
        onOver = False
        while running:
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, (15, 15, WIDTH - 30, HEIGHT - 30), 4)
            pygame.draw.rect(screen, GRAY, (22, 22, WIDTH - 44, HEIGHT - 44), 2)
            dt = clock.tick(5)
            self.timer += dt
            if self.timer > 1000:
                self.timer = 0
                self.textcolor += 1
                if self.textcolor >= 3:
                    self.textcolor = 1

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                    if e.key == pygame.K_SPACE:
                        return 1
                if e.type == pygame.MOUSEMOTION:
                    if (self.startPen.rect.collidepoint(e.pos)):
                        onOver = True
                    else:
                        onOver = False
                if e.type == pygame.MOUSEBUTTONUP:
                    if onOver:
                        return 1
            self.mainPen.write('Box Shooting!!', BLACK, (WIDTH // 2, HEIGHT // 3))
            self.startPen.write('Press SpaceBar to Start!!', COLOR[self.textcolor], (WIDTH // 2, HEIGHT // 3 * 2))
            if onOver:
                pygame.draw.line(screen, RED, self.startPen.rect.bottomleft, self.startPen.rect.bottomright, 1)

            pygame.display.flip()
        return 0


class Outtro(Scene):
    def start(self, score):
        running = True
        onOver = False
        while running:
            screen.fill(WHITE)
            pygame.draw.rect(screen, BLACK, (15, 15, WIDTH - 30, HEIGHT - 30), 4)
            pygame.draw.rect(screen, GRAY, (22, 22, WIDTH - 44, HEIGHT - 44), 2)
            dt = clock.tick(5)
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                    if e.key == pygame.K_s or e.key == pygame.K_r:
                        running = False
                if e.type == pygame.MOUSEMOTION:
                    if (self.startPen.rect.collidepoint(e.pos)):
                        onOver = True
                    else:
                        onOver = False
                if e.type == pygame.MOUSEBUTTONUP:
                    if onOver:
                        return 1
            self.mainPen.write('Game Over', BLACK, (WIDTH // 2, HEIGHT // 3))
            self.startPen.write(f'Your score is {score}...', COLOR[1], (WIDTH // 2, HEIGHT // 3 * 2))
            self.startPen.write('Press r to Restart...', COLOR[1], (WIDTH // 2, HEIGHT // 3 * 2 + 25))
            if onOver:
                pygame.draw.line(screen, RED, self.startPen.rect.bottomleft, self.startPen.rect.bottomright, 1)
            pygame.display.flip()
        return 0


intro = Intro()
outtro = Outtro()

while True:
    go = intro.start()
    game = MainWin()

    if go == 1:
        score = game.start()
        if score > 10:
            outtro.start(score)
    elif go == 0:
        break

pygame.quit()
