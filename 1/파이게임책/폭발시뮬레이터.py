import pygame, sys
import time
from pygame.locals import *
player = pygame.image.load('1/파이게임책/Unknown.png')
pygame.init()
d = pygame.display.set_mode((1400,1000))
pygame.display.set_caption('boom')
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            (_x, _y) = event.pos # (x, y)
            # _y = event.pos[1]
            pygame.draw.rect(d,(255,255,255),(_x,_y,100,100))
            
            
        elif event.type == KEYDOWN: 
            if event.key == K_SPACE: 
                d.blit(player, (0, 0))
                pygame.display.update()
                time.sleep(0.25)
                img_scale = pygame.transform.scale(player, (450, 300))
                d.fill((0,0,0))
                d.blit(img_scale, (0, 0))
                pygame.display.update()
                time.sleep(0.25)
                img_scale = pygame.transform.scale(player, (200, 100))
                d.fill((0,0,0))
                d.blit(img_scale, (0, 0))
                pygame.display.update()
                time.sleep(0.1)
                img_scale = pygame.transform.scale(player, (0, 0))
                d.fill((0,0,0))
                d.blit(img_scale, (0, 0))
                print("boom")

    pygame.display.update()
