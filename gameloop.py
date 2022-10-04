import pygame
import sys
from pygame.locals import *
from ab import mazegen

def gameloop():
    size, scale = 40,10
    r = size * scale + 100
    surf = pygame.display.set_mode((r,r))
    while True:
        pygame.display.update()
        surf.fill((0,0,0))
        a = mazegen(size)
        a.instantiateWallMaze(surf, scale)
        pygame.time.Clock().tick(2)

