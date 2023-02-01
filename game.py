import time
import pygame
import numpy as np

color_background = (0,0,0)
color_grid = (40,40,40)
color_die_next = (170, 170, 170)
color_alive = (255,255,255)

def update(screen, cells, size, progress=False):
    board = np.zeros((cells.shape[0], cells.shape[1]))

    for ( row, col) in np.ndindex(cells.shape):
        neighboursAlive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = color_background if cells[row,col] == 0 else color_alive

        if (progress):
            if (cells[row, col] == 1 ):
                if (neighboursAlive < 2 or neighboursAlive > 3):
                    color = color_die_next
                else:
                    board[row, col] = 1
                    color= color_alive
            else:
                if (neighboursAlive == 3):
                    board[row, col] = 1
                    color = color_alive

        pygame.draw.rect(screen, color, (col* size, row * size, size - 1, size - 1))
    
    return board


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))
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
                    cells = np.zeros((60, 80))
                    update(screen, cells, 10)
                    pygame.display.update()
            
            if (pygame.mouse.get_pressed()[0]):
                pos = pygame.mouse.get_pos()
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