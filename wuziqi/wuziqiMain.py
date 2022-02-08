# @Time : 2022/2/8 20:32
# @Author : WZG
# --coding:utf-8--

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption('五子棋')

while True:
    highL = 40
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((225, 255, 235))
    while highL < 600:
        pygame.draw.line(screen, (0, 0, 0), (0, highL), (600, highL), 1)
        pygame.draw.line(screen, (0, 0, 0), (highL, 0), (highL, 600), 1)

        highL += 40

    pygame.display.flip()


    #pygame.display.update()
