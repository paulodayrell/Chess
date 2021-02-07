class tabuleiro:

    def __init__(self, tamanho):
        self.tamanho = 8
        self.matriz = [[None for x in range(self.tamanho)] for y in range(self.tamanho)]

    def reseta_tabuleiro(self):
