import pygame
import random
import sys

tick_time = 600
tick = tick_time

size = 500
sys.setrecursionlimit(int(size*size/3*2))

filled_positions = [(0,0)]
map = []
special = [0,0]
# chances = [[0 for _ in range(size)] for _ in range(size)]
# total_probe = 0
# recursion_count = 0

min_tiles = int(size*size/2)
max_tiles = int(size*size/2+size*0.25)

print(f"{min_tiles}-{max_tiles}")

def Check_Tile(x,y):
    global tiles_count, map

    # global recursion_count
    # recursion_count += 1

    neighbours = [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]
    neighbours = [(_nx, _ny) for _nx, _ny in neighbours if 0 <= _nx < size and 0 <= _ny < size and map[_nx][_ny] == 0]

    if not neighbours or tiles_count <= 0:
        return
    if len(neighbours) != 1:
        _delete = random.randint(0,len(neighbours)-1)
        for _ in range(_delete):
            neighbours.remove(neighbours[random.randint(0,len(neighbours)-1)])

    random.shuffle(neighbours)
    for nx, ny in neighbours:
        if tiles_count > 0:
            map[nx][ny] = 1
            tiles_count -= 1
            Check_Tile(nx,ny)

def Start():
    global tiles_count, map, filled_positions, special, tick, tick_time

    # global chances,total_probe,recursion_count
    # recursion_count = 0

    special = random.choice(filled_positions)
    tick = tick_time
    tiles = random.randint(min_tiles,max_tiles)
    print(f"Tiles = {tiles}")
    tiles_count = tiles
    map = [[0 for _ in range(size)] for _ in range(size)]
    middle = [random.randint(0,size-1),random.randint(0,size-1)]
    map[middle[0]][middle[1]] = 1

    Check_Tile(middle[0],middle[1])

    filled_positions = [(x, y) for x in range(size) for y in range(size) if map[x][y] == 1]

    # print(f"recursion_count = {recursion_count}")
    # print("map:")
    # for x in map: print(x)
    # print()
    # total_probe += 1
    # for x,y in filled_positions:
    #     chances[x][y] += 1
    # print("\nChances:")
    # for x in chances: print(x)
    # print()

dt = 0
running = True
windowSize = 1000
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
    if tick < 0:
        tick = tick_time
        special = random.choice(filled_positions)
    else: tick -= dt

    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 1:
                color = "green"
                if special[0] == x and special[1] == y:
                    color = "red"
                pygame.draw.rect(screen,color,pygame.Rect(windowSize/size*y,windowSize/size*x,windowSize/size-1,windowSize/size-1))

    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()