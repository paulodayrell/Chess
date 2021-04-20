from Peca import *
from tabuleiro import *
from config import *
import pygame

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255, 0, 0))


class TestXeque:
    def test_is_in_check_by_queen_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando a rainha branca da posicao
        queen = board.get_piece(7, 3)
        board.pecas_tabuleiro[7][3] = None

        # Adicionando a rainha branca em posicao em que ele captura o rei inimigo
        queen.linha = 3
        queen.coluna = 7
        board.pecas_tabuleiro[3][7] = queen

        # Retirando o peao preto da frente para a rainha poder comer  o rei
        board.pecas_tabuleiro[1][5] = None

        board.jogador_atual = "black"

        template_is_in_check = True

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_queen_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando a rainha branca da posicao
        queen = board.get_piece(7, 3)
        board.pecas_tabuleiro[7][3] = None

        # Adicionando a rainha branca em posicao em que ele captura o rei inimigo
        queen.linha = 3
        queen.coluna = 7
        board.pecas_tabuleiro[3][7] = queen

        board.jogador_atual = "black"

        template_is_in_check = False

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_rook_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando a torre branca da posicao
        rook = board.get_piece(7, 7)
        board.pecas_tabuleiro[7][7] = None

        # Adicionandoa torre branca em posicao em que ela captura o rei inimigo
        rook.linha = 4
        rook.coluna = 4
        board.pecas_tabuleiro[4][4] = rook

        # Retirando o peao preto da frente para a torre poder comer  o rei
        board.pecas_tabuleiro[1][4] = None

        board.jogador_atual = "black"

        template_is_in_check = True

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_rook_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando a torre branca da posicao
        rook = board.get_piece(7, 7)
        board.pecas_tabuleiro[7][7] = None

        # Adicionandoa torre branca em posicao em que ela captura o rei inimigo
        rook.linha = 4
        rook.coluna = 4
        board.pecas_tabuleiro[4][4] = rook

        board.jogador_atual = "black"

        template_is_in_check = False

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_bishop_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o bispo branco da posicao dele
        bishop = board.get_piece(7, 5)
        board.pecas_tabuleiro[7][5] = None

        # Adicionando o bispo branco em posicao em que ele captura o rei inimigo
        bishop.linha = 3
        bishop.coluna = 1
        board.pecas_tabuleiro[3][1] = bishop

        # Retirando o peao preto da frente para o bispo poder comer  o rei
        board.pecas_tabuleiro[1][3] = None

        board.jogador_atual = "black"

        template_is_in_check = True

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_bishop_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o bispo branco da posicao dele
        bishop = board.get_piece(7, 5)
        board.pecas_tabuleiro[7][5] = None

        # Adicionando o bispo branco em posicao em que ele captura o rei inimigo
        bishop.linha = 3
        bishop.coluna = 1
        board.pecas_tabuleiro[3][1] = bishop

        board.jogador_atual = "black"

        template_is_in_check = False

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_knight_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o cavalo branco da posicao dele
        knight = board.get_piece(7, 6)
        board.pecas_tabuleiro[7][6] = None

        # Adicionando o cavalo branco em posicao em que ele captura o rei inimigo
        knight.linha = 2
        knight.coluna = 5
        board.pecas_tabuleiro[2][5] = knight

        board.jogador_atual = "black"

        template_is_in_check = True

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_pawn_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o peao branco da posicao dele
        pawn = board.get_piece(6, 0)
        board.pecas_tabuleiro[6][0] = None

        # Adicionando o peao branco em posicao em que ele captura o rei inimigo
        pawn.linha = 1
        pawn.coluna = 5
        board.pecas_tabuleiro[1][5] = pawn

        board.jogador_atual = "black"

        template_is_in_check = True

        assert board.is_in_check() == template_is_in_check

    def test_is_in_check_by_pawn_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o peao branco da posicao dele
        pawn = board.get_piece(6, 0)
        board.pecas_tabuleiro[6][0] = None

        # Adicionando o peao branco em posicao em que ele captura o rei inimigo
        pawn.linha = 1
        pawn.coluna = 4
        board.pecas_tabuleiro[1][4] = pawn

        board.jogador_atual = "black"

        template_is_in_check = False

        assert board.is_in_check() == template_is_in_check

    def test_get_out_of_check_by_queen_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando a rainha branca da posicao
        queen = board.get_piece(7, 3)
        board.pecas_tabuleiro[7][3] = None

        # Adicionando a rainha branca em posicao em que ela captura o rei inimigo
        queen.linha = 3
        queen.coluna = 7
        board.pecas_tabuleiro[3][7] = queen

        # Retirando o peao preto da frente para a rainha poder comer  o rei
        board.pecas_tabuleiro[1][5] = None

        board.jogador_atual = "black"

        template_get_out_of_check = True

        # Verificando se a movimentacao do peao na diagonal entre a rainha e o rei consegue retirar o cheque
        pawn = board.get_piece(1, 6)
        assert board.get_out_of_check(pawn, 2, 6) == template_get_out_of_check

    def test_get_out_of_check_by_rook_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando a torre branca da posicao
        rook = board.get_piece(7, 7)
        board.pecas_tabuleiro[7][7] = None

        # Adicionandoa torre branca em posicao em que ela captura o rei inimigo
        rook.linha = 4
        rook.coluna = 4
        board.pecas_tabuleiro[4][4] = rook

        # Retirando o peao preto da frente para a torre poder comer  o rei
        board.pecas_tabuleiro[1][4] = None

        board.jogador_atual = "black"

        template_get_out_of_check = True

        # Verificando se a movimentacao da rainha para frente do rei consegue retirar o cheque
        queen = board.get_piece(0, 3)
        assert board.get_out_of_check(queen, 1, 4) == template_get_out_of_check

    def test_get_out_of_check_by_bishop_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o bispo branco da posicao dele
        bishop = board.get_piece(7, 5)
        board.pecas_tabuleiro[7][5] = None

        # Adicionando o bispo branco em posicao em que ele captura o rei inimigo
        bishop.linha = 3
        bishop.coluna = 1
        board.pecas_tabuleiro[3][1] = bishop

        # Retirando o peao preto da frente para o bispo poder comer  o rei
        board.pecas_tabuleiro[1][3] = None

        board.jogador_atual = "black"

        template_get_out_of_check = True

        # Verificando se a movimentacao da rainha para frente do rei consegue retirar o cheque
        queen = board.get_piece(0, 3)
        assert board.get_out_of_check(queen, 1, 3) == template_get_out_of_check

    def test_get_out_of_check_by_knight_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o cavalo branco da posicao dele
        knight = board.get_piece(7, 6)
        board.pecas_tabuleiro[7][6] = None

        # Adicionando o cavalo branco em posicao em que ele captura o rei inimigo
        knight.linha = 2
        knight.coluna = 5
        board.pecas_tabuleiro[2][5] = knight

        board.jogador_atual = "black"

        template_get_out_of_check = True

        # Verificando se a movimentacao do peao comendo o cavalo consegue retirar o cheque
        pawn = board.get_piece(1, 6)
        assert board.get_out_of_check(pawn, 2, 5) == template_get_out_of_check

    def test_get_out_of_check_by_pawn_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        # Retirando o peao branco da posicao dele
        pawn = board.get_piece(6, 0)
        board.pecas_tabuleiro[6][0] = None

        # Adicionando o peao branco em posicao em que ele captura o rei inimigo
        pawn.linha = 1
        pawn.coluna = 5
        board.pecas_tabuleiro[1][5] = pawn

        board.jogador_atual = "black"

        template_get_out_of_check = True

        # Verificando se a movimentacao do proprio rei comendo o peao que o coloca em cheque consegue retirar o cheque
        king = board.get_piece(0, 4)
        assert board.get_out_of_check(king, 1, 5) == template_get_out_of_check

    def test_check_mate_one(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[1][7] = Torre(1, 7, "white", tile_length)
        board.pecas_tabuleiro[5][5] = Rei(5, 5, "white", tile_length, moves=1)
        board.pecas_tabuleiro[5][6] = Rei(5, 7, "black", tile_length, moves=1)

        board.jogador_atual = "black"

        template_check_mate = True

        assert board.check_mate() == template_check_mate

    def test_check_mate_two(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[1][5] = Rainha(1, 5, "white", tile_length)
        board.pecas_tabuleiro[2][4] = Rei(2, 4, "white", tile_length, moves=1)
        board.pecas_tabuleiro[0][5] = Rei(0, 5, "black", tile_length, moves=1)

        board.jogador_atual = "black"

        template_check_mate = True

        assert board.check_mate() == template_check_mate

    def test_check_mate_three(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.clear_board()

        board.pecas_tabuleiro[1][5] = Rainha(1, 4, "white", tile_length)
        board.pecas_tabuleiro[2][4] = Rei(2, 4, "white", tile_length, moves=1)
        board.pecas_tabuleiro[0][5] = Rei(0, 5, "black", tile_length, moves=1)

        board.jogador_atual = "black"

        template_check_mate = False

        assert board.check_mate() == template_check_mate

    def test_check_mate_four(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        white_pawn = board.get_piece(6, 4)
        board.pecas_tabuleiro[6][4] = None
        white_pawn.linha = 3
        white_pawn.coluna = 5
        board.pecas_tabuleiro[3][5] = white_pawn

        board.pecas_tabuleiro[1][5] = None

        black_pawn = board.get_piece(1, 6)
        board.pecas_tabuleiro[1][6] = None
        black_pawn.linha = 3
        black_pawn.coluna = 6
        board.pecas_tabuleiro[3][6] = black_pawn

        white_queen = board.get_piece(7, 3)
        board.pecas_tabuleiro[7][3] = None
        white_queen.linha = 3
        white_queen.coluna = 7
        board.pecas_tabuleiro[3][7] = white_queen

        board.jogador_atual = "black"

        template_check_mate = True

        assert board.check_mate() == template_check_mate

    def test_check_mate_five(self):
        # Gerando tabuleiro
        board = Tabuleiro(display)
        board.pecas_tabuleiro = board.reseta_tabuleiro()

        white_pawn = board.get_piece(6, 4)
        board.pecas_tabuleiro[6][4] = None
        white_pawn.linha = 3
        white_pawn.coluna = 5
        board.pecas_tabuleiro[3][5] = white_pawn

        board.pecas_tabuleiro[1][5] = None

        black_pawn = board.get_piece(1, 6)
        board.pecas_tabuleiro[1][6] = None
        black_pawn.linha = 3
        black_pawn.coluna = 6
        board.pecas_tabuleiro[3][6] = black_pawn

        white_queen = board.get_piece(7, 3)
        board.pecas_tabuleiro[7][3] = None
        white_queen.linha = 3
        white_queen.coluna = 7
        board.pecas_tabuleiro[3][7] = white_queen

        black_knight = board.get_piece(0, 1)
        board.pecas_tabuleiro[0][1] = None
        black_knight.linha = 2
        black_knight.coluna = 3
        board.pecas_tabuleiro[2][3] = black_knight

        board.jogador_atual = "black"

        template_check_mate = False

        assert board.check_mate() == template_check_mate
