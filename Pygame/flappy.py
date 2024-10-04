import pygame
import random

pygame.init()

screenX = 1280
screenY = 720

screen = pygame.display.set_mode((screenX, screenY))
clock = pygame.time.Clock()
running = True

colors = ("lightblue",(255,255,0),(0,255,0),(255, 100, 100),(255, 255, 255))
# colors[x]
# 0 - background
# 1 - bird
# 2 - obstacles
# 3 - game over text
# 4 - score text

pygame.font.init()
textFont = pygame.font.SysFont('impact', 200)
gameoverTextSurface = textFont.render('Game Over', False, colors[3])
gameoverTextWidth = gameoverTextSurface.get_width()/2
gameoverTextHeight = gameoverTextSurface.get_height()/2

textFont = pygame.font.SysFont('impact', 80)
scoreTextSurface = textFont.render('Game Over', False, colors[4])
scoreTextWidth = scoreTextSurface.get_width()/2
scoreTextHeight = scoreTextSurface.get_height()/2

y = 100
vY = 0
speed = 320
g = -9.81*speed/4
fps = 0
textBlink = 1000
textBlinkCooldown = textBlink
isText = False
isGame = True
collision = False
step = 600
screenWidth = 1280
spawner = 0
obstacles=[]
score = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.K_SPACE:
            if isGame:
                vY = 500
            else:
                y = 100
                vY = 0
                spawner = 0
                isGame = True
                obstacles = []
                score = 0
    screen.fill(colors[0])
    # is game or gameover
    if isGame:
        if spawner <= screenWidth-step:
            spawner = screenWidth
            randomY = random.randint(-400,0)
            yDown = randomY+step*1.25
            obstacles.append([screenWidth,randomY,yDown,True])
        else: spawner -= speed*fps
        vY += g*fps
        y -= vY * fps
        for i in range(len(obstacles)):
            obstacles[i][0] -= speed * fps
            if obstacles[i][0] <= 360 and obstacles[i][0]+100 >= 300:
                if obstacles[i][3]:
                    score+=1
                    obstacles[i][3] = False
                if obstacles[i][1]+500 >= y or y+60 >= obstacles[i][2]:
                    collision = True
    else:
        if textBlinkCooldown < 0:
            textBlinkCooldown = textBlink
            isText = not isText
        else: textBlinkCooldown -= fps*1000

    # obstacles render
    for i in range(len(obstacles)):
        pygame.draw.rect(screen,colors[2],pygame.Rect(obstacles[i][0],obstacles[i][1],100,500))
        pygame.draw.rect(screen,colors[2],pygame.Rect(obstacles[i][0],obstacles[i][2],100,500))

    # does he lose already
    if ((y < 0 or y > 660) and isGame) or collision:
        isGame = False
        isText = True
        textBlinkCooldown = textBlink
        collision = False
    pygame.draw.rect(screen,colors[1],pygame.Rect(300,y,60,60))

    scoreTextSurface = textFont.render(str(score), False, colors[4])
    scoreTextWidth = scoreTextSurface.get_width()/2
    scoreTextHeight = scoreTextSurface.get_height()/2
    screen.blit(scoreTextSurface, (screenX/2-scoreTextWidth,screenY/4-scoreTextHeight))
    if isText:
        screen.blit(gameoverTextSurface, (screenX/2-gameoverTextWidth,screenY/2-gameoverTextHeight))
    pygame.display.flip()

    fps = clock.tick(60)/1000

pygame.quit()
