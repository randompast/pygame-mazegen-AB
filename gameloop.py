import pygame
import sys
from pygame.locals import *
from ab import mazegen

def gameloop():
    size, scale = 8,80
    r = size * scale + 100
    surf = pygame.display.set_mode((r,r))
    a = mazegen(size)
    playing = True
    while True:
        pygame.display.update()
        surf.fill((0,0,0))
        # a = mazegen(size)
        # a.AldousBroder()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode == 'p':
                    playing = not playing
        if playing:
            a.AldousBroder_step()
            if a.nvisited == a.size**2: a = mazegen(size)
        a.instantiateWallMaze(surf, scale)
        pygame.time.Clock().tick(60)

#   convert AB-step-4fps.gif -coalesce -layers RemoveDups  gif:- | gif_anim_montage - AB-step-4fps-rdups.gif