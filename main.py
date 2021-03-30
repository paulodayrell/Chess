import pygame, sys
from tabuleiro import *
from menu import *
from Peca import *
from pygame.locals import *
import time
from config import *

pygame.init()
framesPerSecond = pygame.time.Clock()

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255,0,0))

tabuleiro = Tabuleiro(display)
menu = Menu(display, tabuleiro)

menu.loop()

