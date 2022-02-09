# @Time : 2022/2/8 20:32
# @Author : WZG
# --coding:utf-8--

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 680))

pygame.display.set_caption('五子棋')

screen.fill((249, 214, 91))


def blackQ(x, y):
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 18, 0)


def whiteQ(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 18, 0)


posXY = []
while True:
    highL = 40
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            pos_X = pos[0] // 40 * 40
            pos_Y = pos[1] // 40 * 40
            posXY.append(pos_X)
            posXY.append(pos_Y)
            if len(posXY) == 2:
                print(pos_X, pos_Y)
                blackQ(posXY[0], posXY[1])
                posXY = []

    blackQ(160, 160)
    while highL <= 640:# 基本棋盘
        pygame.draw.line(screen, (0, 0, 0), (40, highL), (640, highL), 1)
        pygame.draw.line(screen, (0, 0, 0), (highL, 40), (highL, 640), 1)

        highL += 40
    # 棋盘加粗和黑点部分

    pygame.draw.line(screen, (0, 0, 0), (40, 200), (640, 200), 2)
    pygame.draw.line(screen, (0, 0, 0), (40, 480), (640, 480), 2)

    pygame.draw.line(screen, (0, 0, 0), (200, 40), (200, 640), 2)
    pygame.draw.line(screen, (0, 0, 0), (480, 40), (480, 640), 2)
    pygame.draw.rect(screen, (0, 0, 0), ((197, 197), (8, 8)), 8)
    pygame.draw.rect(screen, (0, 0, 0), ((197, 477), (8, 8)), 8)
    pygame.draw.rect(screen, (0, 0, 0), ((477, 197), (8, 8)), 8)
    pygame.draw.rect(screen, (0, 0, 0), ((477, 477), (8, 8)), 8)


    pygame.display.flip() #更新全部显示


    #pygame.display.update()
