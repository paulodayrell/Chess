from Peca import *
from config import *
from tabuleiro import *

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255, 0, 0))


class TestBasicMovementClass:

    def test_king_top_left(self):
        position = (0, 0)
        king = Rei(position[0], position[1], "white", tile_length, moves=1)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = king

        movements = king.get_movements(tabuleiro)

        condition = True

        if [0, 1] not in movements:
            condition = False
        if [1, 0] not in movements:
            condition = False
        if [1, 1] not in movements:
            condition = False

        assert condition

    def test_king_top_right(self):
        position = (0, 7)
        king = Rei(position[0], position[1], "white", tile_length, moves=1)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = king

        movements = king.get_movements(tabuleiro)

        condition = True

        if [0, 6] not in movements:
            condition = False
        if [1, 6] not in movements:
            condition = False
        if [1, 7] not in movements:
            condition = False

        assert condition

    def test_king_bottom_left(self):
        position = (7, 0)
        king = Rei(position[0], position[1], "white", tile_length, moves=1)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = king

        movements = king.get_movements(tabuleiro)

        condition = True

        if [6, 0] not in movements:
            condition = False
        if [6, 1] not in movements:
            condition = False
        if [7, 1] not in movements:
            condition = False

        assert condition

    def test_king_bottom_right(self):
        position = (7, 7)
        king = Rei(position[0], position[1], "white", tile_length, moves=1)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = king

        movements = king.get_movements(tabuleiro)

        condition = True

        if [6, 6] not in movements:
            condition = False
        if [6, 7] not in movements:
            condition = False
        if [7, 6] not in movements:
            condition = False

        assert condition

    def test_queen_top_left(self):
        position = (0, 0)
        queen = Rainha(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = queen

        movements = queen.get_movements(tabuleiro)

        template = [
            [0, 1], [0, 2], [0, 3], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # Vertical
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_queen_top_right(self):
        position = (0, 7)
        queen = Rainha(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = queen

        movements = queen.get_movements(tabuleiro)

        template = [
            [0, 0], [0, 1], [0, 2], [0, 3], [
                0, 4], [0, 5], [0, 6],  # Horizontal
            [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7],  # Vertical
            [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_queen_bottom_left(self):
        position = (7, 0)
        queen = Rainha(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = queen

        movements = queen.get_movements(tabuleiro)
        template = [
            [7, 1], [7, 2], [7, 3], [7, 4], [
                7, 5], [7, 6], [7, 7],  # Horizontal
            [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0],  # Vertical
            [0, 7], [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_queen_bottom_right(self):
        position = (7, 7)
        queen = Rainha(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = queen

        movements = queen.get_movements(tabuleiro)

        template = [
            [7, 0], [7, 1], [7, 2], [7, 3], [
                7, 4], [7, 5], [7, 6],  # Horizontal
            [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7],  # Vertical
            [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_rook_top_left(self):
        position = (0, 0)
        rook = Torre(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = rook

        movements = rook.get_movements(tabuleiro)

        template = [
            [0, 1], [0, 2], [0, 3], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # Vertical
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_rook_top_right(self):
        position = (0, 7)
        rook = Torre(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = rook

        movements = rook.get_movements(tabuleiro)

        template = [
            [0, 0], [0, 1], [0, 2], [0, 3], [
                0, 4], [0, 5], [0, 6],  # Horizontal
            [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7],  # Vertical
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_rook_bottom_left(self):
        position = (7, 0)
        rook = Torre(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = rook

        movements = rook.get_movements(tabuleiro)

        template = [
            [7, 1], [7, 2], [7, 3], [7, 4], [
                7, 5], [7, 6], [7, 7],  # Horizontal
            [0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0],  # Vertical
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_rook_bottom_right(self):
        position = (7, 7)
        rook = Torre(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = rook

        movements = rook.get_movements(tabuleiro)

        template = [
            [7, 0], [7, 1], [7, 2], [7, 3], [
                7, 4], [7, 5], [7, 6],  # Horizontal
            [0, 7], [1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7],  # Vertical
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_bishop_top_left(self):
        position = (0, 0)
        bishop = Bispo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = bishop

        movements = bishop.get_movements(tabuleiro)

        template = [
            [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [7, 7]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_bishop_top_right(self):
        position = (0, 7)
        bishop = Bispo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = bishop

        movements = bishop.get_movements(tabuleiro)

        template = [
            [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1], [7, 0]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_bishop_bottom_left(self):
        position = (7, 0)
        bishop = Bispo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = bishop

        movements = bishop.get_movements(tabuleiro)

        template = [
            [0, 7], [1, 6], [2, 5], [3, 4], [4, 3], [5, 2], [6, 1]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_bishop_bottom_right(self):
        position = (7, 7)
        bishop = Bispo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = bishop

        movements = bishop.get_movements(tabuleiro)

        template = [
            [0, 0], [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]  # Diagonal
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_knight_top_left(self):
        position = (0, 0)
        knight = Cavalo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = knight

        movements = knight.get_movements(tabuleiro)

        template = [
            [1, 2], [2, 1]
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_knight_top_right(self):
        position = (0, 7)
        knight = Cavalo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = knight

        movements = knight.get_movements(tabuleiro)

        template = [
            [1, 5], [2, 6]
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_knight_bottom_left(self):
        position = (7, 0)
        knight = Cavalo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = knight

        movements = knight.get_movements(tabuleiro)

        template = [
            [5, 1], [6, 2]
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_knight_bottom_right(self):
        position = (7, 7)
        knight = Cavalo(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = knight

        movements = knight.get_movements(tabuleiro)

        template = [
            [6, 5], [5, 6]
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_pawn_top_left(self):
        position = (0, 0)
        pawn = Peao(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = pawn

        movements = pawn.get_movements(tabuleiro)

        template = []

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_pawn_top_right(self):
        position = (0, 7)
        pawn = Peao(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = pawn

        movements = pawn.get_movements(tabuleiro)

        template = []

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_pawn_bottom_left(self):
        position = (7, 0)
        pawn = Peao(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = pawn

        movements = pawn.get_movements(tabuleiro)

        template = [
            [5, 0], [6, 0]
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_pawn_bottom_right(self):
        position = (7, 7)
        pawn = Peao(position[0], position[1], "white", tile_length)

        tabuleiro = Tabuleiro(display)
        tabuleiro.clear_board()
        tabuleiro.pecas_tabuleiro[position[0]][position[1]] = pawn

        movements = pawn.get_movements(tabuleiro)

        template = [
            [5, 7], [6, 7]
        ]

        condition = True

        for coordinate in template:
            if coordinate not in movements:
                condition = False

        assert condition

    def test_king_initial_movements(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()

        peace = tabuleiro.get_piece(0, 4)

        template_movements = [
            [0, 3], [0, 5], [1, 3], [1, 4], [1, 5]
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = []
        template_can_not_move = [
            [0, 3], [0, 5], [1, 3], [1, 4], [1, 5]
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_king_initial_movements_without_pawn(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()
        tabuleiro.pecas_tabuleiro[1] = [None for x in range(8)]

        peace = tabuleiro.get_piece(0, 4)

        template_movements = [
            [0, 3], [0, 5], [1, 3], [1, 4], [1, 5]
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [1, 3], [1, 4], [1, 5]
        ]
        template_can_not_move = [
            [0, 3], [0, 5]
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_queen_initial_movements(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()

        peace = tabuleiro.get_piece(0, 3)

        template_movements = [
            [0, 0], [0, 1], [0, 2], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3],  # Vertical
            [1, 2], [2, 1], [3, 0],  # Diagonal Inferior Esquerda
            [1, 4], [2, 5], [3, 6], [4, 7]  # Diagonal Inferior Direita
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = []
        template_can_not_move = [
            [0, 0], [0, 1], [0, 2], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3],  # Vertical
            [1, 2], [2, 1], [3, 0],  # Diagonal Inferior Esquerda
            [1, 4], [2, 5], [3, 6], [4, 7]  # Diagonal Inferior Direita]
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_queen_initial_movements_without_pawn(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()
        tabuleiro.pecas_tabuleiro[1] = [None for x in range(8)]

        peace = tabuleiro.get_piece(0, 3)

        template_movements = [
            [0, 0], [0, 1], [0, 2], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3],  # Vertical
            [1, 2], [2, 1], [3, 0],  # Diagonal Inferior Esquerda
            [1, 4], [2, 5], [3, 6], [4, 7]  # Diagonal Inferior Direita
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3],  # Vertical
            [1, 2], [2, 1], [3, 0],  # Diagonal Inferior Esquerda
            [1, 4], [2, 5], [3, 6], [4, 7]  # Diagonal Inferior Direita]
        ]
        template_can_not_move = [
            [0, 0], [0, 1], [0, 2], [0, 4], [
                0, 5], [0, 6], [0, 7]  # Horizontal
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_rook_initial_movements(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()

        peace = tabuleiro.get_piece(0, 0)

        template_movements = [
            [0, 1], [0, 2], [0, 3], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # Vertical
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = []
        template_can_not_move = [
            [0, 1], [0, 2], [0, 3], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # Vertical
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_rook_initial_movements_without_pawn(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()
        tabuleiro.pecas_tabuleiro[1] = [None for x in range(8)]

        peace = tabuleiro.get_piece(0, 0)

        template_movements = [
            [0, 1], [0, 2], [0, 3], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0],  # Vertical
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]  # Vertical
        ]
        template_can_not_move = [
            [0, 1], [0, 2], [0, 3], [0, 4], [
                0, 5], [0, 6], [0, 7],  # Horizontal
            [7, 0]  # Vertical
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_bishop_initial_movements(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()

        peace = tabuleiro.get_piece(0, 2)

        template_movements = [
            [1, 1], [2, 0],  # Diagonal Equerda Inferior
            [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]  # Diagonal Direita Inferior
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = []
        template_can_not_move = [
            [1, 1], [2, 0],  # Diagonal Equerda Inferior
            [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]  # Diagonal Direita Inferior
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_bishop_initial_movements_without_pawn(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()
        tabuleiro.pecas_tabuleiro[1] = [None for x in range(8)]

        peace = tabuleiro.get_piece(0, 2)

        template_movements = [
            [1, 1], [2, 0],  # Diagonal Equerda Inferior
            [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]  # Diagonal Direita Inferior
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [1, 1], [2, 0],  # Diagonal Equerda Inferior
            [1, 3], [2, 4], [3, 5], [4, 6], [5, 7]  # Diagonal Direita Inferior
        ]
        template_can_not_move = []

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_knight_initial_movements(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()

        peace = tabuleiro.get_piece(0, 1)

        template_movements = [
            [2, 0], [2, 2], [1, 3]
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [2, 0], [2, 2]
        ]
        template_can_not_move = [
            [1, 3]
        ]

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_knight_initial_movements_without_pawn(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()
        tabuleiro.pecas_tabuleiro[1] = [None for x in range(8)]

        peace = tabuleiro.get_piece(0, 1)

        template_movements = [
            [2, 0], [2, 2], [1, 3]
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [2, 0], [2, 2], [1, 3]
        ]
        template_can_not_move = []

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition

    def test_pawn_initial_movements(self):
        tabuleiro = Tabuleiro(display)
        tabuleiro.pecas_tabuleiro = tabuleiro.reseta_tabuleiro()

        peace = tabuleiro.get_piece(1, 1)

        template_movements = [
            [2, 1], [3, 1]  # Vertical
        ]

        # Definindo as posicoes que ela pode se movimentar
        template_can_move = [
            [2, 1], [3, 1]  # Vertical
        ]
        template_can_not_move = []

        movements = peace.get_movements(tabuleiro)

        condition = True

        for coordinate in template_can_move:
            if [coordinate[0], coordinate[1]] not in movements:
                condition = False

        for coordinate in template_can_not_move:
            if [coordinate[0], coordinate[1]] in movements:
                condition = False

        assert condition
