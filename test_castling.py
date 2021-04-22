from Peca import *
from tabuleiro import *
from config import *
import pygame

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255, 0, 0))

class TestCastling:
    def test_castling_black_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando as peças que estao entre o Rei e a Torre
        king = board.get_piece(0, 4)
        board.pecas_tabuleiro[0][5] = None
        board.pecas_tabuleiro[0][6] = None

        board.jogador_atual = "black"

        board.piece_selected = king
        board.move(0, 6)

        assert board.pecas_tabuleiro[0][6].name == "king" and board.pecas_tabuleiro[0][5].name == "rook"

    def test_castling_black_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando as peças que estao entre o Rei e a Torre
        king = board.get_piece(0, 4)
        board.pecas_tabuleiro[0][1] = None
        board.pecas_tabuleiro[0][2] = None
        board.pecas_tabuleiro[0][3] = None

        board.jogador_atual = "black"

        board.piece_selected = king
        board.move(0, 2)

        assert board.pecas_tabuleiro[0][2].name == "king" and board.pecas_tabuleiro[0][3].name == "rook"

    def test_castling_white_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando as peças que estao entre o Rei e a Torre
        king = board.get_piece(7, 4)
        board.pecas_tabuleiro[7][5] = None
        board.pecas_tabuleiro[7][6] = None

        board.jogador_atual = "white"

        board.piece_selected = king
        board.move(7, 6)

        assert board.pecas_tabuleiro[7][6].name == "king" and board.pecas_tabuleiro[7][5].name == "rook"

    def test_castling_white_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando as peças que estao entre o Rei e a Torre
        king = board.get_piece(7, 4)
        board.pecas_tabuleiro[7][3] = None
        board.pecas_tabuleiro[7][2] = None
        board.pecas_tabuleiro[7][1] = None

        board.jogador_atual = "white"

        board.piece_selected = king
        board.move(7, 2)

        assert board.pecas_tabuleiro[7][2].name == "king" and board.pecas_tabuleiro[7][3].name == "rook"
