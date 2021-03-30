from random import choice, sample
from Peca import *


def evaluate(board, max_color):
  if max_color == 'white': return board.white_score - board.black_score
  else: return board.black_score - board.white_score

def minimax(board, depth, alpha, beta, max_player, max_color):

  if not depth or not board.get_moves():
    return None, evaluate(board, max_color)

  moves = board.get_moves()
  best_move = choice(moves)


  if max_player:
    max_eval = float('-inf')
    for move in sample(moves, len(moves)):
      aux_board = board.copy()
      
      board.make_move(move)
      
      current_eval = minimax(board, depth -1, alpha, beta, False, max_color)[1]
      board = aux_board
      
      if current_eval > max_eval:
        max_eval = current_eval
        best_move = move
      alpha = max(alpha, current_eval)
      if beta <= alpha: break
    return best_move, max_eval
  else:
    min_eval = float('inf')
    for move in sample(moves, len(moves)):
      aux_board = board.copy()
      
      board.make_move(move)
      
      current_eval = minimax(board, depth -1, alpha, beta, True, max_color)[1]
      board = aux_board
      
      if current_eval < min_eval:
        min_eval = current_eval
        best_move = move
        beta = min(beta, current_eval)
        if beta <= alpha: break
    return best_move, min_eval
