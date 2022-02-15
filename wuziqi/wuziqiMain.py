# @Time : 2022/2/8 20:32
# @Author : WZG
# --coding:utf-8--

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800, 680))

pygame.display.set_caption('五子棋')


def blackQ(x, y):
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 18, 0)
    pygame.display.update()


def whiteQ(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 18, 0)
    pygame.display.update()


def qipan():
    highL = 40

    screen.fill((249, 214, 91))
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

    pygame.display.flip()


qipan()



def wuzi():
    posXY = [] # 点击的坐标
    pos_exist = [] # 已有棋子的坐标
    color_Q = 0
    exist_black = [] # 已有的黑棋
    exist_white = [] # 已有的白棋
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == True:
                    pos = pygame.mouse.get_pos()
                    if 730 > pos[0] > 680 and 65 > pos[1] > 40:  # 清空棋子
                        qipan()
                        pos_exist = []
                        exist_white = []
                        exist_black = []
                    if pos[0] % 40 > 20:
                        pos_X = pos[0] // 40 * 40 + 40
                        posXY.append(pos_X)
                    else:
                        pos_X = pos[0] // 40 * 40
                        posXY.append(pos_X)
                    if pos[1] % 40 > 20:
                        pos_Y = pos[1] // 40 * 40 + 40
                        posXY.append(pos_Y)
                    else:
                        pos_Y = pos[1] // 40 * 40
                        posXY.append(pos_Y)

                    if len(posXY) >= 2:
                        if posXY not in pos_exist and 40 <= posXY[0] <= 640 and 40 <= posXY[1] <= 640:
                            pos_exist.append(posXY)
                            if color_Q == 0:
                                whiteQ(posXY[0], posXY[1])
                                exist_white.append(posXY)
                                color_Q = 1
                            else:
                                blackQ(posXY[0], posXY[1])
                                exist_black.append(posXY)
                                color_Q = 0
                        posXY = []
                    if pos_exist:

                        x = pos_exist[-1][0]
                        y = pos_exist[-1][1]

                        count1, count2, count3, count4 = 0, 0, 0, 0
                        colorS = exist_white

                        if color_Q == 0:
                            colorS = exist_black

                        for i in range(1, 5):
                            if [x + i * 40, y] in colorS or [x - i * 40, y] in colorS:
                                count1 += 1

                        for i in range(1, 5):
                            if [x + i * 40, y + i * 40] in colorS or [x - i * 40, y - i * 40] in colorS:
                                count2 += 1

                        for i in range(1, 5):
                            if [x + i * 40, y - i * 40] in colorS or [x - i * 40, y + i * 40] in colorS:
                                count3 += 1

                        for i in range(1, 5):
                            if [x, y - i * 40] in colorS or [x, y + i * 40] in colorS:
                                count4 += 1
                        if count1 == 4 or count2 == 4 or count3 == 4 or count4 == 4:
                            if color_Q == 1:
                                clearS = pygame.image.load('3.jpg')
                                screen.blit(clearS, [280, 300])
                                pygame.display.update()
                                break
                            elif color_Q == 0:
                                clearS = pygame.image.load('4.jpg')
                                screen.blit(clearS, [280, 300])
                                pygame.display.update()
                                break

        clearS = pygame.image.load('2.jpg')
        screen.blit(clearS, [680, 40])
        pygame.display.update()


wuzi()
        #pygame.display.update()
