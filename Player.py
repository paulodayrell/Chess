class Player:
    def __init__(self, cor, turn):

        self.turn = turn
        self.cor = cor
        self.pecas_capturadas = []

    def capturar_peca(self, peca):
        self.pecas_capturadas.append(peca)

    def passar_turno(self):
        self.turn = not self.turn