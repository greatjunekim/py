import pygame
import sys
from pygame.locals import QUIT,MOUSEBUTTONDOWN, MOUSEMOTION,MOUSEBUTTONUP

pygame.init()
pygame.display.set_caption("Test Window")
Surface = pygame.display.set_mode((800,400))
FPSCLOCK = pygame.time.Clock()

def main():
    pos = []
    Check = False
    mousebutton = False
    Surface.fill((0, 0, 0))
    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                Check = True
                mousebutton = True

            elif event.type == MOUSEMOTION:
                if mousebutton:
                    pos.append(event.pos)
            elif event.type == MOUSEBUTTONUP:
                mousebutton = False
                Check = False
                pos.clear()
        if Check:
            if len(pos)>1:
                pygame.draw.lines(Surface,(255,255,255), False, pos)
        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == '__main__':
    main()