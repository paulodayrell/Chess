import pygame, atheris, tabuleiro
import sys
from pygame.locals import *
import time
from config import *
from Peca import *
from minimax import *
from move import Move
from final_screen import *
from pawn_promotion_screen import *

class chess_fuzz(tabuleiro.Tabuleiro):
    def __init__(self, display):
        super().__init__(display)

    def fuzz_loop(self, data):
        fdp = atheris.FuzzedDataProvider(data)
        x, y = fdp.ConsumeIntList(2, 4)
        self.validate_click(x, y)

    def loop(self, type_game):
        framesPerSecond = pygame.time.Clock()
        self.pecas_tabuleiro = self.reseta_tabuleiro()

        while self.screen_mode == "playing":

            if type_game == 2:
                self.ai_play()
                time.sleep(1)

            if not type_game == 1 and self.jogador_atual == 'black':
                aux_board = self.copy()
                mv = minimax(aux_board, 2, float('-inf'),
                             float('inf'), True, 'black')

                piece = self.get_piece(
                    mv[0].from_coord[0], mv[0].from_coord[1])
                if piece and piece.name == 'pawn':
                    if mv[0].to_coord[0] == 7:
                        queen = Rainha(piece.linha, piece.coluna,
                                       piece.colour, tile_length, piece.moves)
                        self.place_piece(queen, queen.linha, queen.coluna)

                    self.fifty_moves = 0

                self.make_move(mv[0])
                self.troca_turno()

            if type_game == 0 and self.jogador_atual == 'black':
                self.ai_play()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 27:  # 27 == "ESC"
                        self.screen_mode = "menu"
                else:
                    atheris.Setup(sys.argv, self.fuzz_loop)
                    atheris.Fuzz()
                    self.ai_play()

            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)

        self.get_final_screen()

        self.screen_mode = "playing"




pygame.init()
framesPerSecond = pygame.time.Clock()

display = pygame.display.set_mode(size)
pygame.display.set_caption('Chess')
display.fill((255, 0, 0))

tabuleiro = chess_fuzz(display)
tabuleiro.loop(0)


