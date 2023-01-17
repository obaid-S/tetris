import json
import pygame
from bag import get_data
from bag import Bag
from bag import queueDic

class Board:
    def __init__(self, firstX, firstY, playerNum):
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
        self.board={
            
        }
            #20x10 list
        self.input_timers = {self.left: 0, self.right: 0}
        self.firstX = firstX
        self.firstY = firstY
        self.curX = self.firstX+40
        self.curY = self.firstY
        self.bag=Bag()
        self.piece = self.bag.pieces[0]
        self.gravityTimer = 0
        self.bottomBorder=pygame.Rect(self.firstX,self.firstY+200,100,10)
        self.rightBorder=pygame.Rect(self.firstX+100,self.firstY-20,10,220)
        self.leftBorder=pygame.Rect(self.firstX-10,self.firstY-20,10,220)
        self.blocks=[]
        self.update_blocks()

        

 
    # checks das timings
    def check_timing(self, key ):
        if self.input_timers[key] == 0:
            if key == self.left:
                if self.curX > 90:
                    self.curX -= 10
            else:
                if self.curX < 190:
                    self.curX += 10
            self.input_timers[key] += 1
        elif self.input_timers[key] > self.DAS:
            if key == self.left:
                if self.curX > 90:
                    self.curX -= 10
            else:
                if self.curX < 190:
                    self.curX += 10
        else:
            self.input_timers[key] += 1
 
    # creates background grid
    def grid(self, win, gridScreen):
        height = 20
        len = 10
        background = pygame.Surface((100, 210))
        background.fill([0, 0, 0])
        for box in range(int(len)):
            for boxs in range(int(height)):
                pygame.draw.rect(gridScreen, [80, 80, 80, 100], [
                                 (box)*10, (boxs)*10, 10, 10], 1)
        win.blit(background, (self.firstX, self.firstY-10))
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
        self.update_blocks()
        self.check_collide()
        if color == 0:
            for block in self.blocks:
                pygame.draw.rect(win, get_data('color', self.piece), block)
        else:
            for block in self.blocks:
                pygame.draw.rect(win, [0, 0, 0], block)
                
        pygame.draw.rect(win,[200,20,20],self.leftBorder)
        pygame.draw.rect(win,[200,20,20],self.rightBorder)
        pygame.draw.rect(win,[20,200,20],self.bottomBorder)
        
            
    
    def gravity(self, FPS, gravity):
        # checks if it is time to do gravity
        if self.gravityTimer < (gravity*FPS):
            self.gravityTimer = self.gravityTimer+1
        else:
            self.gravityTimer = 0
            self.curY = self.curY+10
 
    def update_blocks(self):
        self.blocks=[]
        pos = get_data(self.rotation, self.piece)
        for i in range (4):
            temp=pygame.Rect(self.curX+pos[i][0], self.curY+pos[i][1], 10, 10)
            self.blocks.append(temp)

    def check_collide(self):
        for block in self.blocks:#left and right border
            if block.colliderect(self.rightBorder):
                self.curX-=10
                break
            elif block.colliderect(self.leftBorder):
                self.curX+=10
                print(self.curX,block)
                break
        for block in self.blocks:#bottom border
            if block.colliderect(self.bottomBorder):
                del self.bag.pieces[0]
                print(self.bag.pieces)
                if len(self.bag.pieces)==0:
                    self.new_bag()
                else:
                    self.piece=self.bag.pieces[0]
                self.rotation=0
                self.curX = self.firstX+40
                self.curY = self.firstY
                break
        self.update_blocks()



    def new_bag(self):
        if self.bag.queuePlace < max(queueDic):#checks if there is a higher bag, if there is new one isnt made
            self.bag.queuePlace+=1
            self.bag.pieces=queueDic[self.bag.queuePlace]
        else:
            self.bag.make_new_bag()
