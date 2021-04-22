import pygame
import sys
from pygame.locals import *
import time
from config import *
from Peca import *
from minimax import *
from move import Move
from final_screen import *
from pawn_promotion_screen import *

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
        self.pecas_capturadas_anterior = []
        self.pecas_capturadas = []
        self.jogador_atual = 'white'
        self.turnos = 0
        self.piece_selected = None  # guarda a peca atualmente selecionada
        # guarda os movimentos possiveis da peca atualmente selecionada
        self.possible_moves = []
        # self.turn = True #true -> white, false -> black

        self.black_score = 1290
        self.white_score = 1290
        self.weights = {Rei: 900, Rainha: 90, Torre: 50, Bispo: 30, Cavalo: 30, Peao: 10}
        self.fifty_moves = 0
        self.moves = []
        self.screen_mode = "playing"

    def reset(self):
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
        self.pecas_capturadas_anterior = []
        self.pecas_capturadas = []
        self.jogador_atual = 'white'
        self.turnos = 0
        self.fifty_moves = 0
        self.piece_selected = None #guarda a peca atualmente selecionada
        self.possible_moves = [] #guarda os movimentos possiveis da peca atualmente selecionada
        self.screen_mode = "playing"

    def troca_turno(self):
        self.jogador_atual = 'black' if self.jogador_atual == 'white' else 'white'
        self.turnos += 1

        if (len(self.pecas_capturadas_anterior) != len(self.pecas_capturadas)):
            self.fifty_moves = 0

        self.fifty_moves += 1

        self.pecas_capturadas_anterior = self.pecas_capturadas.copy()

        self.get_out_of_check_moves = []

        if self.fifty_moves >= 50:
            self.screen_mode = "draw_fifty_moves"

        if self.dead_position():
            self.screen_mode = "draw_dead_position"

        if self.is_in_check():
            self.current_player_check = True
            is_in_check_mate = self.check_mate()

            if is_in_check_mate:
                self.screen_mode = "final_screen"

        else:
            self.current_player_check = False

            if self.stalemate():
                self.screen_mode = "draw_stalemate"
                    
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

        self.jogador_atual = 'white'

        return board

    def capturar_peca(self, peca):
        if peca.colour == 'black':
            self.black_score -= self.weights[type(peca)]
        else:
            self.white_score -= self.weights[type(peca)]
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
        if not self.posicao_valida(linha, coluna):
            return False
        pos_destino = self.get_piece(linha, coluna)
        return not pos_destino or pos_destino.colour != peca.colour

    def copy(self):
        copy = Tabuleiro(self.surface)
        copy.position = self.position
        copy.pecas_tabuleiro = []

        for i in range(8):
            aux = []
            for j in range(8):
                p = self.pecas_tabuleiro[i][j]
                if p:
                    aux.append(p.copy())
                else:
                    aux.append(None)
            copy.pecas_tabuleiro.append(aux)

        copy.pecas_capturadas = []

        copy.pecas_capturadas = [p.copy() for p in self.pecas_capturadas]

        copy.jogador_atual = self.jogador_atual
        copy.turnos = self.turnos
        copy.piece_selected = self.piece_selected
        # copy.possible_moves = self.possible_moves
        copy.possible_moves = [p.copy() for p in self.possible_moves]

        copy.black_score = self.black_score
        copy.white_score = self.white_score
        copy.weights = self.weights

        return copy
    
    def get_piece_out_of_check_moves(self, piece):
        for movement in piece.get_movements(self):
            for get_out_of_check_move in self.get_out_of_check_moves:
                x_out_of_check, y_out_of_check = get_out_of_check_move[1], get_out_of_check_move[2]
                if self.move_gets_piece_out_of_check(piece, x_out_of_check, y_out_of_check):
                    x_move, y_move = movement
                    if(x_move, y_move) == (x_out_of_check, y_out_of_check):
                        return Move([piece.linha, piece.coluna], movement, None)
        
    
    def get_moves(self):
        moves = []
        for x in range(8):
            for y in range(8):
                piece = self.pecas_tabuleiro[x][y]
                if piece and piece.colour == self.jogador_atual:
                    if self.current_player_check and self.get_piece_out_of_check_moves(piece):
                        moves.append(self.get_out_of_check_moves_ai(piece))
                    elif self.get_regular_move(piece):
                        moves.append(self.get_regular_move(piece))
        return moves
    
    def get_regular_move(self, piece):
        for movement in piece.get_movements(self):
            if self.get_out_of_check(piece, movement[0], movement[1]):
                return Move([piece.linha, piece.coluna], movement, None)        

    def move_gets_piece_out_of_check(self, piece, x, y):
        return (x,y) == (piece.linha, piece.coluna)

    def make_move(self, move):
        self.move_ai(move, move.from_coord, move.to_coord)

    def undo_move(self, move):
        self.move_ai(move, move.to_coord, move.from_coord)
        self.uncapture(move.captured)

    def move_ai(self, move, from_coord, to_coord):

        x_to, y_to = to_coord
        x_from, y_from = from_coord

        piece = self.get_piece(x_from, y_from)
        if not piece:
            return
        self.remove_piece(piece.linha, piece.coluna)
        piece.moves += 1

        pos_destino = self.get_piece(x_to, y_to)
        if pos_destino:
            self.capturar_peca(pos_destino)
            move.captured = pos_destino

        self.place_piece(piece, x_to, y_to)

        self.possible_moves = []

    def uncapture(self, piece):
        if not piece:
            return
        if piece.colour == 'black':
            self.black_score += self.weights[type(piece)]
        else:
            self.white_score += self.weights[type(piece)]
        self.pecas_capturadas.remove(piece)
        self.place_piece(piece, piece.linha, piece.coluna)

    def promocao_peao(self):
        piece_name = PawnPromotionScreen(self.surface, self, self.piece_selected).loop()
        
        if piece_name == "queen":
            return Rainha(self.piece_selected.linha, self.piece_selected.coluna, self.piece_selected.colour, tile_length, self.piece_selected.moves)
        elif piece_name == "rook":
            return Torre(self.piece_selected.linha, self.piece_selected.coluna, self.piece_selected.colour, tile_length, self.piece_selected.moves)
        elif piece_name == "bishop":
            return Bispo(self.piece_selected.linha, self.piece_selected.coluna, self.piece_selected.colour, tile_length, self.piece_selected.moves)
        elif piece_name == "knight":
            return Cavalo(self.piece_selected.linha, self.piece_selected.coluna, self.piece_selected.colour, tile_length, self.piece_selected.moves)          

    def move(self, linha, coluna):
        self.remove_piece(self.piece_selected.linha,
                          self.piece_selected.coluna)
        self.piece_selected.moves += 1

        pos_destino = self.get_piece(linha, coluna)
        if pos_destino:
            self.capturar_peca(pos_destino)

        # jogadaespecial roque
        if self.piece_selected.name == "king" and coluna == (self.piece_selected.coluna + 2):
            torre = self.get_piece(linha, self.piece_selected.coluna + 3)
            self.remove_piece(linha, self.piece_selected.coluna + 3)
            self.place_piece(torre, linha, self.piece_selected.coluna + 1)
            torre.moves += 1
        if self.piece_selected.name == "king" and coluna == (self.piece_selected.coluna - 2):
            torre = self.get_piece(linha, self.piece_selected.coluna - 4)
            self.remove_piece(linha, self.piece_selected.coluna - 4)
            self.place_piece(torre, linha, self.piece_selected.coluna - 1)
            torre.moves += 1

        # # jogadaespecial promocao de peao
        if self.piece_selected.name == "pawn":
            if (self.piece_selected.colour == "white" and linha == 0) or (self.piece_selected.colour == "black" and linha == 7):
                self.piece_selected = self.promocao_peao()

        self.place_piece(self.piece_selected, linha, coluna)
        self.troca_turno()
        self.piece_selected = None
        self.possible_moves = []

    # Recebe uma coordena referente ao clique do usuario na tela e decide a acao a ser tomada
    def validate_click(self, x, y):
        linha, coluna = (y//tile_length), (x//tile_length)

        # Se eu já tiver uma peça selecionada, preciso mover ela
        if self.piece_selected:
            if [linha, coluna] in self.possible_moves:
                if (self.piece_selected.name == 'pawn'):
                    self.fifty_moves = 0
                self.move(linha, coluna)
                self.piece_selected = None
        # Caso eu não tenha uma peça selecionada ou eu não tenha clicado em um movimento possivel, vou trocar de pedra
        peca_origem = self.get_piece(linha, coluna)
        if peca_origem:
            if peca_origem.colour == self.jogador_atual:
                self.piece_selected = peca_origem
                self.possible_moves = []

                if self.current_player_check:
                    for move in self.piece_selected.get_movements(self):
                        for get_out_move in self.get_out_of_check_moves:
                            if (get_out_move[0].linha, get_out_move[0].coluna) == (self.piece_selected.linha, self.piece_selected.coluna):
                                # se ele eh um movimento que tira a peca de xeque
                                if (move[0], move[1]) == (get_out_move[1], get_out_move[2]):
                                    self.possible_moves.append(move)
                else:
                    for move in self.piece_selected.get_movements(self):
                        if self.get_out_of_check(self.piece_selected, move[0], move[1]):
                            self.possible_moves.append(move)

    def get_all_movements(self, player):
        movements = set()

        for linha in range(8):
            for coluna in range(8):
                peca = self.get_piece(linha, coluna)

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
                peca = self.get_piece(linha, coluna)
                if peca and peca.name == "king" and peca.colour == self.jogador_atual:
                    rei = peca

        return (rei.linha, rei.coluna) in movements

    def get_out_of_check(self, peca, to_linha, to_coluna):
        from_linha = peca.linha
        from_coluna = peca.coluna

        # faz um movimento fake
        peca.moves += 1
        self.remove_piece(peca.linha, peca.coluna)
        peca_destino = self.get_piece(to_linha, to_coluna)
        self.place_piece(peca, to_linha, to_coluna)

        # is_in_check
        is_in_check = self.is_in_check()

        # desfaz movimento fake
        peca.moves -= 1
        self.remove_piece(peca.linha, peca.coluna)
        self.place_piece(peca, from_linha, from_coluna)
        if peca_destino:
            self.place_piece(peca_destino, to_linha, to_coluna)

        return not is_in_check

    def check_mate(self):

        for linha in range(8):
            for coluna in range(8):
                peca = self.get_piece(linha, coluna)

                if peca and peca.colour == self.jogador_atual:
                    posicoes = peca.get_movements(self)

                    for posicao in posicoes:
                        if self.get_out_of_check(peca, posicao[0], posicao[1]):
                            self.get_out_of_check_moves.append(
                                (peca, posicao[0], posicao[1]))

        # nao existem movimentos que tirem o jogador de xeque
        if len(self.get_out_of_check_moves) == 0:
            return True

        return False

    def dead_position(self):

        pecas_brancas = {'rook':2, 'knight':2, 'bishop':2, 'queen':1, 'king':1, 'pawn':8}
        pecas_pretas = {'rook':2, 'knight':2, 'bishop':2, 'queen':1, 'king':1, 'pawn':8}
        black_draw = False
        white_draw = False

        for peca in self.pecas_capturadas:
            if(peca.colour == 'white'):
                pecas_brancas[peca.name] -= 1
            else:
                pecas_pretas[peca.name] -= 1

        lone_king_white = True
        king_bishop_white = True
        king_knight_white = True

        if pecas_brancas['bishop'] != 1:
            king_bishop_white = False

        if pecas_brancas['knight'] != 1:
            king_knight_white = False

        for peca in pecas_brancas:
            if(peca != 'king' and pecas_brancas[peca] != 0):
                lone_king_white = False
        
                if(peca != 'bishop'):
                    king_bishop_white = False
                    
                if(peca != 'knight'):
                    king_knight_white = False

        lone_king_black = True
        king_bishop_black = True
        king_knight_black = True

        if pecas_pretas['bishop'] != 1:
            king_bishop_black = False

        if pecas_pretas['knight'] != 1:
            king_knight_black = False

        for peca in pecas_pretas:
            if(peca != 'king' and pecas_pretas[peca] != 0):
                lone_king_black = False

                if(peca != 'bishop'):
                    king_bishop_black = False
                    
                if(peca != 'knight'):
                    king_knight_black = False

        if lone_king_white or king_bishop_white or king_knight_white:
            white_draw = True

        if lone_king_black or king_bishop_black or king_knight_black:
            black_draw = True

        return black_draw and white_draw
        
    def stalemate(self):
        # Se a funcao check_mate retorna true quando o jogador nao estah em xeque um stalemate aconteceu
        if self.check_mate():
            return True
        else:
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
                    pygame.draw.circle(surface, pygame.Color(
                        20, 20, 20), (self.position[i][0]+tile_length/2, self.position[i][1]+tile_length/2), tile_length/4)

        for i in range(8):
            for j in range(8):
                if self.pecas_tabuleiro[i][j] is not None:
                    surface.blit(
                        self.pecas_tabuleiro[i][j].image, self.position[j*8+i])
                font = pygame.font.SysFont(None, 30)
                img = font.render(str(i) + ', ' + str(j),
                                  True, (255, 255, 255))
                surface.blit(img, self.position[j*8+i])

    def loop(self, multiplayer):
        framesPerSecond = pygame.time.Clock()
        self.pecas_tabuleiro = self.reseta_tabuleiro()

        while self.screen_mode == "playing":

            if not multiplayer and self.jogador_atual == 'black':
                aux_board = self.copy()
                mv = minimax(aux_board, 2, float('-inf'),
                             float('inf'), True, 'black')

                piece = self.get_piece(mv[0].from_coord[0], mv[0].from_coord[0])
                if piece and piece.name == 'pawn':
                    self.fifty_moves = 0

                self.make_move(mv[0])
                self.troca_turno()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 27:  # 27 == "ESC"
                        self.screen_mode = "menu"
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos  # sistema de coordenadas

                        self.validate_click(x, y)

            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)

        self.get_final_screen()

        self.screen_mode = "playing"


    def get_final_screen(self):
        if self.screen_mode == "final_screen":
            FinalScreen(self.surface, self.jogador_atual, win = True).loop()
        elif self.screen_mode == "draw_dead_position":
            FinalScreen(self.surface, self.jogador_atual, win = False, draw_type = "Dead Position").loop()
        elif self.screen_mode == "draw_fifty_moves":
            FinalScreen(self.surface, self.jogador_atual, win = False, draw_type = "50 Movimentos").loop()
        elif self.screen_mode == "draw_stalemate":
            FinalScreen(self.surface, self.jogador_atual, win = False, draw_type = "Afogamento").loop()

        self.screen_mode = "playing"
