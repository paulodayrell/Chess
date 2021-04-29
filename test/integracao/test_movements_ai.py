from Peca import *
from config import *
from tabuleiro import *
from move import *

class TestMovimentsAI:
    
    def test_get_regular_move_if_player_not_in_check(self, mocker):
        
        movement = (0,0)
        piece = Rei(movement[0], movement[1], "white", tile_length, moves=1)
        mocker.patch.object(Rei, 'get_movements', return_value=[movement])
        mocker.patch.object(Tabuleiro, 'get_out_of_check', return_value=True)

        assert isinstance(Tabuleiro.get_regular_move(Tabuleiro, piece), Move)

    def test_get_regular_move_if_player_in_check(self, mocker):
                
        movement = (0,0)
        piece = Rei(movement[0], movement[1], "white", tile_length, moves=1)
        mocker.patch.object(Rei, 'get_movements', return_value=[movement])
        mocker.patch.object(Tabuleiro, 'get_out_of_check', return_value=False)

        assert not isinstance(Tabuleiro.get_regular_move(Tabuleiro, piece), Move)

    def test_get_piece_out_of_check_moves_has_move(self, mocker):
        
        movement = (0,0)
        piece = Rei(movement[0], movement[1], "white", tile_length, moves=1)
        mocker.patch.object(Rei, 'get_movements', return_value=[movement])
        Tabuleiro.get_out_of_check_moves = [(Rei, 0,0)]
        mocker.patch.object(Tabuleiro, 'get_out_of_check', return_value=True)
        mocker.patch.object(Tabuleiro, 'move_gets_piece_out_of_check', return_value=True)
        
        assert isinstance(Tabuleiro.get_piece_out_of_check_moves(Tabuleiro, piece), Move)

    def test_get_piece_out_of_check_moves_has_no_moves(self, mocker):
        
        movement = (0,0)
        piece = Rei(movement[0], movement[1], "white", tile_length, moves=1)
        mocker.patch.object(Rei, 'get_movements', return_value=[movement])
        Tabuleiro.get_out_of_check_moves = [(Rei, 0,7)]
        mocker.patch.object(Tabuleiro, 'get_out_of_check', return_value=True)
        mocker.patch.object(Tabuleiro, 'move_gets_piece_out_of_check', return_value=True)
        
        assert not isinstance(Tabuleiro.get_piece_out_of_check_moves(Tabuleiro, piece), Move)

    def test_move_gets_piece_out_of_check_is_true(self):
        movement = (0,0)
        piece = Rei(movement[0], movement[1], "white", tile_length, moves=1)
        
        assert Tabuleiro.move_gets_piece_out_of_check(Tabuleiro, piece, movement[0], movement[1])
        
    def test_move_gets_piece_out_of_check_is_false(self):
        movement = (0,0)
        movement_1 = (0, 1)
        piece = Rei(movement[0], movement[1], "white", tile_length, moves=1)
        
        assert not Tabuleiro.move_gets_piece_out_of_check(Tabuleiro, piece, movement_1[0], movement_1[1])
        
    def test_get_moves_returns_array_if_in_check(self, mocker):
        movement = (0,0)
        Tabuleiro.pecas_tabuleiro = Tabuleiro.reseta_tabuleiro(Tabuleiro)
        Tabuleiro.jogador_atual = 'white'
        Tabuleiro.current_player_check = True
        move = Move([movement[0], movement[1]], movement, None)
        mocker.patch.object(Tabuleiro, 'get_piece_out_of_check_moves', return_value=move)
        mocker.patch.object(Tabuleiro, 'get_regular_move', return_value=None)
        assert len(Tabuleiro.get_moves(Tabuleiro))
        
    def test_get_moves_returns_array_if_not_in_check(self, mocker):
        movement = (0,0)
        Tabuleiro.pecas_tabuleiro = Tabuleiro.reseta_tabuleiro(Tabuleiro)
        Tabuleiro.jogador_atual = 'white'
        Tabuleiro.current_player_check = True
        move = Move([movement[0], movement[1]], movement, None)
        mocker.patch.object(Tabuleiro, 'get_piece_out_of_check_moves', return_value=None)
        mocker.patch.object(Tabuleiro, 'get_regular_move', return_value=move)
        assert len(Tabuleiro.get_moves(Tabuleiro))
    
    def test_get_moves_returns_empty_array(self, mocker):
        movement = (0,0)
        Tabuleiro.pecas_tabuleiro = Tabuleiro.reseta_tabuleiro(Tabuleiro)
        Tabuleiro.jogador_atual = 'black'
        Tabuleiro.current_player_check = True
        move = Move([movement[0], movement[1]], movement, None)
        mocker.patch.object(Tabuleiro, 'get_piece_out_of_check_moves', return_value=None)
        mocker.patch.object(Tabuleiro, 'get_regular_move', return_value=None)
        assert not len(Tabuleiro.get_moves(Tabuleiro))