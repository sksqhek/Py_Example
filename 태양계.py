import turtle
import math


class SolarSystem:
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.kattlite = []
        self.ssturtle = turtle.Turtle()
        self.ssturtle.hideturtle()
        self.ssscreen = turtle.Screen()
        self.ssscreen.setworldcoordinates(-width / 2.0, -height / 2.0, width / 2.0, height / 2.0)
        self.ssscreen.tracer(50)

    def addPlanet(self, aplanet):
        self.planets.append(aplanet)

    def addSun(self, asun):
        self.thesun = asun

    def addKattlite(self, akattlite):
        self.kattlite.append(akattlite)

    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet)

    def showKattlite(self):
        for akattlite in self.sttilte:
            print(akattlite)

    def freeze(self):
        self.ssscreen.exitonclick()

    def movePlanets(self):
        G = .1
        dt = .0001

        for p in self.planets:
            p.moveTo(p.getXPos() + dt * p.getXVel(), p.getYPos() + dt * p.getYVel())

            rx = self.thesun.getXPos() - p.getXPos()
            ry = self.thesun.getYPos() - p.getYPos()
            r = math.sqrt(rx ** 2 + ry ** 2)

            accx = G * self.thesun.getMass() * rx / r ** 3
            accy = G * self.thesun.getMass() * ry / r ** 3

            p.setXVel(p.getXVel() + dt * accx)

            p.setYVel(p.getYVel() + dt * accy)

    def moveKattlite(self):
        G = 1000
        dt = .0001

        for k in self.kattlite:
            k.moveTo(k.getXPos() + dt * k.getXVel(), k.getYPos() + dt * k.getYVel())

            krx = self.p.getXPos() - k.getXPos()
            kry = self.p.getYPos() - k.getYPos()
            kr = math.sqrt(krx ** 2 + kry ** 2)

            kaccx = G * self.p.getMass() * krx / kr ** 3
            kaccy = G * self.p.getMass() * kry / kr ** 3

            k.setXVel(k.getXVel() + dt * kaccx)

            k.setYVel(k.getYVel() + dt * kaccy)


class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0

        self.sturtle = turtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")

    def getName(self):
        return self.name

    def getRadius(self):
        return self.radius

    def getMass(self):
        return self.mass

    def getTemperature(self):
        return self.temp

    def getVolume(self):
        v = 4.0 / 3 * math.pi * self.radius ** 3
        return v

    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius ** 2
        return sa

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def __str__(self):
        return self.name

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y


class Planet:

    def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic

        self.pturtle = turtle.Turtle()
        self.pturtle.up()
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.goto(self.x, self.y)
        self.pturtle.down()

    def getName(self):
        return self.name

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def show(self):
        print(self.name)

    def __str__(self):
        return self.name

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.pturtle.goto(newx, newy)

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy


class Kattlite:

    def __init__(self, iname, irad, im, idist, ivx, ivy, ic):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.velx = ivx
        self.vely = ivy
        self.color = ic

        self.kturtle = turtle.Turtle()
        self.kturtle.up()
        self.kturtle.color(self.color)
        self.kturtle.shape("circle")
        self.kturtle.goto(self.x, self.y)
        self.kturtle.down()

    def getName(self):
        return self.name

    def getMass(self):
        return self.mass

    def getDistance(self):
        return self.distance

    def getDensity(self):
        d = self.mass / self.getVolume()
        return d

    def setName(self, newname):
        self.name = newname

    def show(self):
        print(self.name)

    def moveTo(self, newx, newy):
        self.x = newx
        self.y = newy
        self.kturtle.goto(newx, newy)

    def getXPos(self):
        return self.x

    def getYPos(self):
        return self.y

    def getXVel(self):
        return self.velx

    def getYVel(self):
        return self.vely

    def setXVel(self, newvx):
        self.velx = newvx

    def setYVel(self, newvy):
        self.vely = newvy


def createSSandAnimate():
    ss = SolarSystem(2, 2)

    sun = Sun("SUN", 5000, 10, 5800)
    ss.addSun(sun)

    m = Planet("MERCURY", 19.5, 1000, .25, 0, 2, "blue")
    ss.addPlanet(m)

    m = Planet("EARTH", 47.5, 5000, 0.3, 0, 2.0, "green")
    ss.addPlanet(m)

    m = Planet("MARS", 50, 9000, 0.5, 0, 1.63, "red")
    ss.addPlanet(m)

    m = Planet("JUPITER", 100, 49000, 0.7, 0, 1, "black")
    ss.addPlanet(m)

    m = Planet("Pluto", 1, 500, 0.9, 0, .5, "orange")
    ss.addPlanet(m)

    m = Planet("Asteroid", 1, 500, 1.0, 0, .75, "cyan")
    ss.addPlanet(m)

    n = Kattlite("moon", 1, 40, 0.4, 0, .75, "black")
    ss.addKattlite(n)

    numTimePeriods = 20000
    for amove in range(numTimePeriods):
        ss.movePlanets()

    ss.freeze()


createSSandAnimate()