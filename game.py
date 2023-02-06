import time
import pygame
import numpy as np

color_background = (0, 0, 0)
color_grid = (40, 40, 40)
color_dying = (170, 170, 170)
color_alive = (255, 255, 255)
size = (80, 80)

def game_logic(board, posX, posY, neighboursAlive):
    if (board[posX, posY] == 1 ):
        if (neighboursAlive < 2 or neighboursAlive > 3):
            return [0, color_dying]
        else:
            return [1, color_alive]
    else:
        if (neighboursAlive == 3):
            return [1, color_alive]
                    

def update(screen, board, size, progress=False):
    board_new = np.zeros((board.shape[0], board.shape[1]))

    for (row, col) in np.ndindex(board.shape):
        neighboursAlive = np.sum(board[row - 1 : row + 2, col - 1 : col + 2]) - board[row, col]
        color = color_background if board[row,col] == 0 else color_alive

        if (progress):
            result = game_logic(board, row, col, neighboursAlive)
            if (result):
                board_new[row, col], color = result

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))
    
    return board_new


def main():
    pygame.init()
    screen = pygame.display.set_mode((size[0] * 10, size[1] * 10))

    cells = np.zeros(size)
    screen.fill(color_grid)
    update(screen, cells, 10)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
                if(event.key == pygame.K_BACKSPACE):
                    cells = np.zeros(size)
                    update(screen, cells, 10)
                    pygame.display.update()
            
            if (pygame.mouse.get_pressed()[0]):
                pos = pygame.mouse.get_pos()
                print(pos)
                if (pos[0] > 0 and pos[0] < 800):
                    if (pos[1] > 0 and pos[1] < 800):
                        cells[pos[1] // 10, pos[0] // 10] = 1
                        update(screen, cells, 10)
                        pygame.display.update()

        screen.fill(color_grid)

        if (running):
            cells = update(screen, cells, 10, progress=True)
            pygame.display.update()

        time.sleep(0.0001)

if (__name__ == "__main__"):
    main()