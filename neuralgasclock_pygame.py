import codebookvector as cbv
import digit
import datetime
import numpy as np

from neuralgasclock import *
import pygame

pygame.init()

screen = pygame.display.set_mode((int(W), int(H)))
fps = 30
clock = pygame.time.Clock()
white = (255,255,255); black = (0,0,0)

while True:
    screen.fill(white, (0, 0, int(W), int(H)))

    time = datetime.datetime.now()
    d = newDigit(time, True)
    x = np.array([]); y = np.array([])

    for i in xrange(6):  qsort(TimeGas[i], d[i])

    for num in xrange(6):
        for particle in xrange(N):
            TimeGas[num][particle].learn(d[num][0],d[num][1])
            x = np.append(x, TimeGas[num][particle].x)
            y = np.append(y, TimeGas[num][particle].y)
            pygame.draw.circle(screen, black, (int(x[-1]),int(y[-1])), 1)

    #for pos in zip(x,y):
        #pos = map(int,pos)
        #pygame.draw.circle(screen, (250,250,250), pos, 1)

    pygame.display.update()
    clock.tick(fps)
