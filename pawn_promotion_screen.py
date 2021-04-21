import pygame
import sys
from pygame.locals import *
from button import *
from config import *

class PawnPromotionScreen():
    def __init__(self, display, board, piece):
        self.surface = display
        self.buttonSize = {
            "w": width/2,
            "h": height/2
        }
        self.buttons = [
            Button(self.surface, 'queen', self.selectPiece, 'queen',
                   (190, 190, 190), 0, 0, self.buttonSize["w"], self.buttonSize["h"]),
            Button(self.surface, 'rook', self.selectPiece, 'rook', (190, 190, 190),
                   0, self.buttonSize["w"], self.buttonSize["w"], self.buttonSize["h"]),
            Button(self.surface, 'bishop', self.selectPiece, 'bishop', (190, 190, 190),
                   self.buttonSize["h"], 0, self.buttonSize["w"], self.buttonSize["h"]),
            Button(self.surface, 'knight', self.selectPiece, 'knight', (190, 190, 190),
                   self.buttonSize["h"], self.buttonSize["w"], self.buttonSize["w"], self.buttonSize["h"])
        ]
        self.running = True

        self.board = board
        self.piece = piece

    def draw(self, surface):
        surface.fill((124, 76, 62))
        for button in self.buttons:
            button.drawButton()

    def loop(self):
        framesPerSecond = pygame.time.Clock()

        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = event.pos
                        for button in self.buttons:
                            if(button.buttonX < x and button.buttonX + button.buttonW > x and button.buttonY < y and button.buttonY + button.buttonH > y):
                                return button.click()

            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)

    def selectPiece(self, piece):
        return piece
