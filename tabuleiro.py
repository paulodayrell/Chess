import pygame, sys
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
tile_length = 128
display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255,0,0))

class Tabuleiro(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.dark_square = pygame.image.load("./sprites/128h/square brown dark_png_128px.png")
        self.light_square = pygame.image.load("./sprites/128h/square brown light_png_128px.png")
        self.surf = pygame.Surface((tile_length, tile_length))
        self.rect = self.surf.get_rect()
        self.position = [(x*tile_length, y*tile_length) for x in range(8) for y in range(8)]

    def update(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < width:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        colour_dict = {True: self.light_square, False: self.dark_square}
        current_colour = True
    
        for i in range(len(self.position)):
            if i%8 != 0: current_colour = not current_colour
            surface.blit(colour_dict[current_colour], self.position[i])
        
tabuleiro = Tabuleiro()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
   
    tabuleiro.draw(display)
    pygame.display.update()
    framesPerSecond.tick(FPS)