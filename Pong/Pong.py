import math
from ComputerPlayer import DumbComputerPlayer
from ComputerPlayer import RandomComputerPlayer
from ComputerPlayer import EdgeHunterComputerPlayer
from ComputerPlayer import PerfectEdgeHunterComputerPlayer

import pygame as pg
import pygame.freetype as text

print("Choose your opponent")

print("(0) Normal Computer Player")
print("(1) Random Computer Player")
print("(2) Edge Hitting Computer Player")
print("(3) Perfect Edge Hitting Computer Player")
com_decision = input("Enter (0-3): ")

pg.init()
GAME_FONT = text.SysFont('Arial', 24)
SCALE = 2
ballSpeed = 1.5*SCALE
paddleSpeed = 1.5*SCALE
sWidth = 600*SCALE
sHeight = 500*SCALE
ballSize = 6*SCALE
paddleHeight = 60*SCALE
paddleWidth = 6*SCALE
window = pg.display.set_mode((sWidth,sHeight))
pg.display.set_caption("First Game")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

white = Color(255,255,255)
red = Color(255,0,0)
gray = Color(155,155,155)
blue = Color(0,0,255)

class Rectangle:
    
    def __init__(self, x, y, width, height, vel, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.color = color

    def draw(self):
        pg.draw.rect(window, (self.color.r, self.color.g, self.color.b), (self.x,self.y,self.width, self.height))

    def update(self):
        self.draw()

class Paddle(Rectangle):
    
    score = 0;
    def __init__(self, x, y, width, height, vel, color):
        super().__init__(x, y, width, height, vel, color)

    def moveU(self):
        if  self.y > self.vel:
            self.y -= self.vel

    def moveD(self):
        if  self.y < sHeight - self.height - self.vel:
            self.y += self.vel

class Ball(Rectangle):
    
    def __init__(self, x, y, width, height, velX, velY, color):
        super().__init__(x, y, width, height, math.sqrt(velY*velY + velX*velX), color)
        self.velX = velX
        self.velY = velY

    def move(self):
        self.x += self.velX
        self.y += self.velY

    def update(self):
        self.move()
        self.draw()

def checkAllInputs(paddleL, paddleR):
    keys = pg.key.get_pressed()
    checkInputs(paddleR, keys[pg.K_UP], keys[pg.K_DOWN])
    checkInputs(paddleL, keys[pg.K_w], keys[pg.K_s])


def checkInputs(paddle, up, down):
    keys = pg.key.get_pressed()
    if up:
        paddle.moveU()
    if down:
        paddle.moveD()

def isCollding(ob1, ob2):
    l1 = Point(ob1.x, ob1.y)
    l2 = Point(ob2.x, ob2.y)
    r1 = Point(ob1.x+ob1.width, ob1.y+ob1.height)
    r2 = Point(ob2.x+ob2.width, ob2.y+ob2.height)
    if (l1.x == r1.x or l1.y == r1.y or l2.x == r2.x or l2.y == r2.y):
        return False
    if(l1.x > r2.x or l2.x > r1.x):
        return False
    if(r1.y <= l2.y or r2.y <= l1.y):
        return False

    return True

def findIntersection(ob1, ob2):
    mid1 = Point(ob1.x+ob1.width/2, ob1.y+(ob1.height/2))
    mid2 = Point(ob2.x+ob2.width/2, ob2.y+(ob2.height/2))
    return ((mid1.y-mid2.y) / (ob1.height/2) ) * (7*math.pi/24)

def checkCollisions(collideList):
    if isCollding(collideList[0],collideList[2]):
       intersection = findIntersection(collideList[0],collideList[2])
       collideList[2].velX = -ballSpeed * math.cos(intersection)
       collideList[2].velY = ballSpeed * -math.sin(intersection)
    if isCollding(collideList[1],collideList[2]):
       intersection = findIntersection(collideList[1],collideList[2])
       collideList[2].velX = ballSpeed * math.cos(intersection)
       collideList[2].velY = ballSpeed * -math.sin(intersection)
    if isCollding(collideList[3],collideList[2]):
       collideList[2].velY *= -1
    if isCollding(collideList[4],collideList[2]):
       collideList[2].velY *= -1
    if isCollding(collideList[5],collideList[2]):
       pg.time.delay(5)
       collideList[1].score+=1
       GAME_FONT.render_to(window, (sWidth/2-8, 2), str(collideList[1].score)+" - "+str(collideList[0].score), (255,255,255))
       pg.time.delay(1000)
       collideList[1].y = sHeight/2 - 30
       collideList[0].y = sHeight/2 - 30
       update(collideList)
       pg.time.delay(500)
       collideList[2].x = sWidth/2 - 3 
       collideList[2].y = sHeight/2 - 3
       collideList[2].velY = 0
       collideList[2].velX = ballSpeed/collideList[2].velX
    if isCollding(collideList[6],collideList[2]):
       pg.time.delay(5)
       collideList[0].score+=1
       pg.time.delay(1000)
       GAME_FONT.render_to(window, (sWidth/2-8, 2), str(collideList[1].score)+" - "+str(collideList[0].score), (255,255,255))
       collideList[0].y = sHeight/2 - paddleHeight/2
       collideList[1].y = sHeight/2 - paddleHeight/2
       update(collideList)
       pg.time.delay(500)
       collideList[2].x = sWidth/2 - 3 
       collideList[2].y = sHeight/2 - 3
       collideList[2].velY = 0
       collideList[2].velX = ballSpeed/collideList[2].velX

def checkQuit():
    pg.time.delay(3)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            return False
    return True

def update(updateList):
    window.fill((0,0,0))
    for u in updateList:
        u.update()
    GAME_FONT.render_to(window, (sWidth/2-8, 2), str(updateList[1].score)+" - "+str(updateList[0].score), (255,255,255))
    pg.display.update()



paddleL = Paddle(10, sHeight/2 - paddleHeight/2, paddleWidth, paddleHeight, paddleSpeed, red)
paddleR = Paddle(sWidth - 10 - paddleWidth, sHeight/2 - paddleHeight/2, paddleWidth, paddleHeight, paddleSpeed, blue)
ball = Ball(sWidth/2-ballSize/2, sHeight/2 - ballSize/2, ballSize, ballSize, ballSpeed, 0, white)
wallT = Rectangle(0, 0, sWidth, 22, 0, gray)
wallB = Rectangle(0, sHeight-6, sWidth, 6, 0, gray)
wallR = Rectangle(0, 0, 6, sHeight, 0, gray)
wallL = Rectangle(sWidth-6, 0, 6, sHeight, 0, gray)

drawList = [paddleR, paddleL, ball, wallT, wallB, wallL, wallR]

op = EdgeHunterComputerPlayer(paddleL, ball, SCALE, False)
if com_decision == 1:
    op = PerfectEdgeHunterComputerPlayer(paddleL, ball, SCALE, False)
elif com_decision == 2:
    op = RandomComputerPlayer(paddleL, ball, SCALE, False)
elif com_decision == 3:
    op = DumbComputerPlayer(paddleL, ball, SCALE, False)

while checkQuit():
    checkAllInputs(paddleL, paddleR)
    checkCollisions(drawList)
    op.move()
    update(drawList)

pg.quit()



