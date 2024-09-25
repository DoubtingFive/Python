import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

pygame.font.init()
text_font = pygame.font.SysFont('impact', 200)
text_surface = text_font.render('Game Over', False, (255, 100, 100))
gameoverTextWidth = text_surface.get_width()/2
gameoverTextHeight = text_surface.get_height()/2

y = 100
vY = 0
speed = 320
g = -9.81*speed/4
fps = 0
textBlink = 1000
textBlinkCooldown = textBlink
isText = True
isGame = True
collision = False
step = 600
screenWidth = 1280
spawner = 0
obstacles=[]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if isGame:
                vY = 500
            else:
                y = 100
                vY = 0
                spawner = 0
                isGame = True
                obstacles = []
    screen.fill("lightgreen")
    # is game or gameover
    if isGame:
        if spawner <= screenWidth-step:
            spawner = screenWidth
            randomY = random.randint(-350,0)
            yDown = randomY+400+250
            obstacles.append([len(obstacles),screenWidth,randomY,yDown])
        else: spawner -= speed*fps
        vY += g*fps
        y -= vY * fps
        for i in range(len(obstacles)):
            obstacles[i][1] -= speed * fps
            if (obstacles[i][1] > 300 and obstacles[i][1] < 360):
                if (obstacles[i][2]+500 > y or y > obstacles[i][3]):
                    collision = True
    else:
        if textBlinkCooldown < 0:
            textBlinkCooldown = textBlink
            isText = not isText
        else: textBlinkCooldown -= fps*1000
        if isText:
            screen.blit(text_surface, (1280/2-gameoverTextWidth,720/2-gameoverTextHeight))

    # obstacles render
    for i in range(len(obstacles)):
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(obstacles[i][1],obstacles[i][2],100,500))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(obstacles[i][1],obstacles[i][3],100,500))

    # does he lose already
    if ((y < 0 or y > 660) and isGame) or collision:
        isGame = False
        isText = True
        textBlinkCooldown = textBlink
        collision = False
    pygame.draw.rect(screen,(0,0,0),pygame.Rect(300,y,60,60))
    pygame.display.flip()

    fps = clock.tick(60)/1000

pygame.quit()