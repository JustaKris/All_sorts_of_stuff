import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

def drawGrid(w, rows, surface):

    sizeBtwn = w // rows

    x = 0
    y = 0
    for l in range(rows):
        x = x + sizeBtwn
        y = y + sizeBtwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), {x, w})
        pygame.draw.line(surface, (255, 255, 255), (0, y), {w, y})


def redrawWindow(surface):
    global rows, width
    surface.fill((0, 0, 0))
    drawGrid(width, rows, surface)
    pygame.display.update()


# Game
def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode(size=(width, width))  # Don't need height since we are doing a square
    # s = snake((255,0,0), (10,10))
    flag = True

    clock = pygame.time.Clock()

    # Game Loop
    while flag:
        pygame.time.delay(50)
        clock.tick(10)
        redrawWindow(win)



# cube.rows = rows
# cube.w = rows

main()

