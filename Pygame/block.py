from pygame import *
import random

init()
screen = display.set_mode((1280, 720))
screenX = screen.get_width()
screenY = screen.get_height()

leftSide = screenX/4-50
rightSide = (screenX/4)*3-50

clock = time.Clock()
running = True

obstacles = []
colors = ("black","white","red","blue")
isLeft = True
rightDanger = False
leftDanger = False

def Obstacle():
    global rightDanger
    global leftDanger
    x = random.randint(0,3)
    if x == 0:
        obstacles.append([leftSide,0,colors[2],0])
    if x == 1:
        obstacles.append([rightSide,0,colors[3],0])
    obstaclesRem = []
    leftDanger = False
    rightDanger = False
    for x in range(len(obstacles)):
        obstacles[x][1] += screenY/8
        obstacles[x][3] += 1
        if obstacles[x][3] == 6:
            leftDanger = True
        if obstacles[x][3] == 6:
            rightDanger = True
        if obstacles[x][3] >= 8:
            obstaclesRem.append(obstacles[x])
    for x in obstaclesRem:
        obstacles.remove(x)

Obstacle()

while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT:
                isLeft = True
                Obstacle()
            if e.key == K_RIGHT:
                isLeft = False
                Obstacle()

    screen.fill(colors[0])
    for x in obstacles:
        draw.rect(screen,x[2],Rect(x[0],x[1]-50,50,50))
    if isLeft:
        draw.rect(screen,colors[1],Rect(leftSide,(screenY/4)*3-50,50,50))
        if leftDanger:
            print("Game Over")
    else:
        draw.rect(screen,colors[1],Rect(rightSide,(screenY/4)*3-50,50,50))
        if rightDanger:
            print("Game Over")
    display.flip()

    clock.tick(60)  # limits FPS to 60

quit()
