from tkinter import *

class Sprite:
    def __init__(self, image, x, y):
        self.img = image
        self.x = x
        self.y = y
        self.dx = 0
        self.dy = 0

    def getWidth(self):
        return self.img.width()

    def getHeight(self):
        return self.img.height()

    def draw(self, g):
        g.create_image(self.x, self.y, anchor=NW, image=self.img)

    def move(self):
        self.x += self.dx
        self.y += self.dy

    def setDx(self, dx):
        self.dx = dx

    def setDy(self, dy):
        self.dy = dy

    def getDx(self):
        return self.dx

    def getDy(self):
        return self.dy

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def checkCollision(self, other):
        p1x = self.x
        p1y = self.y
        p2x = self.x + self.getWidth()
        p2y = self.y + self.getHeight()
        p3x = other.x
        p3y = other.y
        p4x = other.x + other.getWidth()
        p4y = other.y + other.getHeight()

        overlapped = not (p4x < p2x or p3x > p2x or p2y < p3y or p1y > p4y)
        return overlapped

    def handCollision(self, other):
        pass


class GoalpostSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = 0
        self.dy = 0

    def move(self):
        if ((self.dx > 0) and (self.x < 10)):
            return
        if ((self.dx > 0) and (self.x > 800)):
            return
        super().move()
        self.dx = 0

    def handleCollision(self, other):
        if type(other) is BallSprite:
            self.game.endGame()

class ShotSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game

    def move(self):
        self.y -= 50
        if (self.y < 0):
            del self
            return
        super().move()
    def handleCollision(self, other):
        if type(other) is BallSprite:
            self.game.removeSprite(self)
            self.game.removeSprite(other)


class BallSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dx = -10

    def move(self):
        if (((self.dx < 0) and (self.x < 10)) or ((self.dx > 0) and (self.x > 750))):
            self.dx = -self.dx
            self.y += 50
            if (self.y > 600):
                self.game.endGame()
        super().move()
    def handleCollision(self, other):
        if type(other) is BallSprite:
            self.game.removeSprite(self)
            self.game.removeSprite(other)


class PlayerSprite(Sprite):
    def __init__(self, game, image, x, y):
        super().__init__(image, x, y)
        self.game = game
        self.dy = -20

    def move(self):
        super().move()
        if (self.y < -100):
            self.game.removeSprite(self)

    def handleCollision(self, other):
        if type(other) is BallSprite:
            self.game.removeSprite(self)
            self.game.removeSprite(other)

class GroundGame():
    def keyLeft(self, event):
        self.Goalpost.setDx(-15)
        return

    def keyRight(self, event):
        self.Goalpost.setDx(+15)
        return

    def keySpace(self, event):
        self.fire()
        return

    def initSprites(self):
        self.Goalpost = GoalpostSprite(self, self.GoalpostImage, 370, 550)
        self.sprites.append(self.Goalpost)
        for y in range(0, 2):
            for x in range(0, 12):
                ball = BallSprite(self, self.BallImage, 100 + (x * 50), (50) + y * 30)
                self.sprites.append(ball)

    def __init__(self, master):
        self.master = master
        self.sprites = []
        self.canvas = Canvas(master, width=1000, height=700)
        self.canvas.pack()
        self.PlayerImage = PhotoImage(file="bang.png")#"D:\Player.png")
        self.GoalpostImage = PhotoImage(file="bang.png")#"D:\Goalpost.png")
        self.BallImage = PhotoImage(file="bang.png")#"D:\Ball.png")
        self.running = True
        self.initSprites()
        master.bind("<Left>", self.keyLeft)
        master.bind("<Right>", self.keyRight)
        master.bind("<space>", self.keySpace)

    def startGame(self):
        self.sprites.clear()
        self.initSprites()

    def endGame(self):
        self.running = False
        pass

    def removeSprite(self, sprite):
        if (sprite in self.sprites):
            self.sprites.remove(sprite)
            del sprite

    def fire(self):
        shot = ShotSprite(self, self.PlayerImage, self.Goalpost.getX() + 10, self.Goalpost.getY() - 30)
        self.sprites.append(shot)

    def paint(self, g):
        self.canvas.delete(ALL)
        self.canvas.create_rectangle(0, 0, 1000, 700, fill="green")
        for sprite in self.sprites:
            sprite.draw(self.canvas)

    def gameLoop(self):
        for sprite in self.sprites:
            sprite.move()
        for me in self.sprites:
            for other in self.sprites:
                if me != other:
                    if (me.checkCollision(other)):
                        me.handleCollision(other)
                        other.handleCollision(me)
        self.paint(self.canvas)
        if (self.running):
            self.master.after(10, self.gameLoop)

root = Tk()
g = GroundGame(root)
root.after(10, g.gameLoop())
root.mainloop()