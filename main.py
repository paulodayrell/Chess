import sys
import pygame as pg

pg.init()

BOARD_LENGTH = 8
size = width, height = 660, 490
speed = [1.2, 1.2]
black = 0, 0, 0

screen = pg.display.set_mode(size)

tabuleiro = [[None for x in range(BOARD_LENGTH)]for y in range(BOARD_LENGTH)]

while 1:
    draw_squares(screen)
    for event in pg.event.get():
        if event.type == pg.QUIT: sys.exit()
    screen.fill(black)
    pg.display.flip()