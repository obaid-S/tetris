

import pygame
import json
from random import randint
from bag import Bag
from board import Board
 
 
curBag = Bag()
allBag = curBag.pieces
 
# win init
pygame.init()
win = pygame.display.set_mode((300, 300))
win.fill([70, 120, 70])
# makes it so that u can give a alpha value
gridScreen = pygame.Surface((1000, 1000), pygame.SRCALPHA)
 
 
# makes a clock to keep track of frames
FPS = 30
clock = pygame.time.Clock()
 
startxPos = 100
startyPos = 30
 
gravity = 1  # decrease to make quicker
 
playerNum = 1  # num of players
players = []
for player in range(1, (playerNum+1)):
    player = Board(startxPos, startyPos, player, allBag)
    players.append(player)
 
 
running = True
while running:
    for player in players:
        player.grid(win, gridScreen)
        player.draw_piece(win, 2)  # deletes prev frame
        player.gravity(FPS, gravity)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())
            if event.type == pygame.KEYDOWN:  # binds for rotation
                if event.key == player.clockWise:
                    player.rotate('+')
                if event.key == player.counterClockWise:
                    player.rotate('-')
 
            if event.type == pygame.QUIT:  # game closses
                running = False
 
        # checks for movement
        pressed = pygame.key.get_pressed()
        for k in player.input_timers:
            if pressed[k]:
                player.check_timing(k, player.input_timers[k])
            else:
                player.input_timers[k] = 0
        if pressed[player.down]:
            player.curY += 10
 
        player.draw_piece(win)
    pygame.display.update()
    # checks if it has reached the given millescoands if it hasnt it waits
    clock.tick(FPS)
 


