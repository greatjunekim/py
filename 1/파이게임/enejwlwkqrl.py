import pygame #파이 게임 모듈 임포트
from random import randint
import sys
import time
from pygame.locals import QUIT,MOUSEBUTTONDOWN,KEYDOWN,K_SPACE

pygame.init() #파이 게임 초기화
WIDTH = 600
HEIGHT = 600
Large_Font = pygame.font.SysFont(None, 60)
Small_Font = pygame.font.SysFont(None, 36)
pygame.display.set_caption('CATCHING!_HAEDAL')
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT)) #화면 크기 설정
FPSCLOCK = pygame.time.Clock()

def main():
    Start_Time = int(time.time())
    GiveTime = 60
    Score = 0
    Miss = 0
    Game_Start = False
    Game_Over = False
    Start_image = pygame.image.load('FrontHaedal.png')
    End_image = pygame.image.load('BackHaedal.png')
    Sit_image = pygame.image.load('SitHaedal.png')
    Haedal = Sit_image.get_rect(left= randint(0,WIDTH - Sit_image.get_width()),top = randint(30,HEIGHT - Sit_image.get_height()))
    Start_Message = Small_Font.render("Game_Start : SpaceBar",True,(0,0,0))
    Over_Message = Large_Font.render("GAME_OVER",True,(0,0,0))
    while True: #게임 루프
        Score_Message = Small_Font.render("Score : {}".format(Score),True,(255,255,255))
        MissCount_Message = Small_Font.render("Miss : {}".format(Miss),True,(255,255,255))
        Score_End_Message = Large_Font.render("Total Score : {}".format(Score - Miss), True, (0, 0, 0))
        Time_Message = Small_Font.render("Time : {}".format(GiveTime), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    Game_Start = True
            elif event.type == MOUSEBUTTONDOWN:
                if Game_Start:
                    if Haedal.collidepoint(event.pos):
                        Score += 1
                    else:
                        Miss += 1
                    Haedal = Sit_image.get_rect(left=randint(0, WIDTH - Sit_image.get_width()),
                                                top=randint(30, HEIGHT - Sit_image.get_height()))

        #게임이 시작되기전 대기 화면
        if Game_Start == False and Game_Over == False:
            Loading_Time = int(time.time())
            SURFACE.fill((255,255,255))
            SURFACE.blit(Start_image,(WIDTH/2 +100, HEIGHT/2))
            SURFACE.blit(Start_Message,(WIDTH/2-200,HEIGHT/2))

        #게임이 시작
        elif Game_Start == True and Game_Over == False:
            Current_Time = int(time.time())
            SURFACE.fill((0,0,0))
            SURFACE.blit(Sit_image,Haedal)
            SURFACE.blit(Score_Message,(15,15))
            SURFACE.blit(MissCount_Message, (WIDTH/2-30, 15))
            SURFACE.blit(Time_Message,(WIDTH-130,15))
            GiveTime = 60 - (Current_Time - Start_Time) + (Loading_Time - Start_Time)
            #제한 시간 오버
            if GiveTime <= 0:
                Game_Over = True
                Game_Start = False
                GiveTime = 0
        elif Game_Over ==True:
            SURFACE.fill((255,255,255))
            SURFACE.blit(Over_Message,(WIDTH/2-200,HEIGHT/2))
            SURFACE.blit(Score_End_Message, (WIDTH/2-150,HEIGHT/2-100))
            SURFACE.blit(End_image,(WIDTH/2 +100, HEIGHT/2))


        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__ == '__main__':
    main()

