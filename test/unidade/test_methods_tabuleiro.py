from Peca import *
from tabuleiro import *
from config import *
from util import *
from unittest import mock
import pytest
import pygame

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255,0,0))

@mock.patch("tabuleiro.Tabuleiro.troca_turno")
@mock.patch("tabuleiro.Tabuleiro.place_piece")
@mock.patch("tabuleiro.Tabuleiro.capturar_peca")
@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.remove_piece")
def test_move_castle_king_side(mock_self_remove_piece, mock_self_get_piece, mock_self_capturar_peca, mock_self_place_piece, mock_self_troca_turno):
    mock_torre = mock.Mock(name="mock torre", **{'moves':0})
    mock_rei = mock.Mock(name="mock rei")
    mock_piece_selected = mock.Mock(**{'linha':7, 'coluna':4, 'moves':0})
    mock_piece_selected.name = "king"

    def side_effect_get_piece(linha, coluna):
        if(linha,coluna) == (7,7):
            return mock_torre
        elif(linha,coluna) == (7,4):
            return mock_rei
    
    mock_self_get_piece.side_effect = side_effect_get_piece

    board = Tabuleiro(display)
    board.piece_selected = mock_piece_selected
    board.move(7,6)

    assert mock_piece_selected.moves == 1
    assert mock_torre.moves == 1
    assert board.piece_selected == None
    assert board.possible_moves == []
    mock_self_remove_piece.assert_any_call(7,4)
    mock_self_remove_piece.assert_any_call(7,7)
    mock_self_place_piece.assert_any_call(mock_torre,7,5)
    mock_self_place_piece.assert_any_call(mock_piece_selected,7,6)
    mock_self_troca_turno.assert_called_once()

@mock.patch("tabuleiro.Tabuleiro.troca_turno")
@mock.patch("tabuleiro.Tabuleiro.place_piece")
@mock.patch("tabuleiro.Tabuleiro.capturar_peca")
@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.remove_piece")
def test_move_castle_queen_side(mock_self_remove_piece, mock_self_get_piece, mock_self_capturar_peca, mock_self_place_piece, mock_self_troca_turno):
    mock_torre = mock.Mock(name="mock torre", **{'moves':0})
    mock_rei = mock.Mock(name="mock rei")
    mock_piece_selected = mock.Mock(**{'linha':7, 'coluna':4, 'moves':0})
    mock_piece_selected.name = "king"

    def side_effect_get_piece(linha, coluna):
        if(linha,coluna) == (7,0):
            return mock_torre
        elif(linha,coluna) == (7,4):
            return mock_rei
        
    mock_self_get_piece.side_effect = side_effect_get_piece

    board = Tabuleiro(display)
    board.piece_selected = mock_piece_selected
    board.move(7,2)

    assert mock_piece_selected.moves == 1
    assert mock_torre.moves == 1
    assert board.piece_selected == None
    assert board.possible_moves == []
    mock_self_remove_piece.assert_any_call(7,4)
    mock_self_remove_piece.assert_any_call(7,0)
    mock_self_place_piece.assert_any_call(mock_torre,7,3)
    mock_self_place_piece.assert_any_call(mock_piece_selected,7,2)
    mock_self_troca_turno.assert_called_once()

