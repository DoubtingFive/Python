import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()
running = True
board = [0,0,0,0,0,0,0,0,0]
turn = 1
colors = [(100, 0, 200),(64, 0, 128),(255, 75, 75),(100, 100, 255),(255,128,0)] # 0fill 1lines 2X 3O 4winnertext
gameOver = False

while running:
    for event in pygame.event.get():
        if not gameOver:
            if event.type == pygame.MOUSEBUTTONDOWN:
                counter = 0
                row = 0
                for x in board:
                    counter += 1
                    x1 = 200 * counter - 5
                    y1 = 195 + (200*(row))
                    x2 = 200 * (counter - 1) +5
                    y2 = 200 * row
                    if counter >= 3:
                        counter = 0
                        row += 1
                    if event.pos[0] <= x1 and event.pos[1] <= y1 and event.pos[0] >= x2 and event.pos[1] >= y2 and x == 0:
                        board[(counter + row*3)-1] = turn
                        turn *= -1
                _counter = 0
                for x in range(9):
                    if board[x] != 0:
                        _counter += 1
                    if _counter >= 9:
                        print("tie")
                        gameOver = True
                        winner = "Tie"
                for y in range(3):
                    for x in range(3):
                        if board[y * 3] + board[1 + y * 3] + board[2 + y * 3] == 3:
                            print("X wins")
                            gameOver = True
                            winner = "X"
                        elif board[y * 3] + board[1 + y * 3] + board[2 + y * 3] == -3:
                            print("O wins")
                            gameOver = True
                            winner = "O"
                        if board[x] + board[x+3] + board[x+6] == 3:
                            print("X wins")
                            gameOver = True
                            winner = "X"
                        elif board[x] + board[x+3] + board[x+6] == -3:
                            print("O wins")
                            gameOver = True
                            winner = "O"
                        if board[0] + board[4] + board[8] == 3:
                            print("X wins")
                            gameOver = True
                            winner = "X"
                        elif board[0] + board[4] + board[8] == -3:
                            print("O wins")
                            gameOver = True
                            winner = "O"
                        if board[2] + board[4] + board[6] == 3:
                            print("X wins")
                            gameOver = True
                            winner = "X"
                        elif board[2] + board[4] + board[6] == -3:
                            print("O wins")
                            gameOver = True
                            winner = "O"
        if event.type == pygame.QUIT:
            running = False
    screen.fill(colors[0])
    if not gameOver:
        pygame.draw.line(screen, colors[1], (195, 0), (195,600),10)
        pygame.draw.line(screen, colors[1], (395, 0), (395,600),10)
        pygame.draw.line(screen, colors[1], (0, 195), (600,195),10)
        pygame.draw.line(screen, colors[1], (0, 395), (600,395),10)
        counter = 0
        row = 0
        for x in board:
            if x == 1:
                x1 = 50 + (200*counter)
                y1 = 145 + (200*row)
                x2 = 145 + (200*counter)
                y2 = 50 + (200*row)
                pygame.draw.line(screen, colors[2], (x1, y1), (x2,y2),10)
                pygame.draw.line(screen, colors[2], (x2, y1), (x1,y2),10)
            if x == -1:
                xC = 100 + (200*counter)
                yC = 100 + (200*row)
                pygame.draw.circle(screen, colors[3], (xC, yC), 50,5)
            counter += 1
            if counter >= 3:
                counter = 0
                row += 1
    else:
        font = pygame.font.Font(None, 80)
        if not winner == "Tie":
            text = font.render(f"{winner} wins!", True, colors[4])
        else:
            text = font.render(f"Tie!", True, colors[4])
        text_rect = text.get_rect(center=(300,300))
        screen.blit(text, text_rect)
        pygame.display.flip()
        running = False
    pygame.display.flip()
    clock.tick(60) / 1000

sleep(8)
pygame.quit()