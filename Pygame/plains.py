import pygame
import random
import sys

sys.setrecursionlimit(2000)

size = 12
dt = 0
running = True
power_map_on = False
is_overload = False
windowSize = 600
map = [[1 for _ in range(size)] for _ in range(size)]
power_map = [[0 for _ in range(size)] for _ in range(size)]
overload = []
red_up = 1
blue_up = 2

pygame.init()
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()

def Draw():
    global power_map_on,is_overload
    power_map_on = False
    screen.fill("black")

    for x in range(size):
        for y in range(size):
            _plot = map[x][y]
            if _plot == 1:
                if is_overload: color = (128,16,32)
                else: color = "green"
                pygame.draw.rect(screen,color,pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))
            elif _plot == 2:
                pygame.draw.rect(screen,"red",pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))
            elif _plot == 3:
                pygame.draw.rect(screen,"blue",pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))
            elif _plot == 4:
                pygame.draw.rect(screen,(255,255,0),pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))
            elif _plot == 5:
                pygame.draw.rect(screen,(255,128,0),pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))

    pygame.display.flip()

def Check_Connections():
    global red_up,blue_up,overload,is_overload,power_map
    is_overload = False
    _red_up = 1
    _blue_up = 2
    power_map = [[0 for _ in range(size)] for _ in range(size)]
    for x in range(size):
        for y in range(size):
            if map[x][y] == 4:
                _red_up = _red_up * 2
            elif map[x][y] == 5:
                _blue_up = _blue_up * 3
            elif map[x][y] == 3:
                neighbours = [[x,y+1],[x+1,y],[x,y-1],[x-1,y]]
                for z in range(4):
                    _nx,_ny = neighbours[z]
                    if 0 <= _nx < size and 0 <= _ny < size:
                        if map[_nx][_ny] == 2:
                            _neighbours = [[_nx,_ny+1],[_nx+1,_ny],[_nx,_ny-1],[_nx-1,_ny]]
                            count = 0
                            for w in range(4):
                                _nx2,_ny2 = _neighbours[w]
                                if map[_nx2][_ny2] == 3:
                                    count += 1
                            if count == 0: continue
                            power_map[x][y] += red_up/count
                            power_map[_nx][_ny] += -red_up/count
                if power_map[x][y] == 0 or power_map[x][y] > blue_up:
                    is_overload = True
                    found_overload = False
                    i = 0
                    while i < len(overload):
                        if overload[i][0] == x and overload[i][1] == y:
                            found_overload = True
                            if overload[i][2] >= 3:
                                power_map[x][y] = 0
                                map[x][y] = 1
                                overload.remove([x,y,overload[i][2]])
                                i -= 1
                                if len(overload) == 0: is_overload = False
                                break
                            else:
                                overload[i][2] += 1
                        i+=1
                    if not found_overload:
                        overload.append([x,y,1])
    if not is_overload:
        overload = []
    red_up = _red_up
    if _blue_up > blue_up:
        blue_up = _blue_up
        Check_Connections()

Draw()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            _x = x/(windowSize/size)
            _y = y/(windowSize/size)
            m_press = pygame.mouse.get_pressed()
            if map[int(_x)][int(_y)] == 4 and (m_press[0] or m_press[1]):
                map[int(_x)][int(_y)] = 5
            elif m_press[1] or (map[int(_x)][int(_y)] == 5 and m_press[0]):
                map[int(_x)][int(_y)] = 4
            elif map[int(_x)][int(_y)] != 1:
                map[int(_x)][int(_y)] = 1
            elif m_press[0]:
                map[int(_x)][int(_y)] = 2
            elif m_press[2]:
                map[int(_x)][int(_y)] = 3
            Check_Connections()
            Draw()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if power_map_on:
                    power_map_on = False
                    Draw()
                    continue
                power_map_on = True
                screen.fill("black")

                for x in range(size):
                    for y in range(size):
                        _plot = power_map[x][y]
                        if _plot >= 1:
                            pygame.draw.rect(screen,(0,min(_plot*4,64),min(_plot*16,255)),pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))
                        elif _plot <= -1:
                            pygame.draw.rect(screen,(min(-_plot*16,255),min(-_plot*4,64),0),pygame.Rect(windowSize/size*x,windowSize/size*y,windowSize/size-1,windowSize/size-1))

                pygame.display.flip()

    clock.tick(60)

pygame.quit()