import pygame
import random

gameTick = 250
tick = gameTick
windowSize = 600
snakeSize = windowSize/12
snakePos = [snakeSize*6,snakeSize*6]   
direction = 1
dirFuture = False
directionFuture = -1
gameOver = True
# 0 - North
# 1 - East
# 2 - South
# 3 - West
size = [snakePos]
dt = 0
apple = []

pygame.init()
screen = pygame.display.set_mode((windowSize, windowSize))
clock = pygame.time.Clock()
running = True

def NewApple():
    global apple
    apple = [random.randint(0,11)*snakeSize,random.randint(0,11)*snakeSize]
    while apple in size:
        apple = [random.randint(0,11)*snakeSize,random.randint(0,11)*snakeSize]
NewApple()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if gameOver:
                gameOver = False
                NewApple()
                tick = gameTick
                snakePos = [snakeSize*6,snakeSize*6]
                size = [snakePos]
            if dir:
                if event.key == pygame.K_UP and not direction == 2:
                    direction = 0
                    dir = False
                if event.key == pygame.K_RIGHT and not direction == 3: 
                    direction = 1
                    dir = False
                if event.key == pygame.K_DOWN and not direction == 0: 
                    direction = 2
                    dir = False
                if event.key == pygame.K_LEFT and not direction == 1: 
                    direction = 3
                    dir = False
            else:
                if event.key == pygame.K_UP and not direction == 2:
                    directionFuture = 0
                    dirFuture = True
                if event.key == pygame.K_RIGHT and not direction == 3: 
                    directionFuture = 1
                    dirFuture = True
                if event.key == pygame.K_DOWN and not direction == 0: 
                    directionFuture = 2
                    dirFuture = True
                if event.key == pygame.K_LEFT and not direction == 1: 
                    directionFuture = 3
                    dirFuture = True

    screen.fill("black")
    pygame.draw.rect(screen,"red",pygame.Rect(apple[0],apple[1],snakeSize,snakeSize))
    pygame.draw.rect(screen,"green",pygame.Rect(size[0][0]+snakeSize*0.05,size[0][1]+snakeSize*0.05,snakeSize*0.92,snakeSize*0.92))
    pygame.draw.rect(screen,"darkgreen",pygame.Rect(size[0][0]+snakeSize*0.30,size[0][1]+snakeSize*0.5,snakeSize*0.1,snakeSize*0.1))
    pygame.draw.rect(screen,"darkgreen",pygame.Rect(size[0][0]+snakeSize*0.70,size[0][1]+snakeSize*0.5,snakeSize*0.1,snakeSize*0.1))
    for x in size[1::]:
        pygame.draw.rect(screen,"green",pygame.Rect(x[0]+snakeSize*0.1,x[1]+snakeSize*0.1,snakeSize*0.2,snakeSize*0.2))
    
    if tick < 0:
        if dirFuture and dir:
            dirFuture = False
            direction = directionFuture
        dir = True
        if direction == 0:
            snakePos[1] -= snakeSize
        if direction == 1:
            snakePos[0] += snakeSize
        if direction == 2:
            snakePos[1] += snakeSize
        if direction == 3:
            snakePos[0] -= snakeSize
        tick = gameTick
        if (snakePos[0] < 0 or snakePos[0] >= windowSize or snakePos[1] < 0 or snakePos[1] >= windowSize) or (snakePos in size[1::]):
            gameOver = True
            tick = gameTick
        if apple == snakePos:
            NewApple()
        else:
            size.remove(size[len(size)-1])
        size.insert(0,[snakePos[0],snakePos[1]])
    elif not gameOver:
        tick -= dt

    pygame.display.flip()

    dt = clock.tick(60)

pygame.quit()
