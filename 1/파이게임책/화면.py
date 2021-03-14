
import pygame, sys 
from pygame.locals import *

isBigSize = False
x = 0
y = 0

xSpeed = 0
ySpeed = 0

def toggleScreenSize():
    global isBigSize
    if isBigSize:
        pygame.display.set_mode((300,400))
        isBigSize = False
    else:
        pygame.display.set_mode((1400,1000))
        isBigSize = True
pygame.init()
d = pygame.display.set_mode((300,400))
pygame.display.set_caption('hello word!')
player = pygame.image.load('1/파이게임책/soldier3.png')

while True:
    for event in pygame.event.get():
        if (event.type != MOUSEMOTION):
            print(event)

        if event.type == KEYUP and event.key == 27:
            toggleScreenSize()
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN and event.key == 1073741903: # right key
            xSpeed = +5
        elif event.type == KEYUP and event.key == 1073741903: # right key
            xSpeed = 0
            
        if event.type == KEYDOWN and event.key == 1073741904: # left key
            xSpeed = -5
        elif event.type == KEYUP and event.key == 1073741904: # left key
            xSpeed = 0
        
        if event.type == KEYDOWN and event.key == 1073741905: # down key
            ySpeed = +5
        elif event.type == KEYUP and event.key == 1073741905: # down key
            ySpeed = 0
        
        if event.type == KEYDOWN and event.key == 1073741906: # up key
            ySpeed = -5
        elif event.type == KEYUP and event.key == 1073741906: # up key
            ySpeed = 0
    x = x + xSpeed
    y = y + ySpeed
    d.fill((0,0,0))
    d.blit(player, (x, y))    
    pygame.display.update()
    



    
        
    


    