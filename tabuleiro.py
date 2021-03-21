import pygame, sys, pecas
from pygame.locals import *
import time

tile_length = 128

class Tabuleiro(pygame.sprite.Sprite):
    def __init__(self, display):
        super().__init__() 
        self.surface = display
        self.dark_square = pygame.image.load("./sprites/128h/square brown dark.png")
        self.light_square = pygame.image.load("./sprites/128h/square brown light.png")
        self.surf = pygame.Surface((tile_length, tile_length))
        self.rect = self.surf.get_rect()
        self.position = [(x*tile_length, y*tile_length) for x in range(8) for y in range(8)]

        self.player1 = 'white'
        self.player2 = 'black'

    def reseta_tabuleiro(self):
        def gerar_pecas(cor):
            return [pecas.Torre(cor), pecas.Cavalo(cor), pecas.Bispo(cor), pecas.Rainha(cor),
                    pecas.Rei(cor), pecas.Bispo(cor), pecas.Cavalo(cor), pecas.Torre(cor)]

        board = [[None for x in range(8)] for x in range(8)]
    
        board[0] = gerar_pecas("black")
        board[7] = gerar_pecas("white")
        board[1] = [pecas.Peao("black") for square in board[1]]
        board[6] = [pecas.Peao("white") for square in board[6]]

        return board
 
    def draw(self, surface):
        colour_dict = {True: self.light_square, False: self.dark_square}
        current_colour = True
    
        for i in range(len(self.position)):
            if i%8 != 0: current_colour = not current_colour
            surface.blit(colour_dict[current_colour], self.position[i])
        
        pecas_tabuleiro = self.reseta_tabuleiro()

        for i in range(8):
            for j in range(8):
                if pecas_tabuleiro[i][j] is not None:
                    surface.blit(pecas_tabuleiro[i][j].image, self.position[i*8+j])

    def loop(self):
        running = True

        FPS = 60
        framesPerSecond = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 27: # 27 == "ESC"
                        running = False

            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)