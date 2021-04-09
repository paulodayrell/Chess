import pygame
import sys
from pygame.locals import *
import time
from config import *
from Peca import *

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

        self.get_out_of_check_moves = []
        self.current_player_check = False
        self.pecas_tabuleiro = []
        self.pecas_capturadas = []
        self.jogador_atual = 'white'
        self.turnos = 0
        self.piece_selected = None #guarda a peca atualmente selecionada
        self.possible_moves = [] #guarda os movimentos possiveis da peca atualmente selecionada

    def troca_turno(self):
        self.jogador_atual = 'black' if self.jogador_atual =='white' else 'white'
        self.turnos += 1

        self.get_out_of_check_moves = []

        if self.is_in_check():
            self.current_player_check = True
            print("Check mate", self.check_mate())
            print("get_out_of_check_moves", self.get_out_of_check_moves)
        else:
            self.current_player_check = False
    
    def clear_board(self):
        self.pecas_tabuleiro = [[None for x in range(8)] for x in range(8)]

    def reseta_tabuleiro(self):
        def gerar_pecas(cor):
            if cor == "black":
                return [Torre(0, 0, cor, tile_length), Cavalo(0, 1, cor, tile_length), Bispo(0, 2, cor, tile_length), Rainha(0, 3, cor, tile_length),
                        Rei(0, 4, cor, tile_length), Bispo(0, 5, cor, tile_length), Cavalo(0, 6, cor, tile_length), Torre(0, 7, cor, tile_length)]
            else:
                return [Torre(7, 0, cor, tile_length), Cavalo(7, 1, cor, tile_length), Bispo(7, 2, cor, tile_length), Rainha(7, 3, cor, tile_length),
                        Rei(7, 4, cor, tile_length), Bispo(7, 5, cor, tile_length), Cavalo(7, 6, cor, tile_length), Torre(7, 7, cor, tile_length)]

        board = [[None for x in range(8)] for x in range(8)]

        board[0] = gerar_pecas("black")
        board[7] = gerar_pecas("white")
        board[1] = [Peao(1, index, "black", tile_length)
                    for index, square in enumerate(board[1])]
        board[6] = [Peao(6, index, "white", tile_length)
                    for index, square in enumerate(board[6])]

        return board

    def capturar_peca(self, peca):
        self.pecas_capturadas.append(peca)

    def get_piece(self, linha, coluna):
        return self.pecas_tabuleiro[linha][coluna]

    def place_piece(self, peca, linha, coluna):
        self.pecas_tabuleiro[linha][coluna] = peca
        peca.linha = linha
        peca.coluna = coluna

    def remove_piece(self, linha, coluna):
        self.pecas_tabuleiro[linha][coluna] = None

    def posicao_valida(self, linha, coluna):
        if linha >= 0 and linha < 8 and coluna >= 0 and coluna < 8:
            return True
        return False

    def pode_mover(self, peca, linha, coluna):
        if not self.posicao_valida(linha, coluna): return False
        pos_destino = self.get_piece(linha, coluna)
        return not pos_destino or pos_destino.colour!=peca.colour
    
    def move(self, linha, coluna):
        self.remove_piece(self.piece_selected.linha, self.piece_selected.coluna)
        self.piece_selected.moves +=1

        pos_destino = self.get_piece(linha,coluna)
        if pos_destino:
            self.capturar_peca(pos_destino)

        self.place_piece(self.piece_selected, linha, coluna)

        self.troca_turno()
        self.piece_selected = None
        self.possible_moves = []

    #Recebe uma coordena referente ao clique do usuario na tela e decide a acao a ser tomada
    def validate_click(self, x, y):
        linha, coluna = (y//tile_length), (x//tile_length)

        #Se eu já tiver uma peça selecionada, preciso mover ela
        if self.piece_selected:
            if [linha, coluna] in self.possible_moves:
                peca_capturada = self.move(linha, coluna)
                self.piece_selected = None
        #Caso eu não tenha uma peça selecionada ou eu não tenha clicado em um movimento possivel, vou trocar de pedra
        peca_origem = self.get_piece(linha, coluna)
        if peca_origem:
            if peca_origem.colour == self.jogador_atual:
                self.piece_selected = peca_origem
                self.possible_moves = []

                if self.current_player_check:
                    for move in self.piece_selected.get_movements(self):
                        for get_out_move in self.get_out_of_check_moves:
                            if (get_out_move[0].linha, get_out_move[0].coluna) == (self.piece_selected.linha, self.piece_selected.coluna):
                                if (move[0], move[1]) == (get_out_move[1], get_out_move[2]): #se ele eh um movimento que tira a peca de xeque
                                    self.possible_moves.append(move)
                else:
                    for move in self.piece_selected.get_movements(self):
                        if self.get_out_of_check(self.piece_selected, move[0], move[1]):
                            self.possible_moves.append(move)            

    def get_all_movements(self, player):
        movements = set()

        for linha in range(8):
            for coluna in range(8):
                peca = self.get_piece(linha,coluna)

                if peca and peca.colour == player:
                    posicoes = peca.get_movements(self)

                    for posicao in posicoes:
                        movements.add(tuple(posicao))

        return movements

    def is_in_check(self):

        opponent = "black" if self.jogador_atual == "white" else "white"

        movements = self.get_all_movements(opponent)

        rei = None

        for linha in range(8):
            for coluna in range(8):
                peca = self.get_piece(linha,coluna)

                if peca and peca.name == "king" and peca.colour == self.jogador_atual:
                    rei = peca

        return (rei.linha, rei.coluna) in movements

    def get_out_of_check(self, peca, to_linha, to_coluna):
        from_linha = peca.linha
        from_coluna = peca.coluna

        #faz um movimento fake
        peca.moves += 1
        self.remove_piece(peca.linha, peca.coluna)
        peca_destino = self.get_piece(to_linha, to_coluna)
        self.place_piece(peca, to_linha, to_coluna)

        #is_in_check
        is_in_check = self.is_in_check()

        #desfaz movimento fake
        peca.moves -= 1
        self.remove_piece(peca.linha, peca.coluna)
        self.place_piece(peca, from_linha, from_coluna)
        if peca_destino:
            self.place_piece(peca_destino, to_linha, to_coluna)

        return not is_in_check

    def check_mate(self):

        for linha in range(8):
            for coluna in range(8):
                peca = self.get_piece(linha,coluna)

                if peca and peca.colour == self.jogador_atual:
                    posicoes = peca.get_movements(self)

                    for posicao in posicoes:
                        if self.get_out_of_check(peca, posicao[0], posicao[1]):
                            self.get_out_of_check_moves.append((peca, posicao[0], posicao[1]))

        if len(self.get_out_of_check_moves) == 0: #nao existem movimentos que tirem o jogador de xeque
            return True

        return False

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