@mock.patch("tabuleiro.Tabuleiro.promocao_peao")
@mock.patch("tabuleiro.Tabuleiro.troca_turno")
@mock.patch("tabuleiro.Tabuleiro.place_piece")
@mock.patch("tabuleiro.Tabuleiro.capturar_peca")
@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.remove_piece")
def test_move_pawn_promotion_white(mock_self_remove_piece, mock_self_get_piece, mock_self_capturar_peca, mock_self_place_piece, mock_self_troca_turno, mock_self_promocao_peao):
    mock_bispo = mock.Mock(name="mock bispo", **{'moves':0})
    mock_piece_selected = mock.Mock(**{'linha':1, 'coluna':4, 'moves':0, 'colour':'white'})
    mock_piece_selected.name = "pawn"
    mock_rainha = mock.Mock(name="mock rainha", **{'moves':1})

    def side_effect_get_piece(linha, coluna):
        if(linha,coluna) == (0,5):
            return mock_bispo
        
    mock_self_get_piece.side_effect = side_effect_get_piece
    mock_self_promocao_peao.return_value = mock_rainha

    board = Tabuleiro(display)
    board.piece_selected = mock_piece_selected
    board.move(0,5)

    assert mock_piece_selected.moves == 1
    assert board.piece_selected == None
    assert board.possible_moves == []
    mock_self_remove_piece.assert_any_call(1,4)
    mock_self_place_piece.assert_any_call(mock_rainha,0,5)
    mock_self_troca_turno.assert_called_once()
    mock_self_promocao_peao.assert_called_once()
    mock_self_capturar_peca.assert_any_call(mock_bispo)

@mock.patch("tabuleiro.Tabuleiro.promocao_peao")
@mock.patch("tabuleiro.Tabuleiro.troca_turno")
@mock.patch("tabuleiro.Tabuleiro.place_piece")
@mock.patch("tabuleiro.Tabuleiro.capturar_peca")
@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.remove_piece")
def test_move_pawn_promotion_black(mock_self_remove_piece, mock_self_get_piece, mock_self_capturar_peca, mock_self_place_piece, mock_self_troca_turno, mock_self_promocao_peao):
    mock_bispo = mock.Mock(name="mock bispo", **{'moves':0})
    mock_piece_selected = mock.Mock(**{'linha':6, 'coluna':4, 'moves':0, 'colour':'black'})
    mock_piece_selected.name = "pawn"
    mock_rainha = mock.Mock(name="mock rainha", **{'moves':1})

    def side_effect_get_piece(linha, coluna):
        if(linha,coluna) == (7,5):
            return mock_bispo
        
    mock_self_get_piece.side_effect = side_effect_get_piece
    mock_self_promocao_peao.return_value = mock_rainha

    board = Tabuleiro(display)
    board.piece_selected = mock_piece_selected
    board.move(7,5)

    assert mock_piece_selected.moves == 1
    assert board.piece_selected == None
    assert board.possible_moves == []
    mock_self_remove_piece.assert_any_call(6,4)
    mock_self_place_piece.assert_any_call(mock_rainha,7,5)
    mock_self_troca_turno.assert_called_once()
    mock_self_promocao_peao.assert_called_once()
    mock_self_capturar_peca.assert_any_call(mock_bispo)

@mock.patch("tabuleiro.Tabuleiro.stalemate")
@mock.patch("tabuleiro.Tabuleiro.is_in_check")
@mock.patch("tabuleiro.Tabuleiro.dead_position")
def test_troca_turno_dead_position(mock_self_dead_position, mock_self_is_in_check, mock_self_stalemate):
    mock_peca_1 = mock.Mock(name='peca1')
    mock_peca_2 = mock.Mock(name='peca2')
    mock_self_dead_position.return_value = True
    mock_self_is_in_check.return_value = False
    mock_self_stalemate.return_value = False

    board = Tabuleiro(display)
    board.jogador_atual = "white"
    board.turnos = 0
    board.pecas_capturadas_anterior = [mock_peca_1]
    board.pecas_capturadas = [mock_peca_1, mock_peca_2]

    board.troca_turno()

    assert board.jogador_atual == "black"
    assert board.turnos == 1
    assert board.fifty_moves == 1
    assert len(board.pecas_capturadas_anterior) == len(board.pecas_capturadas)
    assert board.get_out_of_check_moves == []
    assert board.screen_mode == "draw_dead_position"
    assert board.current_player_check == False

