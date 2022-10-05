import pygame
import sys
from pygame.locals import *
from ab import mazegen

def gameloop():
    size, scale = 4,80
    r = size * scale + 100
    surf = pygame.display.set_mode((r,r))
    a = mazegen(size)
    while True:
        pygame.display.update()
        surf.fill((0,0,0))
        a = mazegen(size)
        a.AldousBroder()
        # a.AldousBroder_step()
        a.instantiateWallMaze(surf, scale)
        # if a.nvisited == a.size**2: a = mazegen(size)
        pygame.time.Clock().tick(2)

