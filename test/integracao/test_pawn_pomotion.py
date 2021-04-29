from Peca import *
from tabuleiro import *
from config import *
from unittest import mock
import pygame

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255, 0, 0))

class TestPawnPromotion:

    @mock.patch("tabuleiro.PawnPromotionScreen")
    def test_pawn_promotion_white(self, mock_PawnPromotionScreen):

        mock_instance = mock_PawnPromotionScreen.return_value
        mock_instance.loop.return_value = 'queen'

        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[1][4] = Peao(1,4,'white',tile_length,5)
        board.pecas_tabuleiro[2][0] = Rei(2,0,'white',tile_length,5)
        board.pecas_tabuleiro[7][7] = Rei(7,7,'black',tile_length,5)

        board.piece_selected = board.pecas_tabuleiro[1][4]

        board.move(0,4)

        assert board.pecas_tabuleiro[0][4].name == 'queen'

    @mock.patch("tabuleiro.PawnPromotionScreen")
    def test_pawn_promotion_white_capture(self, mock_PawnPromotionScreen):

        mock_instance = mock_PawnPromotionScreen.return_value
        mock_instance.loop.return_value = 'queen'

        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[0][5] = Bispo(0,5,'black',tile_length,5)
        board.pecas_tabuleiro[1][4] = Peao(1,4,'white',tile_length,5)
        board.pecas_tabuleiro[2][0] = Rei(2,0,'white',tile_length,5)
        board.pecas_tabuleiro[7][7] = Rei(7,7,'black',tile_length,5)

        board.piece_selected = board.pecas_tabuleiro[1][4]

        board.move(0,5)

        assert board.pecas_tabuleiro[0][5].name == 'queen'

    @mock.patch("tabuleiro.PawnPromotionScreen")
    def test_pawn_promotion_black(self, mock_PawnPromotionScreen):

        mock_instance = mock_PawnPromotionScreen.return_value
        mock_instance.loop.return_value = 'queen'

        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[6][4] = Peao(6,4,'black',tile_length,5)
        board.pecas_tabuleiro[2][0] = Rei(2,0,'white',tile_length,5)
        board.pecas_tabuleiro[7][7] = Rei(7,7,'black',tile_length,5)

        board.piece_selected = board.pecas_tabuleiro[6][4]

        board.move(7,4)

        assert board.pecas_tabuleiro[7][4].name == 'queen'

    @mock.patch("tabuleiro.PawnPromotionScreen")
    def test_pawn_promotion_black_capture(self, mock_PawnPromotionScreen):

        mock_instance = mock_PawnPromotionScreen.return_value
        mock_instance.loop.return_value = 'queen'

        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[7][5] = Bispo(7,5,'white',tile_length,5)
        board.pecas_tabuleiro[6][4] = Peao(6,4,'black',tile_length,5)
        board.pecas_tabuleiro[2][0] = Rei(2,0,'white',tile_length,5)
        board.pecas_tabuleiro[7][7] = Rei(7,7,'black',tile_length,5)

        board.piece_selected = board.pecas_tabuleiro[6][4]

        board.move(7,5)

        assert board.pecas_tabuleiro[7][5].name == 'queen'