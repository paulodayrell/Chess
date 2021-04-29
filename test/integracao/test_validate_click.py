from Peca import *
from tabuleiro import *
from config import *
from util import *
import pygame

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255,0,0))

class TestValidateClickClass:
    def test_black_king_clicks(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()
        board.pecas_tabuleiro[1] = [None for x in range(8)]
        
        board.jogador_atual = "black"

        coords_first_click = (0, 4)
        coords_second_click = (1, 5)

        piece = board.get_piece(coords_first_click[0], coords_first_click[1])

        board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
        board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        template_board = Tabuleiro(display)
        template_board.pecas_tabuleiro = template_board.reseta_tabuleiro()
        template_board.pecas_tabuleiro[1] = [None for x in range(8)]

        template_board.pecas_tabuleiro[0][4] = None
        template_board.pecas_tabuleiro[1][5] = piece

        assert UtilTable.compareBoards(board, template_board)

    def test_black_queen_clicks(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()
        board.pecas_tabuleiro[1] = [None for x in range(8)]
        
        board.jogador_atual = "black"

        coords_first_click = (0, 3)
        coords_second_click = (4, 7)

        piece = board.get_piece(coords_first_click[0], coords_first_click[1])

        board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
        board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        template_board = Tabuleiro(display)
        template_board.pecas_tabuleiro = template_board.reseta_tabuleiro()
        template_board.pecas_tabuleiro[1] = [None for x in range(8)]

        template_board.pecas_tabuleiro[coords_first_click[0]][coords_first_click[1]] = None
        template_board.pecas_tabuleiro[coords_second_click[0]][coords_second_click[1]] = piece

        assert UtilTable.compareBoards(board, template_board)

    def test_black_rook_clicks(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()
        board.pecas_tabuleiro[1] = [None for x in range(8)]
        
        board.jogador_atual = "black"

        coords_first_click = (0, 0)
        coords_second_click = (6, 0)

        piece = board.get_piece(coords_first_click[0], coords_first_click[1])

        board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
        board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        template_board = Tabuleiro(display)
        template_board.pecas_tabuleiro = template_board.reseta_tabuleiro()
        template_board.pecas_tabuleiro[1] = [None for x in range(8)]

        template_board.pecas_tabuleiro[coords_first_click[0]][coords_first_click[1]] = None
        template_board.pecas_tabuleiro[coords_second_click[0]][coords_second_click[1]] = piece

        assert UtilTable.compareBoards(board, template_board)

    def test_black_bishop_clicks(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()
        board.pecas_tabuleiro[1] = [None for x in range(8)]
        
        board.jogador_atual = "black"

        coords_first_click = (0, 2)
        coords_second_click = (5, 7)

        piece = board.get_piece(coords_first_click[0], coords_first_click[1])

        board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
        board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        template_board = Tabuleiro(display)
        template_board.pecas_tabuleiro = template_board.reseta_tabuleiro()
        template_board.pecas_tabuleiro[1] = [None for x in range(8)]

        template_board.pecas_tabuleiro[coords_first_click[0]][coords_first_click[1]] = None
        template_board.pecas_tabuleiro[coords_second_click[0]][coords_second_click[1]] = piece

        assert UtilTable.compareBoards(board, template_board)


    def test_black_knight_clicks(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()
        board.pecas_tabuleiro[1] = [None for x in range(8)]
        
        board.jogador_atual = "black"

        coords_first_click = (0, 6)
        coords_second_click = (2, 7)

        piece = board.get_piece(coords_first_click[0], coords_first_click[1])

        board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
        board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        template_board = Tabuleiro(display)
        template_board.pecas_tabuleiro = template_board.reseta_tabuleiro()
        template_board.pecas_tabuleiro[1] = [None for x in range(8)]

        template_board.pecas_tabuleiro[coords_first_click[0]][coords_first_click[1]] = None
        template_board.pecas_tabuleiro[coords_second_click[0]][coords_second_click[1]] = piece

        assert UtilTable.compareBoards(board, template_board)

    def test_black_pawn_clicks(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()
        
        board.jogador_atual = "black"

        coords_first_click = (1, 5)
        coords_second_click = (3, 5)

        piece = board.get_piece(coords_first_click[0], coords_first_click[1])

        board.validate_click(coords_first_click[1] * tile_length, coords_first_click[0] * tile_length)
        board.validate_click(coords_second_click[1] * tile_length, coords_second_click[0] * tile_length)

        template_board = Tabuleiro(display)
        template_board.pecas_tabuleiro = template_board.reseta_tabuleiro()

        template_board.pecas_tabuleiro[coords_first_click[0]][coords_first_click[1]] = None
        template_board.pecas_tabuleiro[coords_second_click[0]][coords_second_click[1]] = piece

        assert UtilTable.compareBoards(board, template_board)