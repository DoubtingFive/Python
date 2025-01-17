import pygame
import random
import sys

size = 500
sys.setrecursionlimit(int(size*size/3*2))
tick_time = 1000/size
tick = tick_time

map = []
display_map = map

tiles_order = []
tiles = 0

special = [0,0]
filled_positions = [(0,0)]

# chances = [[0 for _ in range(size)] for _ in range(size)]
# total_probe = 0
# recursion_count = 0

min_tiles = int((size*size)/2)
max_tiles = int((size*size)/2+size*0.25)

def Tick_Display():
    global tiles_order, filled_positions, display_map, size, max_tiles
    tiles_order_len = len(tiles_order)
    _limit = max(int(max_tiles/70),1)
    if tiles_order_len > _limit:
        tiles_order_len = _limit
    for x in range(tiles_order_len):
        display_map[tiles_order[x][0]][tiles_order[x][1]] = 1
    tiles_order = tiles_order[_limit::]
    filled_positions = [(x, y) for x in range(size) for y in range(size) if display_map[x][y] == 1]

def Check_Tile(x,y):
    global tiles_count, map, tiles_order

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
            tiles_order.append([nx,ny])
            Check_Tile(nx,ny)

def Start():
    global tiles_count, map, filled_positions, special, tick, tick_time, display_map

    # global chances,total_probe,recursion_count
    # recursion_count = 0

    special = random.choice(filled_positions)
    tick = tick_time
    tiles = random.randint(min_tiles,max_tiles)
    tiles_count = tiles
    map = [[0 for _ in range(size)] for _ in range(size)]
    display_map = [[0 for _ in range(size)] for _ in range(size)]
    middle = [random.randint(0,size-1),random.randint(0,size-1)]
    map[middle[0]][middle[1]] = 1

    Check_Tile(middle[0],middle[1])


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
            if event.key == pygame.K_SPACE:
                Start()

    screen.fill("black")
    if tick < 0:
        tick = tick_time
        if size < 50: special = random.choice(filled_positions)
        if map: Tick_Display()
    else: tick -= dt

    for x in range(len(display_map)):
        for y in range(len(display_map[x])):
            if display_map[x][y] == 1:
                color = "green"
                if special[0] == x and special[1] == y:
                    color = "red"
                pygame.draw.rect(screen,color,pygame.Rect(windowSize/size*y,windowSize/size*x,windowSize/size-1,windowSize/size-1))

    pygame.display.flip()

    dt = clock.tick(120)

pygame.quit()