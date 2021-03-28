import pygame
import sys
import pecas
from pygame.locals import *
import time
from Player import Player
from config import *

tile_length = 64

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
        self.white_player = Player('white', True)
        self.black_player = Player('black', False)
        
        self.piece_selected = None #guarda a peca atualmente selecionada
        self.possible_moves = [] #guarda os movimentos possiveis da peca atualmente selecionada
        # self.turn = True #true -> white, false -> black

    def change_turn(self):
        self.white_player.passar_turno()
        self.black_player.passar_turno()

    def reseta_tabuleiro(self):
        def gerar_pecas(cor):
            if cor == "black":
                return [pecas.Torre(0, 0, cor, tile_length), pecas.Cavalo(0, 1, cor, tile_length), pecas.Bispo(0, 2, cor, tile_length), pecas.Rainha(0, 3, cor, tile_length),
                        pecas.Rei(0, 4, cor, tile_length), pecas.Bispo(0, 5, cor, tile_length), pecas.Cavalo(0, 6, cor, tile_length), pecas.Torre(0, 7, cor, tile_length)]
            else:
                return [pecas.Torre(7, 0, cor, tile_length), pecas.Cavalo(7, 1, cor, tile_length), pecas.Bispo(7, 2, cor, tile_length), pecas.Rainha(7, 3, cor, tile_length),
                        pecas.Rei(7, 4, cor, tile_length), pecas.Bispo(7, 5, cor, tile_length), pecas.Cavalo(7, 6, cor, tile_length), pecas.Torre(7, 7, cor, tile_length)]

        board = [[None for x in range(8)] for x in range(8)]

        board[0] = gerar_pecas("black")
        board[7] = gerar_pecas("white")
        board[1] = [pecas.Peao(1, index, "black", tile_length)
                    for index, square in enumerate(board[1])]
        board[6] = [pecas.Peao(6, index, "white", tile_length)
                    for index, square in enumerate(board[6])]

        return board

    def get_piece(self, linha, coluna):
        return self.pecas_tabuleiro[linha][coluna]

    def place_piece(self, peca, linha, coluna):
        self.pecas_tabuleiro[linha][coluna] = peca
        peca.linha = linha
        peca.coluna = coluna

    def remove_piece(self, linha, coluna):
        self.pecas_tabuleiro[linha][coluna] = None
        
    #Primeiro clique na peca
    def set_possible_moves(self, linha, coluna):
        self.possible_moves = []
        self.piece_selected = None

        peca = self.get_piece(linha, coluna)

        if peca:

            self.piece_selected = peca
            
            for m in peca.get_movements():
                if self.can_move(peca, m[0], m[1]):
                    self.possible_moves.append(m)

    def can_move(self, peca, to_linha, to_coluna):

        target_place = self.get_piece(to_linha, to_coluna)

        if peca.name == 'king':
            if target_place and target_place.colour == peca.colour:
                return False
        elif peca.name == 'rook':
            if peca.linha != to_linha: #esta se movimentando entre linhas
                for i in range(min(peca.linha, to_linha), max(peca.linha, to_linha)+1):
                    if peca.linha != i and self.get_piece(i, peca.coluna): #Verifica se nao estah na mesma casa da peca
                        if (i, peca.coluna) == (to_linha, to_coluna): #na casa de destino o teste eh mais estrito
                            if target_place.colour == peca.colour:
                                return False
                        else:
                            return False
            elif peca.coluna != to_coluna: #esta se movimentando entre colunas
                for i in range(min(peca.coluna, to_coluna), max(peca.coluna, to_coluna)+1):
                    if peca.coluna != i and self.get_piece(peca.linha, i):
                        if (peca.linha, i) == (to_linha, to_coluna): #na casa de destino o teste eh mais estrito
                            if target_place.colour == peca.colour:
                                return False
                        else:
                            return False
            else:
                return False
        elif peca.name == 'bishop':

            difference_linha = to_linha - peca.linha
            difference_coluna = to_coluna - peca.coluna

            soma_linha = 0
            soma_coluna = 0

            # -+ direita superior
            # -- esquerda superior
            # ++ direita inferior
            # +- esquerda inferior
            if difference_linha < 0:
                soma_linha = -1
            elif difference_linha > 0:
                soma_linha = 1
            else:
                return False
            if difference_coluna < 0:
                soma_coluna = -1
            elif difference_coluna > 0:
                soma_coluna = 1
            else:
                return False

            test_place = [peca.linha, peca.coluna] 

            while (test_place[0], test_place[1]) != (to_linha, to_coluna):
                test_place = [test_place[0]+soma_linha, test_place[1]+soma_coluna]
                if self.get_piece(test_place[0], test_place[1]):
                    if to_linha == test_place[0] and to_coluna == test_place[1]:
                        if target_place and target_place.colour == peca.colour:
                            return False
                    else:
                        return False

        elif peca.name == 'knight':
            
            if target_place and target_place.colour == peca.colour:
                return False

        elif peca.name == 'pawn':

            difference_linha = to_linha - peca.linha
            difference_coluna = to_coluna - peca.coluna

            #Se eh um movimento diagonal
            if (difference_linha < 0 and difference_coluna < 0) or (difference_linha > 0 and difference_coluna > 0) or (difference_linha > 0 and difference_coluna < 0) or (difference_linha < 0 and difference_coluna > 0):
                if target_place: #Testa captura
                    if target_place.colour == peca.colour:
                        return False
                else:
                    return False
            else:
                if peca.colour == "black":
                    if self.get_piece(to_linha, to_coluna):
                        return False
                    if difference_linha > 1:
                        if self.get_piece(peca.linha+1, to_coluna):
                            return False
                else:
                    if self.get_piece(to_linha, to_coluna):
                        return False
                    if difference_linha < -1:
                        if self.get_piece(peca.linha-1, to_coluna):
                            return False

        elif peca.name == 'queen':

            if (peca.linha != to_linha and peca.coluna != to_coluna):
                difference_linha = to_linha - peca.linha
                difference_coluna = to_coluna - peca.coluna

                soma_linha = 0
                soma_coluna = 0

                # -+ direita superior
                # -- esquerda superior
                # ++ direita inferior
                # +- esquerda inferior
                if difference_linha < 0:
                    soma_linha = -1
                elif difference_linha > 0:
                    soma_linha = 1
                else:
                    return False
                if difference_coluna < 0:
                    soma_coluna = -1
                elif difference_coluna > 0:
                    soma_coluna = 1
                else:
                    return False

                test_place = [peca.linha, peca.coluna] 

                while (test_place[0], test_place[1]) != (to_linha, to_coluna):
                    test_place = [test_place[0]+soma_linha, test_place[1]+soma_coluna]
                    if self.get_piece(test_place[0], test_place[1]):
                        if to_linha == test_place[0] and to_coluna == test_place[1]:
                            if target_place and target_place.colour == peca.colour:
                                return False
                        else:
                            return False
            else: #movimento de torre
                if peca.linha != to_linha: #esta se movimentando entre linhas
                    for i in range(min(peca.linha, to_linha), max(peca.linha, to_linha)+1):
                        if peca.linha != i and self.get_piece(i, peca.coluna): #Verifica se nao estah na mesma casa da peca
                            if (i, peca.coluna) == (to_linha, to_coluna): #na casa de destino o teste eh mais estrito
                                if target_place and target_place.colour == peca.colour:
                                    return False
                            else:
                                return False
                elif peca.coluna != to_coluna: #esta se movimentando entre colunas
                    for i in range(min(peca.coluna, to_coluna), max(peca.coluna, to_coluna)+1):
                        if peca.coluna != i and self.get_piece(peca.linha, i):
                            if (peca.linha, i) == (to_linha, to_coluna): #na casa de destino o teste eh mais estrito
                                if target_place and target_place.colour == peca.colour:
                                    return False
                            else:
                                return False
                else:
                    return False

        return True

    def move(self, linha, coluna):
        pos_destino = self.get_piece(linha,coluna)

        self.remove_piece(self.piece_selected.linha, self.piece_selected.coluna)
        self.place_piece(self.piece_selected, linha, coluna)

        if pos_destino:
            if pos_destino.colour == 'white':
                self.white_player.capturar_peca(pos_destino)
            else:
                self.black_player.capturar_peca(pos_destino)
        self.piece_selected.moves +=1
        self.piece_selected.moved = True
        self.change_turn()
        #print(self.get_piece(linha, coluna).name)
        self.piece_selected = None
        self.possible_moves = []
        
    #Recebe uma coordena referente ao clique do usuario na tela e decide a acao a ser tomada
    def validate_click(self, x, y):
        linha, coluna = (y//tile_length), (x//tile_length)

        #Segundo clique
        if self.piece_selected:
            moved = False

            for m in self.possible_moves:
                if (linha, coluna) == (m[0], m[1]):
                    self.move(m[0], m[1])
                    moved = True

            if not moved:
                self.piece_selected = None
                self.possible_moves = []

        #Primeiro clique
        else:
            if self.get_piece(linha, coluna):
                if self.get_piece(linha, coluna).colour == "black" and self.black_player.turn:
                    self.set_possible_moves(linha, coluna)
                elif self.get_piece(linha, coluna).colour == "white" and self.white_player.turn:
                    self.set_possible_moves(linha, coluna)

        print(str(linha), str(coluna))
        #print(self.get_piece(linha, coluna).name)


    def draw(self, surface):
        colour_dict = {True: self.light_square, False: self.dark_square}
        current_colour = True


        for i in range(len(self.position)):
            if i % 8 != 0:
                current_colour = not current_colour
            surface.blit(colour_dict[current_colour], self.position[i])
            for pm in self.possible_moves:
                if((self.position[i][1]//tile_length, self.position[i][0]//tile_length) == (pm[0], pm[1])):
                    pygame.draw.circle(surface, pygame.Color(0,0,0,220), (self.position[i][0]+tile_length/2, self.position[i][1]+tile_length/2), tile_length/4)

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
        self.pecas_tabuleiro = self.reseta_tabuleiro()
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

                        self.validate_click(x,y)



            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)
