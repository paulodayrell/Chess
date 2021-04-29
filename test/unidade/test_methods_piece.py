from unittest import mock
from Peca import *
from config import *

def has_same_content(list1, list2):
    for x in list1:
        if x not in list2:
            return False
    for y in list2:
        if y not in list1:
            return False
    return True

def test_movimentos_diagonais():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [
            (3, 3), (2, 2), (1, 1), (0, 0), # Diagonal Superior Esquerda
            (3, 5), (2, 6), (1, 7), # Diagonal Superior Direita
            (5, 3), (6, 2), (7, 1), # Diagonal Inferior Esquerda
            (5, 5), (6, 6), (7, 7) # Diagonal Inferior Direita
        ]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    piece = Peca(4, 4, 'black', 'bishop', tile_length, 0)

    assert has_same_content(piece.movimentos_diagonais(mock_board), [
        [3, 3], [2, 2], [1, 1], [0, 0], # Diagonal Superior Esquerda
        [5, 3], [6, 2], [7, 1], # Diagonal Inferior Esquerda
        [3, 5], [2, 6], [1, 7], # Diagonal Superior Direita
        [5, 5], [6, 6], [7, 7] # Diagonal Inferior Direita
    ])

@mock.patch("tabuleiro.Tabuleiro.pode_mover")
@mock.patch("tabuleiro.Tabuleiro.get_piece")
def test_movimentos_cruz(mock_tabuleiro_get_piece, mock_tabuleiro_pode_mover):
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [
            (3, 4), (2, 4), (1, 4), (0, 4), # Superior
            (4, 5), (4, 6), (4, 7), # Direita
            (5, 4), (6, 4), (7, 4), # Inferior
            (4, 3), (4, 2), (4, 1), (4, 0) # Esquerda
        ]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    piece = Peca(4, 4, 'black', 'rook', tile_length, 0)

    assert has_same_content(piece.movimentos_cruz(mock_board), [
        [3, 4], [2, 4], [1, 4], [0, 4], # Superior
        [5, 4], [6, 4], [7, 4], # Inferior
        [4, 3], [4, 2], [4, 1], [4, 0], # Esquerda
        [4, 5], [4, 6], [4, 7] # Direita
    ])

def test_teste_torre_para_roque():
    mock_rook = mock.Mock(**{'colour': 'black', 'moves': 0})
    mock_rook.name = "rook"
    mock_board = mock.Mock(**{})
    mock_board.get_piece.return_value = mock_rook

    king = Rei(0, 4, 'black', tile_length, 0)

    assert king.testeTorreParaRoque(mock_board, 0, 0) == True

def test_king_get_movements():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [(0, 1), (1, 0), (1, 1)]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.current_player_check = False
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    king = Rei(0, 0, 'black', tile_length, 1)

    assert has_same_content(king.get_movements(mock_board), [
        [0, 1], [1, 0], [1, 1]
    ])

def test_rook_get_movements_roque():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [(0, 3), (1, 3), (1, 4), (1, 5), (0, 5), (0, 2)]:
            return True
        else:
            return False

    def side_effect_get_piece(linha, coluna):
        if (linha, coluna) == (0, 0):
            mock_rook = mock.Mock(**{'linha': 0, 'coluna': 0, 'colour': 'black', 'tile_length': tile_length, 'moves': 0})
            mock_rook.name = "rook"
            return mock_rook
        else:
            return None

    mock_board = mock.Mock(**{})
    mock_board.current_player_check = False
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.side_effect = side_effect_get_piece

    king = Rei(0, 4, 'black', tile_length, 0)
    
    assert has_same_content(king.get_movements(mock_board), [
        [0, 3], [0, 5], [1, 3], [1, 4], [1, 5], [0, 2]
    ])

def test_bishop_get_movements():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [
            (3, 3), (2, 2), (1, 1), (0, 0), # Diagonal Superior Esquerda
            (3, 5), (2, 6), (1, 7), # Diagonal Superior Direita
            (5, 3), (6, 2), (7, 1), # Diagonal Inferior Esquerda
            (5, 5), (6, 6), (7, 7) # Diagonal Inferior Direita
        ]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    bishop = Bispo(4, 4, 'black', tile_length, 0)

    assert has_same_content(bishop.get_movements(mock_board), [
        [3, 3], [2, 2], [1, 1], [0, 0], # Diagonal Superior Esquerda
        [5, 3], [6, 2], [7, 1], # Diagonal Inferior Esquerda
        [3, 5], [2, 6], [1, 7], # Diagonal Superior Direita
        [5, 5], [6, 6], [7, 7] # Diagonal Inferior Direita
    ])

def test_knight_get_movements():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [
            (1, 2), (2, 1)
        ]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    knight = Cavalo(0, 0, 'black', tile_length, 0)

    assert has_same_content(knight.get_movements(mock_board), [[2, 1], [1, 2]])

def test_queen_get_movements():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)
        ]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    queen = Rainha(0, 0, 'black', tile_length, 0)

    assert has_same_content(queen.get_movements(mock_board), [
        [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7],
        [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],
        [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7]
    ])

def test_pawn_get_movements():
    def side_effect_pode_mover(self, linha, coluna):
        if (linha, coluna) in [
            (1, 0), (2, 0)
        ]:
            return True
        else:
            return False

    mock_board = mock.Mock(**{})
    mock_board.pode_mover.side_effect = side_effect_pode_mover
    mock_board.get_piece.return_value = None

    pawn = Peao(0, 0, 'black', tile_length, 0)

    assert has_same_content(pawn.get_movements(mock_board), [
        [1, 0], [2, 0]
    ])