@mock.patch("tabuleiro.Tabuleiro.stalemate")
@mock.patch("tabuleiro.Tabuleiro.is_in_check")
@mock.patch("tabuleiro.Tabuleiro.dead_position")
def test_troca_turno_fifty_moves(mock_self_dead_position, mock_self_is_in_check, mock_self_stalemate):
    mock_peca_1 = mock.Mock(name='peca1')
    mock_peca_2 = mock.Mock(name='peca2')
    mock_self_dead_position.return_value = False
    mock_self_is_in_check.return_value = False
    mock_self_stalemate.return_value = False

    board = Tabuleiro(display)
    board.jogador_atual = "black"
    board.turnos = 0
    board.pecas_capturadas_anterior = [mock_peca_1, mock_peca_2]
    board.pecas_capturadas = [mock_peca_1, mock_peca_2]
    board.fifty_moves = 50

    board.troca_turno()

    assert board.jogador_atual == "white"
    assert board.turnos == 1
    assert board.get_out_of_check_moves == []
    assert board.screen_mode == "draw_fifty_moves"
    assert board.current_player_check == False

@mock.patch("tabuleiro.Tabuleiro.check_mate")
@mock.patch("tabuleiro.Tabuleiro.stalemate")
@mock.patch("tabuleiro.Tabuleiro.is_in_check")
@mock.patch("tabuleiro.Tabuleiro.dead_position")
def test_troca_turno_is_in_check(mock_self_dead_position, mock_self_is_in_check, mock_self_stalemate, mock_self_check_mate):
    mock_peca_1 = mock.Mock(name='peca1')
    mock_peca_2 = mock.Mock(name='peca2')
    mock_self_dead_position.return_value = False
    mock_self_is_in_check.return_value = True
    mock_self_stalemate.return_value = False
    mock_self_check_mate.return_value = True

    board = Tabuleiro(display)
    board.jogador_atual = "black"
    board.turnos = 0
    board.pecas_capturadas_anterior = [mock_peca_1, mock_peca_2]
    board.pecas_capturadas = [mock_peca_1, mock_peca_2]
    board.fifty_moves = 0

    board.troca_turno()

    assert board.jogador_atual == "white"
    assert board.turnos == 1
    assert board.get_out_of_check_moves == []
    assert board.screen_mode == "final_screen"
    assert board.current_player_check == True

@mock.patch("tabuleiro.Tabuleiro.stalemate")
@mock.patch("tabuleiro.Tabuleiro.is_in_check")
@mock.patch("tabuleiro.Tabuleiro.dead_position")
def test_troca_turno_stalemate(mock_self_dead_position, mock_self_is_in_check, mock_self_stalemate):
    mock_peca_1 = mock.Mock(name='peca1')
    mock_peca_2 = mock.Mock(name='peca2')
    mock_self_dead_position.return_value = False
    mock_self_is_in_check.return_value = False
    mock_self_stalemate.return_value = True

    board = Tabuleiro(display)
    board.jogador_atual = "black"
    board.turnos = 0
    board.pecas_capturadas_anterior = [mock_peca_1, mock_peca_2]
    board.pecas_capturadas = [mock_peca_1, mock_peca_2]
    board.fifty_moves = 0

    board.troca_turno()

    assert board.jogador_atual == "white"
    assert board.turnos == 1
    assert board.get_out_of_check_moves == []
    assert board.screen_mode == "draw_stalemate"
    assert board.current_player_check == False

@pytest.mark.parametrize("linha, coluna, expected", [(0,0,True),(9,0,False),(8,8,False),(5,4,True),(2,3,True),(-1,0,False)])
def test_posicao_valida(linha,coluna,expected):
    board = Tabuleiro(display)
    assert board.posicao_valida(linha,coluna) == expected

@mock.patch("tabuleiro.Tabuleiro.posicao_valida")
def test_pode_mover_pos_invalida(mock_self_posicao_valida):
    mock_self_posicao_valida.return_value = False

    board = Tabuleiro(display)

    assert board.pode_mover(mock.Mock(),0,0) == False

