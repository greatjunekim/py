import time
import pygame
import sys
from pygame.locals import *

pygame.init()
pygame.display.set_caption("Test Window")
Surface = pygame.display.set_mode((600,300))
FPSCLOCK = pygame.time.Clock()
def main(): 
    speed = 1
    moveToY = 0
    moveToX = 0
    x = 0
    y = 0

    # 바닥속성
    plateColor = (1,255,155)
    plateRect = (0,0,1500,1400)
    plateLevel = 0

    # 광물 속성
    mRect = (10, 20, 10, 10)
    mLevel = 1
    mColor = (200,50,40)

    
    # player
    playerColor = (1,55,155)

    changeColor = (0,0,0)
    changeColorUntil = time.time() - 1


    while True:
        #print(f'광물x = {mRect[0]}')
        isMouseDown = False

        Surface.fill((0,0,0))
        for event in pygame.event.get():
            print(event)
            print(f'type: {event.type}')
            #x 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                isMouseDown = True

            if event.type == KEYDOWN:
                if event.scancode == 54: 
                    speed = speed - 1
                if event.scancode == 55:
                    speed = speed + 1
                if event.scancode == 79: 
                    moveToX = +speed
                if event.scancode == 80:
                    moveToX = -speed
                if event.scancode == 81:
                    moveToY = +speed
                if event.scancode == 82:
                    moveToY = -speed

            if event.type == KEYUP:
                if event.scancode == 79 or event.scancode == 80: 
                    moveToX = 0
                if event.scancode == 81 or event.scancode == 82:
                    moveToY = 0

            # if event.type == MOUSEBUTTONDOWN:
            #     print("뿌셔뿌셔")

        x = x + moveToX
        y = y + moveToY

        if x < 0: x = 0
        if 600 - 10 < x: x = 600 - 10
        if y < 0: y = 0
        if 300 - 10 < y: y = 300 - 10

        
        dx = mRect[0] - x
        dy = mRect[1] - y
        #print(f'dx:{dx}')
        #print(f'dy:{dy}')

        if dx < 0: dx = -dx
        if dy < 0: dy = -dy

        if isMouseDown and dx < 5 and dy < 5:
            print("x,y 차이가 5 미만이다 ")
            changeColor = (255,0,0)
            changeColorUntil = time.time() + 0.2
            
            
        #맨 밑바닥
        pygame.draw.rect(Surface, plateColor, plateRect)
        
        #광물
        pygame.draw.rect(Surface, mColor, mRect)

        #플래이어
        playerRect = (x, y, 10, 10)
        
        if time.time() < changeColorUntil: 
            playerColor = changeColor
        else:
            playerColor = (1, 55, 155)

        pygame.draw.rect(Surface, playerColor, playerRect)

        # print(f'x,y: {playerRect}')

        pygame.display.update()
        FPSCLOCK.tick(30)

if __name__ == '__main__':
    main()