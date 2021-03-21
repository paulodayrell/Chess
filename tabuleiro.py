import pygame
import sys
import pecas
from pygame.locals import *
import time

tile_length = 128


class Tabuleiro(pygame.sprite.Sprite):
    def __init__(self, display):
        super().__init__()
        self.surface = display
        self.dark_square = pygame.image.load(
            "./sprites/128h/square brown dark.png")
        self.light_square = pygame.image.load(
            "./sprites/128h/square brown light.png")
        self.surf = pygame.Surface((tile_length, tile_length))
        self.rect = self.surf.get_rect()
        self.position = [(x*tile_length, y*tile_length)
                         for x in range(8) for y in range(8)]
        self.pecas_tabuleiro = []
        self.player1 = 'white'
        self.player2 = 'black'

    def reseta_tabuleiro(self):
        def gerar_pecas(cor):
            if cor == "black":
                return [pecas.Torre(0, 0, cor), pecas.Cavalo(0, 1, cor), pecas.Bispo(0, 2, cor), pecas.Rainha(0, 3, cor),
                        pecas.Rei(0, 4, cor), pecas.Bispo(0, 5, cor), pecas.Cavalo(0, 6, cor), pecas.Torre(0, 7, cor)]
            else:
                return [pecas.Torre(7, 0, cor), pecas.Cavalo(7, 1, cor), pecas.Bispo(7, 2, cor), pecas.Rainha(7, 3, cor),
                        pecas.Rei(7, 4, cor), pecas.Bispo(7, 5, cor), pecas.Cavalo(7, 6, cor), pecas.Torre(7, 7, cor)]

        board = [[None for x in range(8)] for x in range(8)]

        board[0] = gerar_pecas("black")
        board[7] = gerar_pecas("white")
        board[1] = [pecas.Peao(1, index, "black")
                    for index, square in enumerate(board[1])]
        board[6] = [pecas.Peao(6, index, "white")
                    for index, square in enumerate(board[6])]

        return board

    def draw(self, surface):
        colour_dict = {True: self.light_square, False: self.dark_square}
        current_colour = True

        for i in range(len(self.position)):
            if i % 8 != 0:
                current_colour = not current_colour
            surface.blit(colour_dict[current_colour], self.position[i])

        self.pecas_tabuleiro = self.reseta_tabuleiro()

        for i in range(8):
            for j in range(8):
                if self.pecas_tabuleiro[i][j] is not None:
                    surface.blit(
                        self.pecas_tabuleiro[i][j].image, self.position[j*8+i])
                font = pygame.font.SysFont(None, 30)
                img = font.render(str(i) + ', ' + str(j),
                                  True, (255, 255, 255))
                surface.blit(img, self.position[j*8+i])

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
                    if event.key == 27:  # 27 == "ESC"
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos  # sistema de coordenadas
                        linha, coluna = (y//tile_length), (x//tile_length)
                        print(str(linha))
                        print(str(coluna))
                        print()
                        print(self.pecas_tabuleiro[linha][coluna].name)
                        print(self.pecas_tabuleiro[linha]
                              [coluna].get_movements())
                        # for button in self.buttons:
                        #     if(button.buttonX < x and button.buttonX + button.buttonW > x and button.buttonY < y and button.buttonY + button.buttonH > y):
                        #         button.click()

            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)
