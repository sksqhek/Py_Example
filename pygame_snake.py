import pygame
import sys
import time
import random

from pygame.locals import *

window_width = 800
window_height = 600

grid_size = 20
grid_width = window_width / grid_size
grid_height = window_height / grid_size

WHITE = (255,255,255)
GREEN = (0,50,0)
ORANGE = (255,95,35)
GRAY = (100,100,100)

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

FPS = 10

class Python(object):
    def __init__(self):
        self.create()
        self.color = GREEN

    def create(self):
        self.length = 2
        self.positions = [((window_width / 2),(window_height / 2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def control(self,xy):
        if(xy[0] * -1, xy[1] * -1) == self.direction:
            return
        else:
            self.direction = xy

    def move(self):
        cur = self.positions[0]
        x,y = self.direction
        new = (((cur[0] + (x * grid_size)) % window_width), (cur[1] + (y * grid_size)) % window_height)
        if new in self.positions[2:]:
            self.create()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def eat(self):
         self.length += 1

    def draw(self, surface):
        for p in self.positions:
            draw_object(surface, self.color, p)

class Feed(object):
    def __init__(self):
        self.position = (0,0)
        self.color = ORANGE
        self.create()

    def create(self):
        self.position = (random.randint(0,grid_width - 1) * grid_size, random.randint(0,grid_height - 1) * grid_size)

    def draw(self, surface):
        draw_object(surface,self.color, self.position)


def draw_object(surface, color, pos):
        r = pygame.Rect((pos[0],pos[1]), (grid_size,grid_size))
        pygame.draw.rect(surface, color, r)

def check_eat(python, feed):
    if python.positions[0] == feed.position:
        python.eat()
        feed.create()

def show_info(length, speed, surface):
    font = pygame.font.Font(None, 34)
    text = font.render("Length: " + str(length) + "       Speed: " + str(round(speed, 2)), 1, GRAY)
    pos = text.get_rect()
    pos.centerx = 150
    surface.blit(text, pos)

if __name__ == '__main__':
    python = Python()
    feed = Feed()
    pygame.init()

    window = pygame.display.set_mode((window_width,window_height),0,32)
    pygame.display.set_caption('python game')
    surface = pygame.Surface(window.get_size())
    surface = surface.convert()
    surface.fill(WHITE)
    clock = pygame.time.Clock()
    pygame.key.set_repeat(1,40)
    window.blit(surface,(0,0))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    python.control(UP)
                elif event.key == K_DOWN:
                    python.control(DOWN)
                elif event.key == K_LEFT:
                    python.control(LEFT)
                elif event.key == K_RIGHT:
                    python.control(RIGHT)

        surface.fill(WHITE)
        python.move()
        check_eat(python, feed)
        speed = (FPS + python.length) / 2
        show_info(python.length, speed, surface)
        python.draw(surface)
        feed.draw(surface)
        window.blit(surface, (0,0))
        pygame.display.flip()
        pygame.display.update()
        clock.tick(speed)
