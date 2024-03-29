import pygame, sys
from pygame.locals import *
from button import *
from config import *

class Menu():
    def __init__(self, display, board):
        self.surface = display
        self.buttonSize = {
            "w": 300,
            "h": 70
        }
        self.buttons = [
            Button( self.surface, 'Um Jogador', self.gotoBoardScreen, 0, (190, 190, 190), self.surface.get_width() / 2 - (self.buttonSize["w"] / 2), self.surface.get_height() / 2 - (self.buttonSize["h"] / 4) - (2 * self.buttonSize["h"]), self.buttonSize["w"], self.buttonSize["h"]),
            Button( self.surface, 'Multijogador', self.gotoBoardScreen, 1, (190, 190, 190), self.surface.get_width() / 2 - (self.buttonSize["w"] / 2), self.surface.get_height() / 2 - (self.buttonSize["h"] / 4) - (1/2 * self.buttonSize["h"]), self.buttonSize["w"], self.buttonSize["h"]),
            Button( self.surface, 'IA X IA', self.gotoBoardScreen, 2, (190, 190, 190), self.surface.get_width() / 2 - (self.buttonSize["w"] / 2), self.surface.get_height() / 2 - (self.buttonSize["h"] / 4) + 1 * self.buttonSize["h"], self.buttonSize["w"], self.buttonSize["h"]),
            Button( self.surface, 'Sair', self.exit, None, (190, 190, 190), self.surface.get_width() / 2 - (self.buttonSize["w"] / 2), self.surface.get_height() / 2 - (self.buttonSize["h"] / 4) + (2.5 * self.buttonSize["h"]), self.buttonSize["w"], self.buttonSize["h"])
        ]

        self.board = board

    def draw(self, surface):

        surface.fill((124, 76, 62))

        buttonWidth = self.buttonSize["w"]
        buttonHeight = self.buttonSize["h"]

        # Renderizando título "Menu"
        textTitle = pygame.font.Font.render(pygame.font.SysFont('comicsansms', 32), "Menu", 1, (0, 0, 0)) 
        textTitlePos = textTitle.get_rect()
        textTitlePos.centerx = surface.get_rect().centerx
        textTitlePos.y = buttonHeight/4
        surface.blit(textTitle, textTitlePos)

        for button in self.buttons:
            button.drawButton()
            
    def loop(self):
        framesPerSecond = pygame.time.Clock()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 49:
                        self.board.reset() # Reseta o tabuleiro antes de iniciar um novo jogo
                        self.board.loop()
                    elif event.key == 50:
                        self.board.reset() # Reseta o tabuleiro antes de iniciar um novo jogo
                        self.board.loop()
                    elif event.key == 51:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        for button in self.buttons:
                            if(button.buttonX < x and button.buttonX + button.buttonW > x and button.buttonY < y and button.buttonY + button.buttonH > y):
                                button.click()


            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)

    def gotoBoardScreen(self, type_game):
        # 0 : player x AI
        # 1 : player x player
        # 2 : AI X AI
        self.board.reset() # Reseta o tabuleiro antes de iniciar um novo jogo
        self.board.loop(type_game)

    def exit(self):
        pygame.quit()
        sys.exit()