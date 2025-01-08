import pygame
import random
import sys

sys.setrecursionlimit(2000)

size = 12
dt = 0
running = True
windowSize = 1000
map = []

min_tiles = 40
max_tiles = 60

tiles = random.randint(min_tiles,max_tiles)
tiles = 10

def Check_Tile(x,y):
    global loop_count
    global tiles_count
    global map
    neighbours = ([x,y+1],[x+1,y],[x,y-1],[x-1,y])
    for n_pos in neighbours:
        loop_count += 1
        if n_pos[0] >= 0 and n_pos[0] < size and n_pos[1] >= 0 and n_pos[1] < size and tiles_count > 0 and random.choice([True,False]):
            if map[n_pos[0]][n_pos[1]] == 0:
                map[n_pos[0]][n_pos[1]] = 1
                tiles_count -= 1
            Check_Tile(n_pos[0],n_pos[1])


def Start():
    global loop_count
    global code_execution
    global tiles_count
    global tiles
    global map
    tiles_count = tiles
    loop_count = 0
    code_execution = False
    map = [[0 for _ in range(size)] for _ in range(size)]
    middle = [random.randint(0,size-1),random.randint(0,size-1)]
    map[middle[0]][middle[1]] = 1
    while tiles_count > 0:
        Check_Tile(middle[0],middle[1])
        if tiles_count <= 0:
            break
        pos = [0,0]
        while map[pos[0]][pos[1]] == 0:
            loop_count += 1
            pos = [random.randint(0,size-1),random.randint(0,size-1)]
        Check_Tile(pos[0],pos[1])
    # print()
    # for x in map:
    #     print(x)
    # print(f"\nloops = {loop_count}\n")

pygame.init()
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            Start()

    screen.fill("black")

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 1:
                pygame.draw.rect(screen,"green",pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))

    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()
