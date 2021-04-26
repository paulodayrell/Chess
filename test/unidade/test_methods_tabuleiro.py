from Peca import *
from tabuleiro import *
from config import *
from util import *
from unittest import mock
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
