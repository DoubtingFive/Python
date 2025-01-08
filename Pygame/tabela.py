import pygame
import random
import sys
print (sys.getrecursionlimit())
sys.setrecursionlimit(50000)

size = 1000
dt = 0
running = True
windowSize = 1000
map = [[0 for _ in range(size)] for _ in range(size)]

min_tiles = 40
max_tiles = 60

min_tiles_count = min_tiles
max_tiles_count = max_tiles

def Check_Tile(x,y):
    neighbors = ([x,y+1],[x+1,y],[x,y-1],[x-1,y])
    for _x in neighbors:
        if _x[0] >= 0 and _x[0] < size and _x[1] >= 0 and _x[1] < size and map[_x[0]][_x[1]] == 0 and max_tiles_count > 0 and random.choice([True,False]):
            map[_x[0]][_x[1]] = 1
            max_tiles_count -= 1
            Check_Tile(_x[0],_x[1])

_temp = int(size/2)
map[_temp][_temp] = 1
Check_Tile(_temp,_temp)

pygame.init()
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 1:
                pygame.draw.rect(screen,"green",pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size,windowSize/size))

    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()