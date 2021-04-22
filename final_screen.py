import pygame, sys
from pygame.locals import *
from button import *
from config import *
import time

class FinalScreen():
    def __init__(self, display, looser, win, draw_type):
        self.surface = display
        self.looser = looser # Indica o jogador perdedor
        self.start_time = None # Tempo que indica quando a funcao loop foi chamada pela primeira vez
        self.seconds_to_desapear = 5 # Segundos para a tela final desaparecer
        self.win = win # Se True, houve ganhador; se false, foi empate
        self.draw_type = draw_type # Se for um caso de empate, contem o nome do caso de empate

    def draw(self, surface):

        surface.fill((124, 76, 62))

        # Renderizando título "Resultado"
        textTitle = pygame.font.Font.render(pygame.font.SysFont('comicsansms', 32), "Resultado", 1, (0, 0, 0)) 
        textTitlePos = textTitle.get_rect()
        textTitlePos.centerx = surface.get_rect().centerx
        textTitlePos.y = 50
        surface.blit(textTitle, textTitlePos)

        # Renderizando quem foi o ganhador
        if self.win:
            textWinnerContent = "Ganhador: " + "Preto" if self.looser == "white" else "Branco"
        else:
            textWinnerContent = "Empate por " + self.draw_type
        textWinner = pygame.font.Font.render(pygame.font.SysFont('comicsansms', 32), textWinnerContent, 1, (0, 0, 0)) 
        textWinnerPos = textWinner.get_rect()
        textWinnerPos.centerx = surface.get_rect().centerx
        textWinnerPos.y = 150
        surface.blit(textWinner, textWinnerPos)
        
        # Renderizando contador para voltar para o Menu
        textCronometerContent = "." * round(self.start_time + self.seconds_to_desapear - time.time())
        textCronometer = pygame.font.Font.render(pygame.font.SysFont('comicsansms', 48), textCronometerContent, 1, (0, 0, 0)) 
        textCronometerPos = textCronometer.get_rect()
        textCronometerPos.centerx = surface.get_rect().centerx
        textCronometerPos.y = 250
        surface.blit(textCronometer, textCronometerPos)

    def loop(self):
        framesPerSecond = pygame.time.Clock()
        self.start_time = time.time()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == 51:
                        pygame.quit()
                        sys.exit()

            self.draw(self.surface)
            pygame.display.update()
            framesPerSecond.tick(FPS)

            # Sair do loop quando passar os segundos 
            if time.time() >= self.start_time + self.seconds_to_desapear: # Quando se passarem "seconds_to_desapear" segundos...
                break

    def exit(self):
        pygame.quit()
        sys.exit()