@pytest.mark.parametrize("linha, coluna, cor, expected", [(0,0,'',True),(6,5,'white',False),(0,7,'black',True)])
@mock.patch("tabuleiro.Tabuleiro.get_piece")
def test_pode_mover_combinacoes(mock_self_get_piece, linha, coluna, cor, expected):

    def side_effect_get_piece(linha, coluna):
        if (linha, coluna) == (0,0):
            return None
        elif (linha,coluna) == (6,5):
            return mock.Mock(**{'colour':'white'})
        elif (linha,coluna) == (0,7):
            return mock.Mock(**{'colour':'black'})

    mock_peca = mock.Mock(**{'colour':'white'})
    mock_self_get_piece.side_effect = side_effect_get_piece

    board = Tabuleiro(display)

    assert board.pode_mover(mock_peca,linha,coluna) == expected

@mock.patch("tabuleiro.Rainha")
@mock.patch("tabuleiro.Torre")
@mock.patch("tabuleiro.Bispo")
@mock.patch("tabuleiro.Cavalo")
@mock.patch("tabuleiro.PawnPromotionScreen")
def test_promocao_peao(mock_PawnPromotionScreen, mock_Cavalo, mock_Bispo, mock_Torre, mock_Rainha):

    mock_instance = mock_PawnPromotionScreen.return_value
    mock_instance.loop.side_effect = ["queen", "rook", "bishop", "knight"]

    board = Tabuleiro(display)
    board.piece_selected = mock.Mock(**{'linha':0, 'coluna':0, 'colour':'white', 'moves':0})

    board.promocao_peao()
    mock_Rainha.assert_called_once_with(0,0,'white',tile_length,0)
    board.promocao_peao()
    mock_Torre.assert_called_once_with(0,0,'white',tile_length,0)
    board.promocao_peao()
    mock_Bispo.assert_called_once_with(0,0,'white',tile_length,0)
    board.promocao_peao()
    mock_Cavalo.assert_called_once_with(0,0,'white',tile_length,0)

@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.move")
def test_validate_click_primeiro(mock_self_move, mock_self_get_piece):

    mock_piece_selected = mock.Mock()
    mock_piece_selected.name = 'pawn'
    mock_self_get_piece.return_value = None

    board = Tabuleiro(display)

    board.piece_selected = mock_piece_selected
    board.possible_moves = [[1,2]]

    board.validate_click(tile_length*2,tile_length)

    assert board.fifty_moves == 0
    assert board.piece_selected == None
    mock_self_move.assert_called_once_with(1,2)

@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.move")
def test_validate_click_segundo_in_check(mock_self_move, mock_self_get_piece):

    mock_peca_clicada = mock.Mock(**{'linha':1, 'coluna':2, 'colour':'black', 'get_movements.return_value':[[2,3]]})

    mock_self_get_piece.return_value = mock_peca_clicada

    board = Tabuleiro(display)

    board.piece_selected = None
    board.jogador_atual = "black"
    board.current_player_check = True
    board.get_out_of_check_moves = [(mock.Mock(**{'linha':1, 'coluna':2}), 2, 3)]

    board.validate_click(tile_length*2,tile_length)

    assert board.possible_moves == [[2,3]]
    assert board.piece_selected == mock_peca_clicada

@mock.patch("tabuleiro.Tabuleiro.get_out_of_check")
@mock.patch("tabuleiro.Tabuleiro.get_piece")
@mock.patch("tabuleiro.Tabuleiro.move")
def test_validate_click_segundo_not_in_check(mock_self_move, mock_self_get_piece, mock_self_get_out_of_check):

    def side_effect_get_out_of_check(peca,linha,coluna):
        if peca.linha == 1 and peca.coluna == 2 and linha == 2 and coluna == 3:
            return True

    mock_peca_clicada = mock.Mock(**{'linha':1, 'coluna':2, 'colour':'black', 'get_movements.return_value':[[2,3]]})

    mock_self_get_piece.return_value = mock_peca_clicada
    mock_self_get_out_of_check.side_effect = side_effect_get_out_of_check

    board = Tabuleiro(display)

    board.piece_selected = None
    board.jogador_atual = "black"
    board.current_player_check = False
    board.get_out_of_check_moves = [(mock.Mock(**{'linha':1, 'coluna':2}), 2, 3)]

    board.validate_click(tile_length*2,tile_length)

    assert board.possible_moves == [[2,3]]