from pygame import *
import random

init()
screenX = 1280
screenY = 720
screen = display.set_mode((screenX, screenY))

blockY = (screenY/4)*3-50

font.init()
text_font = font.SysFont('impact', 80)

leftSide = (screenX/8)*3-50
rightSide = (screenX/8)*5-50

clock = time.Clock()
running = True

obstacles = []
colors = ("black","white","red","blue")
isLeft = True
rightDanger = False
leftDanger = False
isGame = True

score = 0

def Obstacle():
    global rightDanger
    global leftDanger
    global isGame
    global score
    score += 1
    x = random.randint(0,4)
    if x <= 1:
        obstacles.append([leftSide,0,colors[2],0,True])
    elif x >= 3:
        obstacles.append([rightSide,0,colors[3],0,False])
    obstaclesRem = []
    leftDanger = False
    rightDanger = False
    for x in range(len(obstacles)):
        obstacles[x][1] += screenY/8
        obstacles[x][3] += 1
        if obstacles[x][3] == 6 and obstacles[x][4]:
            leftDanger = True
        if obstacles[x][3] == 6 and not obstacles[x][4]:
            rightDanger = True
        if obstacles[x][3] >= 8:
            obstaclesRem.append(obstacles[x])
    for x in obstaclesRem:
        obstacles.remove(x)

def Reset():
    global obstacles
    global score
    score = 0
    obstacles = []
    Obstacle()

Obstacle()


while running:
    for e in event.get():
        if e.type == QUIT:
            running = False
        if e.type == KEYDOWN:
            if e.key == K_LEFT or e.key == K_a or e.key == K_s:
                isLeft = True
                Obstacle()
            if e.key == K_RIGHT or e.key == K_l or e.key == K_k:
                isLeft = False
                Obstacle()

    screen.fill(colors[0])
    for x in obstacles:
        draw.rect(screen,x[2],Rect(x[0],x[1]-50,50,50))
    if isLeft:
        draw.rect(screen,colors[1],Rect(leftSide,blockY,50,50))
        if leftDanger and isGame:
            Reset()
    else:
        draw.rect(screen,colors[1],Rect(rightSide,blockY,50,50))
        if rightDanger and isGame:
            Reset()
    text_surface = text_font.render(str(score), False, colors[1])
    textWidth = text_surface.get_width()/2
    textHeight = text_surface.get_height()/2
    screen.blit(text_surface, (screenX/2-textWidth,screenY/4-textHeight))
    display.flip()

    clock.tick(60)  # limits FPS to 60

quit()
