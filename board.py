
import json
import pygame
from bag import get_data
 
 
class Board:
 
    def __init__(self, firstX, firstY, playerNum, curBag):
        while True:
            try:
                file = open('keyBinds.txt', 'r')
                binds = json.loads(file.read())
                binds = binds[f'player{playerNum}']
                self.right = binds['right']
                self.left = binds['left']
                self.down = binds['down']
                self.clockWise = binds['clockWise']
                self.counterClockWise = binds['counterClockWise']
                self.DAS = binds['DAS']
                self.ARR = binds['ARR']
                break
            except:
                file = open('keyBinds.txt', 'w')
                temp = {f'player{playerNum}': {  # gets binds of player
                        'left': pygame.K_LEFT,
                        'right': pygame.K_RIGHT,
                        'down': pygame.K_DOWN,
                        'clockWise': pygame.K_UP,
                        'counterClockWise': pygame.K_z,
                        'DAS': 10,
                        'ARR': 10}}
                file.write(json.dumps(temp))
        self.rotation = 0
        self.input_timers = {self.left: 0, self.right: 0}
        self.firstX = firstX
        self.firstY = firstY
        self.curX = self.firstX+40
        self.curY = self.firstY
        self.piece = curBag[0]
        self.gravityTimer = 0
 
    # checks das timings
    def check_timing(self, key, time, ):
        if time == 0:
            if key == self.left:
                if self.curX > 100:
                    self.curX -= 10
            else:
                if self.curX < 200:
                    self.curX += 10
            self.input_timers[key] += 1
        elif time > self.DAS:
            if key == self.left:
                if self.curX > 100:
                    self.curX -= 10
            else:
                if self.curX < 200:
                    self.curX += 10
        else:
            self.input_timers[key] += 1
 
    # creates background grid
    def grid(self, win, gridScreen):
        height = 20
        len = 10
        background = pygame.Surface((100, 200))
        background.fill([0, 0, 0])
        for box in range(int(len)):
            for boxs in range(int(height)):
                pygame.draw.rect(gridScreen, [80, 80, 80, 100], [
                                 (box)*10, (boxs)*10, 10, 10], 1)
        win.blit(background, (self.firstX, self.firstY))
        win.blit(gridScreen, (self.firstX, self.firstY))
 
    # rotate piece
    def rotate(self, dir):
        if dir == '+':
            if self.rotation == 3:  # resets rotation cycle
                self.rotation = 0
            else:
                self.rotation += 1
        else:
            if self.rotation == 0:  # resets rotation cycle
                self.rotation = 3
            else:
                self.rotation -= 1
 
    # draws Piece
    def draw_piece(self, win, color=0):
        pos = get_data(self.rotation, self.piece)
        if color == 0:
            for i in range(4):
                pygame.draw.rect(win, get_data('color', self.piece),  [
                                 self.curX+pos[i][0], self.curY+pos[i][1], 10, 10])
        else:
            for i in range(4):
                pygame.draw.rect(win, [0, 0, 0], [
                                 self.curX+pos[i][0], self.curY+pos[i][1], 10, 10])
 
    def gravity(self, FPS, gravity):
        # checks if it is time to do gravity
        if self.gravityTimer < (gravity*FPS):
            self.gravityTimer = self.gravityTimer+1
        else:
            self.gravityTimer = 0
            self.curY = self.curY+10
 
