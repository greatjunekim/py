import pygame
import sys
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN

pygame.init()
pygame.display.set_caption("Test Window")
pygame.key.set_repeat(10,10)
Surface = pygame.display.set_mode((500,400))
FPSCLOCK = pygame.time.Clock()

def main():
    xpos = 100
    ypos = 100
    while True:
        Surface.fill((0,0,0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_LEFT:
                    xpos -= 10
                if event.key == K_RIGHT:
                    xpos += 10
                if event.key == K_UP:
                    ypos -= 10
                if event.key == K_DOWN:
                    ypos += 10
        pygame.draw.circle(Surface, (255, 255, 255), (xpos, ypos), 20)
        pygame.display.update()
        FPSCLOCK.tick(30)
if __name__ == '__main__':
    main()
# for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == KEYDOWN:
#                 if event.key == K_LEFT:
#                     xpos -= 10
#                 if event.key == K_RIGHT:
#                     xpos += 10
#                 if event.key == K_UP:
#                     ypos -= 10
#                 if event.key == K_DOWN:
#                     ypos += 10