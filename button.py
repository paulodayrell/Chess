import pygame

class Button:
    def __init__(self, surface, text, action, actionsProps, color, x, y, width, height):
        self.buttonX = x
        self.buttonY = y
        self.buttonW = width
        self.buttonH = height

        self.text = text

        self.surface = surface

        self.color = color

        self.action = action
        self.actionProps = actionsProps

    def drawButton(self):
        pygame.draw.rect(
            self.surface, 
            self.color,
            (self.buttonX, self.buttonY, self.buttonW, self.buttonH)
        )
        textButton = pygame.font.Font.render(pygame.font.SysFont('comicsansms', 32), self.text, 1, (0, 0, 0)) 
        self.surface.blit(
            textButton, 
            (self.buttonX + (self.buttonW / 2) - textButton.get_rect()[2] / 2, self.buttonY + (self.buttonH / 2) - textButton.get_rect()[3] / 2)
        )

    def click(self):
        if self.actionProps != None:
            return self.action(self.actionProps)
        else:
            return self.action()