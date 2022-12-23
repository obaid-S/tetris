import random
import pygame

shapes=['I','O','L','J','Z','S','T']
I={
    'color':[144, 233, 239],
    0:[[-10,0],[0,0],[10,0],[20,0]],
    1:[[10,-10],[10,0],[10,10],[10,20]],
    2:[[-10,10],[0,10],[10,10],[20,10]],#diff rotatioins
    3:[[0,-10],[0,0],[0,10],[0,20]]
}
O={
    'color':[240,230,140],
    0:[[0,0],[10,0],[0,10],[10,10]],
    1:[[0,0],[10,0],[0,10],[10,10]],
    2:[[0,0],[10,0],[0,10],[10,10]],
    3:[[0,0],[10,0],[0,10],[10,10]]
}
J={
    'color':[0, 0, 255],
    0:[[-10,-10],[-10,0],[0,0],[10,0]],
    1:[[10,-10],[0,-10],[0,0],[0,10]],
    2:[[-10,0],[0,0],[10,0],[10,10]],
    3:[[0,-10],[0,0],[0,10],[-10,10]]
}
L={
    'color':[250, 150, 70],
    0:[[10,-10],[10,0],[0,0],[-10,0]],
    1:[[0,-10],[0,0],[0,10],[10,10]],
    2:[[-10,10],[-10,0],[0,0],[10,0]],
    3:[[-10,-10],[0,-10],[0,0],[0,10]]
}
S={
    'color':[40, 240, 70],
    0:[[-10,0],[0,0],[0,-10],[10,-10]],
    1:[[0,-10],[0,0],[10,0],[10,10]],
    2:[[-10,10],[0,10],[0,0],[10,0]],
    3:[[-10,-10],[-10,0],[0,0],[0,10]],
}
Z={
    'color':[220, 20, 60],
    0:[[-10,-10],[0,-10],[0,0],[10,0]],
    1:[[10,-10],[10,0],[0,0],[0,10]],
    2:[[-10,0],[0,0],[0,10],[10,10]],
    3:[[-10,10],[-10,0],[0,0],[0,-10]],
}
T={
    'color':[100, 50, 150],
    0:[[-10,0],[0,0],[0,-10],[10,0]],
    1:[[0,-10],[0,0],[0,10],[10,0]],
    2:[[-10,0],[0,0],[0,10],[10,0]],
    3:[[-10,0],[0,-10],[0,0],[0,10]]
}


class Bag:
    def __init__(self):
        self.pieces=[]
        self.newBag()
        
    def newBag(self):
        temp=shapes
        for i in range(7):
            temp2=temp[random.randint(0,len(temp)-1)]
            self.pieces.append(temp2)
            temp.remove(temp2)

    def getData(self,val,piece):
        if piece=='I':
            return I[val]
        if piece=='O':
            return O[val]
        if piece=='T':
            return T[val]
        if piece=='L':
            return L[val]
        if piece=='J':
            return J[val]
        if piece=='S':
            return S[val]
        if piece=='Z':
            return Z[val]

    def drawPiece(self,win,piece,xPos,yPos, rotation, color=0):
        if color==0:
            for i in range(4):
                pos=self.getData(rotation,piece)
                print(rotation,pos)

                pygame.draw.rect(win, self.getData('color',piece), [xPos+pos[i][0],yPos+pos[i][1],10,10])
        else:
            for i in range(4):
                pos=self.getData(rotation,piece)
                pygame.draw.rect(win, [0,0,0], [xPos+pos[i][0],yPos+pos[i][1],10,10])



            