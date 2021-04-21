from Peca import *
from tabuleiro import *
from config import *
from util import *
import pygame

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255,0,0))

class TestDraw:
    def test_fifty_moves_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        board.pecas_tabuleiro[1] = [None for x in range(8)] # Retirando os peoes
        board.pecas_tabuleiro[6] = [None for x in range(8)] # Retirando os peoes

        for i in range(50):
            if i % 4 == 0:
                coords_first_click = (7, 4)
                coords_second_click = (6, 4)
                board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
                board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

            if i % 4 == 1:
                coords_first_click = (0, 4)
                coords_second_click = (1, 4)
                board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
                board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

            if i % 4 == 2:
                coords_first_click = (6, 4)
                coords_second_click = (7, 4)
                board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
                board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

            if i % 4 == 3:
                coords_first_click = (1, 4)
                coords_second_click = (0, 4)
                board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
                board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        assert board.screen_mode == "draw_fifty_moves"

    def test_dead_position_king_x_king(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        for i in range(len(board.pecas_tabuleiro[1])): # Para cada peao preto
            pawn = board.pecas_tabuleiro[1][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[1][i] = None
        
        for i in range(len(board.pecas_tabuleiro[6])): # Para cada peao branco
            pawn = board.pecas_tabuleiro[6][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[6][i] = None

        board.pecas_capturadas.append(board.pecas_tabuleiro[0][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][7])
        board.pecas_tabuleiro[0][0] = None # Retirando torre preta
        board.pecas_tabuleiro[0][1] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][2] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][3] = None # Retirando rainha preta
        board.pecas_tabuleiro[0][5] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][6] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][7] = None # Retirando torre preta

        board.pecas_capturadas.append(board.pecas_tabuleiro[7][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][7])
        board.pecas_tabuleiro[7][0] = None # Retirando torre branca
        board.pecas_tabuleiro[7][1] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][2] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][3] = None # Retirando rainha branca
        board.pecas_tabuleiro[7][5] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][6] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][7] = None # Retirando torre branca

        assert board.dead_position()

    def test_dead_position_king_bishop_x_king_bishop(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        for i in range(len(board.pecas_tabuleiro[1])): # Para cada peao preto
            pawn = board.pecas_tabuleiro[1][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[1][i] = None
        
        for i in range(len(board.pecas_tabuleiro[6])): # Para cada peao branco
            pawn = board.pecas_tabuleiro[6][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[6][i] = None

        board.pecas_capturadas.append(board.pecas_tabuleiro[0][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][7])
        board.pecas_tabuleiro[0][0] = None # Retirando torre preta
        board.pecas_tabuleiro[0][2] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][3] = None # Retirando rainha preta
        board.pecas_tabuleiro[0][5] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][6] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][7] = None # Retirando torre preta

        board.pecas_capturadas.append(board.pecas_tabuleiro[7][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][7])
        board.pecas_tabuleiro[7][0] = None # Retirando torre branca
        board.pecas_tabuleiro[7][2] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][3] = None # Retirando rainha branca
        board.pecas_tabuleiro[7][5] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][6] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][7] = None # Retirando torre branca

        assert board.dead_position()

    def test_dead_position_king_knight_x_king_knight(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        for i in range(len(board.pecas_tabuleiro[1])): # Para cada peao preto
            pawn = board.pecas_tabuleiro[1][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[1][i] = None
        
        for i in range(len(board.pecas_tabuleiro[6])): # Para cada peao branco
            pawn = board.pecas_tabuleiro[6][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[6][i] = None

        board.pecas_capturadas.append(board.pecas_tabuleiro[0][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][7])
        board.pecas_tabuleiro[0][0] = None # Retirando torre preta
        board.pecas_tabuleiro[0][1] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][3] = None # Retirando rainha preta
        board.pecas_tabuleiro[0][5] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][6] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][7] = None # Retirando torre preta

        board.pecas_capturadas.append(board.pecas_tabuleiro[7][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][7])
        board.pecas_tabuleiro[7][0] = None # Retirando torre branca
        board.pecas_tabuleiro[7][1] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][3] = None # Retirando rainha branca
        board.pecas_tabuleiro[7][5] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][6] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][7] = None # Retirando torre branca

        assert board.dead_position()

    def test_dead_position_king_x_king_bishop(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        for i in range(len(board.pecas_tabuleiro[1])): # Para cada peao preto
            pawn = board.pecas_tabuleiro[1][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[1][i] = None
        
        for i in range(len(board.pecas_tabuleiro[6])): # Para cada peao branco
            pawn = board.pecas_tabuleiro[6][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[6][i] = None

        board.pecas_capturadas.append(board.pecas_tabuleiro[0][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][7])
        board.pecas_tabuleiro[0][0] = None # Retirando torre preta
        board.pecas_tabuleiro[0][1] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][2] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][3] = None # Retirando rainha preta
        board.pecas_tabuleiro[0][5] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][6] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][7] = None # Retirando torre preta

        board.pecas_capturadas.append(board.pecas_tabuleiro[7][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][7])
        board.pecas_tabuleiro[7][0] = None # Retirando torre branca
        board.pecas_tabuleiro[7][1] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][3] = None # Retirando rainha branca
        board.pecas_tabuleiro[7][5] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][6] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][7] = None # Retirando torre branca

        assert board.dead_position()

    def test_dead_position_king_x_king_knight(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        for i in range(len(board.pecas_tabuleiro[1])): # Para cada peao preto
            pawn = board.pecas_tabuleiro[1][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[1][i] = None
        
        for i in range(len(board.pecas_tabuleiro[6])): # Para cada peao branco
            pawn = board.pecas_tabuleiro[6][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[6][i] = None

        board.pecas_capturadas.append(board.pecas_tabuleiro[0][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][7])
        board.pecas_tabuleiro[0][0] = None # Retirando torre preta
        board.pecas_tabuleiro[0][1] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][2] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][3] = None # Retirando rainha preta
        board.pecas_tabuleiro[0][5] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][6] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][7] = None # Retirando torre preta

        board.pecas_capturadas.append(board.pecas_tabuleiro[7][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][7])
        board.pecas_tabuleiro[7][0] = None # Retirando torre branca
        board.pecas_tabuleiro[7][2] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][3] = None # Retirando rainha branca
        board.pecas_tabuleiro[7][5] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][6] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][7] = None # Retirando torre branca

        assert board.dead_position()

    def test_dead_position_king_bishop_x_king_knight(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro() # Adicionando pecas default ao tabuleiro
        for i in range(len(board.pecas_tabuleiro[1])): # Para cada peao preto
            pawn = board.pecas_tabuleiro[1][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[1][i] = None
        
        for i in range(len(board.pecas_tabuleiro[6])): # Para cada peao branco
            pawn = board.pecas_tabuleiro[6][i]
            board.pecas_capturadas.append(pawn)
            board.pecas_tabuleiro[6][i] = None

        board.pecas_capturadas.append(board.pecas_tabuleiro[0][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][1])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[0][7])
        board.pecas_tabuleiro[0][0] = None # Retirando torre preta
        board.pecas_tabuleiro[0][1] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][3] = None # Retirando rainha preta
        board.pecas_tabuleiro[0][5] = None # Retirando bispo preto
        board.pecas_tabuleiro[0][6] = None # Retirando cavalo preto 
        board.pecas_tabuleiro[0][7] = None # Retirando torre preta

        board.pecas_capturadas.append(board.pecas_tabuleiro[7][0])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][2])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][3])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][5])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][6])
        board.pecas_capturadas.append(board.pecas_tabuleiro[7][7])
        board.pecas_tabuleiro[7][0] = None # Retirando torre branca
        board.pecas_tabuleiro[7][2] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][3] = None # Retirando rainha branca
        board.pecas_tabuleiro[7][5] = None # Retirando bispo branco
        board.pecas_tabuleiro[7][6] = None # Retirando cavalo branco 
        board.pecas_tabuleiro[7][7] = None # Retirando torre branca

        assert board.dead_position()

    def test_stalemate_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "black"
        board.pecas_tabuleiro[0][4] = Rei(0, 4, "black", tile_length, moves=0)
        board.pecas_tabuleiro[1][4] = Peao(1, 4, "white", tile_length)
        board.pecas_tabuleiro[2][4] = Rei(2, 4, "white", tile_length, moves=1)
        
        assert board.stalemate()

    def test_stalemate_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "black"
        board.pecas_tabuleiro[0][0] = Rei(0, 0, "black", tile_length, moves=1)
        board.pecas_tabuleiro[1][0] = Peao(1, 0, "white", tile_length)
        board.pecas_tabuleiro[2][1] = Rei(2, 1, "white", tile_length, moves=1)
        
        assert board.stalemate()

    def test_stalemate_three(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "black"
        board.pecas_tabuleiro[0][7] = Rei(0, 7, "black", tile_length, moves=1)
        board.pecas_tabuleiro[2][6] = Rei(2, 6, "white", tile_length, moves=1)
        board.pecas_tabuleiro[2][7] = Peao(2, 7, "white", tile_length)
        board.pecas_tabuleiro[3][3] = Bispo(3, 3, "white", tile_length)
        
        assert board.stalemate()

    def test_stalemate_four(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "white"
        board.pecas_tabuleiro[0][7] = Rei(0, 7, "white", tile_length, moves=1)
        board.pecas_tabuleiro[1][7] = Peao(1, 7, "white", tile_length)
        board.pecas_tabuleiro[2][6] = Rainha(2, 6, "black", tile_length)
        board.pecas_tabuleiro[5][1] = Rei(5, 1, "black", tile_length, moves=1)
        
        assert board.stalemate()

    def test_stalemate_five(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "white"
        board.pecas_tabuleiro[1][5] = Bispo(2, 6, "black", tile_length)
        board.pecas_tabuleiro[2][5] = Rei(2, 5, "black", tile_length, moves=1)
        board.pecas_tabuleiro[2][7] = Rei(2, 7, "white", tile_length, moves=1)
        
        assert board.stalemate()

    def test_stalemate_six(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "black"
        board.pecas_tabuleiro[2][0] = Peao(2, 0, "black", tile_length)
        board.pecas_tabuleiro[3][0] = Rei(3, 0, "black", tile_length, moves=1)
        board.pecas_tabuleiro[3][2] = Rei(3, 2, "white", tile_length, moves=1)
        board.pecas_tabuleiro[4][1] = Peao(4, 1, "black", tile_length)
        board.pecas_tabuleiro[4][2] = Peao(4, 2, "white", tile_length)
        board.pecas_tabuleiro[5][1] = Peao(5, 1, "white", tile_length)
        board.pecas_tabuleiro[6][0] = Peao(6, 0, "white", tile_length)
        
        assert board.stalemate()

    def test_stalemate_seven(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()
        board.jogador_atual = "white"
        board.pecas_tabuleiro[2][6] = Bispo(2, 6, "black", tile_length)
        board.pecas_tabuleiro[2][5] = Rei(2, 5, "black", tile_length, moves=1)
        board.pecas_tabuleiro[2][7] = Rei(2, 7, "white", tile_length, moves=1)
        board.pecas_tabuleiro[6][5] = Torre(6, 5, "black", tile_length)
        
        assert board.stalemate()