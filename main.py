import pygame
import json
from random import randint
from bag import Bag

curBag=Bag()
print(curBag.pieces)
#keybinds
while True:
    curPiece=curBag.pieces[0]
    try:
        file=open('keyBinds.txt','r')
        binds=json.loads(file.read())
        right=binds['right']
        left=binds['left']
        down=binds['down']  
        clockWise=binds['clockWise']
        counterClockWise=binds['counterClockWise']
        DAS=binds['DAS']
        ARR=binds['DAS']    
        break 
    except:
        file=open('keyBinds.txt','w')
        temp={'left':pygame.K_LEFT,
        'right':pygame.K_RIGHT,
        'down':pygame.K_DOWN,
        'clockWise':pygame.K_UP,
        'counterClockWise':pygame.K_z,
        'DAS':10,
        'ARR':10}
        file.write(json.dumps(temp))
        
pygame.init()
color=[255,255,255]
win=pygame.display.set_mode((300,300))

#makes a clock to keep track of frames
FPS=30
clock= pygame.time.Clock()

xPos=140 
yPos=30

input_timers={left:0,right:0}#timers for das


gravity=1 #decrease to make quicker
gravityTimer=0 #keeps track of how many frames has passed to only go down after seconds
rotation=0
def rotate(dir):
    global rotation
    if dir=='+':
        if rotation==3:#resets rotation cycle
            rotation=0
        else:
            rotation+=1
    else:
        if rotation==0:#resets rotation cycle
            rotation=3
        else:
            rotation-=1

def checkTiming(key,time):#checks das timings
    global xPos
    global yPos
    if time==0:
        if key==left:
            xPos-=10
        else:
            xPos+=10
        input_timers[key]+=1
    elif time>DAS:
        if key==left:
            xPos-=10
        else:
            xPos+=10
    else:
        input_timers[key]+=1
        

running=True
while running:
    curBag.drawPiece(win,curPiece,xPos,yPos,rotation, 2)#deletes prev frame

    if gravityTimer<(gravity*FPS):#checks if it is time to do gravity
        gravityTimer=gravityTimer+1
    else:
        gravityTimer=0
        yPos=yPos+10
   
    #checks what button is pressed
    for event in pygame.event.get():

        if event.type==pygame.KEYDOWN:#binds for rotation
            if event.key==clockWise:
                rotate('+')
            if event.key==counterClockWise:
                rotate('-')

        if event.type==pygame.QUIT:#game closses
            running=False

    #checks for movement
    pressed = pygame.key.get_pressed()
    for k in input_timers:
        if pressed[k]:
            checkTiming(k,input_timers[k])
        else:
            input_timers[k]=0
    if pressed[down]:
        yPos+=10

           
            
    
    curBag.drawPiece(win,curPiece,xPos,yPos,rotation)
    pygame.display.update()
    clock.tick(FPS)# checks if it has reached the given millescoands if it hasnt it waits

