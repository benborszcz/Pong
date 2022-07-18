import random
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class DumbComputerPlayer():
    def __init__(self, paddle, ball, scale):
        self.paddle = paddle
        self.ball = ball
        self.paddle.vel = 0.60 * scale
        self.scale = scale
    
    def move(self):
        midPaddle = Point(self.paddle.x+self.paddle.width/2, self.paddle.y+(self.paddle.height/2))
        midBall = Point(self.ball.x+self.ball.width/2, self.ball.y+(self.ball.height/2))
        diff = midPaddle.y - midBall.y
        if diff > 0:
            self.paddle.moveU()
        elif diff < 0:
            self.paddle.moveD()

class RandomComputerPlayer():
    random.seed(13264)
    def __init__(self, paddle, ball, scale, isRight):
        self.paddle = paddle
        self.ball = ball
        self.isRight = isRight
        self.paddle.vel = 1.0 * scale
        self.seeking = False
        self.target = 1
        self.scale = scale
    
    def move(self):
        if self.isRight:
            if not(self.seeking) and self.ball.velX > 0:
                self.seeking = True
                self.target = random.randrange(-20,20)
            if self.seeking and self.ball.velX < 0:
                self.seeking = False
                self.target = 0
        else:
            if not(self.seeking) and self.ball.velX < 0:
                self.seeking = True
                self.target = random.randrange(-20,20)
            if self.seeking and self.ball.velX > 0:
                self.seeking = False
                self.target = 0
        midPaddle = Point(self.paddle.x+self.paddle.width/2, self.paddle.y+(self.paddle.height/2))
        midBall = Point(self.ball.x+self.ball.width/2, self.ball.y+(self.ball.height/2))
        diff = midPaddle.y - midBall.y + (self.target*self.scale)
        if diff > 0:
            self.paddle.moveU()
        elif diff < 0:
            self.paddle.moveD()

class EdgeHunterComputerPlayer():
    random.seed(13264)
    def __init__(self, paddle, ball, scale, isRight):
        self.paddle = paddle
        self.ball = ball
        self.isRight = isRight
        self.paddle.vel = 1.0 * scale
        self.seeking = False
        self.target = 1
        self.scale = scale
    
    def move(self):
        if self.isRight:
            if not(self.seeking) and self.ball.velX > 0:
                self.seeking = True
                self.target = random.randrange(20,29)
                mod = random.randint(0,1)
                if(mod == 1):
                    self.target *= -1
            if self.seeking and self.ball.velX < 0:
                self.seeking = False
                self.target = 0
        else:
            if not(self.seeking) and self.ball.velX < 0:
                self.seeking = True
                self.target = random.randrange(20,29)
                mod = random.randint(0,1)
                if(mod == 1):
                    self.target *= -1
            if self.seeking and self.ball.velX > 0:
                self.seeking = False
                self.target = 0
        midPaddle = Point(self.paddle.x+self.paddle.width/2, self.paddle.y+(self.paddle.height/2))
        midBall = Point(self.ball.x+self.ball.width/2, self.ball.y+(self.ball.height/2))
        diff = midPaddle.y - midBall.y + (self.target*self.scale)
        if diff > 0:
            self.paddle.moveU()
        elif diff < 0:
            self.paddle.moveD()


class PerfectEdgeHunterComputerPlayer():
    random.seed(13264)
    def __init__(self, paddle, ball, scale, isRight):
        self.paddle = paddle
        self.ball = ball
        self.isRight = isRight
        self.seeking = False
        self.target = 1
        self.scale = scale
    
    def move(self):
        if self.isRight:
            if not(self.seeking) and self.ball.velX > 0:
                self.seeking = True
                self.target = random.randrange(20,29)
                mod = random.randint(0,1)
                if(mod == 1):
                    self.target *= -1
            if self.seeking and self.ball.velX < 0:
                self.seeking = False
                self.target = 0
        else:
            if not(self.seeking) and self.ball.velX < 0:
                self.seeking = True
                self.target = random.randrange(20,29)
                mod = random.randint(0,1)
                if(mod == 1):
                    self.target *= -1
            if self.seeking and self.ball.velX > 0:
                self.seeking = False
                self.target = 0
        midPaddle = Point(self.paddle.x+self.paddle.width/2, self.paddle.y+(self.paddle.height/2))
        midBall = Point(self.ball.x+self.ball.width/2, self.ball.y+(self.ball.height/2))
        diff = midPaddle.y - midBall.y + (self.target*self.scale)
        if diff > 0:
            self.paddle.moveU()
        elif diff < 0:
            self.paddle.moveD()



