import pygame, sys
from tabuleiro import *
from menu import *
from pecas import *
from pygame.locals import *
import time

pygame.init()

FPS = 60
framesPerSecond = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

size = width, height = 1024, 1024
display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255,0,0))

tabuleiro = Tabuleiro(display)
menu = Menu(display, tabuleiro)

menu.loop()

'''
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    menu.draw(display)
    pygame.display.update()
    framesPerSecond.tick(FPS)
'''