import random
import pygame

class mazegen():
    def __init__(self, size):
        self.size = size
        self.nvisited = 0
        self.visited = self.make_matrix(size, size, 0)
        self.vwalls = self.make_matrix(size+1, size+1, 1)
        self.hwalls = self.make_matrix(size+1, size+1, 1)
        self.current_point = self.rand_pos()
        self.visit(self.current_point)
        # self.AldousBroder()

    def instantiateWallMaze(self, surf, scale):
        size = self.size
        for i in range(size):
            for j in range(size):
                color = (0,255,0) if self.visited[i][j] == 1 else (0,0,255)
                pygame.draw.rect(surf, color, [i*scale + 50, j*scale + 50, scale, scale])
        pygame.draw.rect(surf, (255,255,0), [self.current_point[0]*scale + 50, self.current_point[1]*scale + 50, scale, scale])
        for i in range(size+1):
            for j in range(size+1):
                s = scale/2.0
                if( self.hwalls[i][j] and i < size):
                    pygame.draw.rect(surf, (255,255,255), [i*scale + 50, j*scale + 50, scale, scale/10], scale//4)
                if( self.vwalls[i][j] and j < size ):
                    pygame.draw.rect(surf, (255,255,255), [i*scale + 50, j*scale + 50, scale/10, scale], scale//4)

    def AldousBroder(self):
        p = self.current_point

        while(self.nvisited < self.size**2):
            next_point = self.pickNeighbor(p)
            if ( self.visited[next_point[0]][next_point[1]] == 0 ):
                self.visit(next_point)
                self.removeWall(p, next_point)
            p = next_point

    def AldousBroder_step(self):
        if (self.nvisited < self.size**2):
            next_point = self.pickNeighbor(self.current_point)
            if ( self.visited[next_point[0]][next_point[1]] == 0 ):
                self.visit(next_point)
                self.removeWall(self.current_point, next_point)
            self.current_point = next_point

    def removeWall(self, p1, p2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        if(dx == -1):
            i = p1[0]
            j = p1[1]
            self.vwalls[ i ][ j ] = 0
        if(dy == -1):
            i = p1[0]
            j = p1[1]
            self.hwalls[ i ][ j ] = 0
        if(dx == 1):
            i = p1[0]+dx
            j = p1[1]
            self.vwalls[ i ][ j ] = 0
        if(dy == 1):
            i = p1[0]
            j = p1[1]+dy
            self.hwalls[ i ][ j ] = 0

    def pickNeighbor(self, p):
        i = p[0]
        j = p[1]
        all_neighbors = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        neighbors = []
        for n in all_neighbors:
            if self.checkValid(n):
                neighbors += [n]
        return neighbors[ random.randint(0, len(neighbors) - 1) ]

    def checkValid(self, point):
        ival = 0 <= point[0] and point[0] < self.size
        jval = 0 <= point[1] and point[1] < self.size
        return ival and jval

    def visit(self, p):
        self.visited[ p[0] ][ p[1] ] = 1
        self.nvisited += 1

    def rand_pos(self):
        i = random.randint(0, self.size - 1)
        j = random.randint(0, self.size - 1)
        return [i,j]

    def make_matrix(self,n,m,v):
        arr = []
        for i in range(n):
            arr += [[v]*m]
        return arr
