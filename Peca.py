from abc import ABCMeta, abstractmethod
import pygame

class Peca:
    def __init__(self, linha, coluna, colour, name, tile_length, abc=ABCMeta):
        self.linha = linha
        self.coluna = coluna
        self.colour = colour
        self.name = name
        self.captured = False
        self.moves = 0 # nao precisamos de moved pq é só verificar se moves >0
        self.image = pygame.image.load(
            "./sprites/128h/" + colour + "_" + name + ".png")
        self.tile_length = tile_length
        self.image = pygame.transform.scale(self.image, (tile_length, tile_length))

    def __str__(self):
        print("Nome: ", self.name)
        print("Linha: ", self.linha)
        print("Coluna: ", self.coluna)
        print("Cor: ", self.colour)

    @abstractmethod
    def get_movements(self):
        pass


    def copy(self):
        copy = type(self)(self.linha, self.coluna, self.colour, self.tile_length)
        copy.captured = self.captured
        copy.moves = self.moves
        copy.image = self.image
        return copy

    def set_posicao(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
    
    def get_posicao(self):
        return [self.linha, self.coluna]

    def movimentos_diagonais(self, tabuleiro):
        moveset = []
        
        linha =self.linha - 1
        coluna = self.coluna - 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            linha -= 1
            coluna -= 1

        linha = self.linha + 1
        coluna = self.coluna - 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            linha += 1
            coluna -= 1

        linha =self.linha - 1
        coluna = self.coluna + 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            linha -= 1
            coluna += 1

        linha =self.linha + 1
        coluna = self.coluna + 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            linha += 1
            coluna += 1


        #print(moveset)
        return moveset

    def movimentos_cruz(self, tabuleiro):
        moveset = []
        
        linha = self.linha - 1
        coluna = self.coluna
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            linha -= 1

        linha = self.linha + 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            linha += 1

        linha = self.linha
        coluna = self.coluna - 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            coluna -= 1

        coluna = self.coluna + 1
        while tabuleiro.pode_mover(self, linha, coluna):
            moveset.append([linha, coluna])
            if tabuleiro.get_piece(linha, coluna): break
            coluna += 1

        return moveset

class Rei(Peca):
    def __init__(self, linha, coluna, colour, tile_length):
        self.moveset = {(coluna, linha) for coluna in range(-1, 2)
                        for linha in range(-1, 2) if coluna != 0 or linha != 0}
        super().__init__(linha, coluna, colour, 'king', tile_length)

    def get_movements(self, tabuleiro):
        moveset = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                linha = self.linha + i
                coluna = self.coluna + j
                if(tabuleiro.pode_mover(self, linha, coluna)):
                    moveset.append([linha, coluna])
        return moveset

class Torre(Peca):
    def __init__(self, linha, coluna, colour, tile_length):
        super().__init__(linha, coluna, colour, 'rook', tile_length)

    def get_movements(self, tabuleiro):
        moveset = self.movimentos_cruz(tabuleiro)
        #print(moveset)
        return moveset

class Bispo(Peca):
    def __init__(self, linha, coluna, colour, tile_length):
        super().__init__(linha, coluna, colour, 'bishop', tile_length)

    def get_movements(self, tabuleiro):
        return self.movimentos_diagonais(tabuleiro)

class Cavalo(Peca):
    def __init__(self, linha, coluna, colour, tile_length):
        super().__init__(linha, coluna, colour, 'knight', tile_length)

    def get_movements(self, tabuleiro):
        moveset = [
            [self.linha+2, self.coluna-1],
            [self.linha+2, self.coluna+1],
            [self.linha-2, self.coluna-1],
            [self.linha-2, self.coluna+1],
            [self.linha+1, self.coluna+2],
            [self.linha+1, self.coluna-2],
            [self.linha-1, self.coluna+2],
            [self.linha-1, self.coluna-2]
        ]

        return [m for m in moveset if tabuleiro.pode_mover(self, m[0], m[1])]

class Rainha(Peca):
    def __init__(self, linha, coluna, colour, tile_length):
        super().__init__(linha, coluna, colour, 'queen', tile_length)

    def get_movements(self, tabuleiro):
        moveset = self.movimentos_diagonais(tabuleiro)
        moveset += self.movimentos_cruz(tabuleiro)
        
        return moveset

class Peao(Peca):
    def __init__(self, linha, coluna, colour, tile_length):
        self.direction = -1 if colour == 'white' else 1
        self.moveset = {(linha * self.direction, 0) for linha in range(1, 2)}
        super().__init__(linha, coluna, colour, 'pawn', tile_length)

    def get_movements(self, tabuleiro):
        moveset = []

        linha = self.linha + self.direction
        coluna = self.coluna

        if tabuleiro.posicao_valida(linha, coluna) and not tabuleiro.get_piece(linha, coluna):
            moveset.append([linha, coluna])
            if self.moves == 0:
                linha += self.direction
                if not tabuleiro.get_piece(linha, coluna):
                    moveset.append([linha, coluna])

        offset = [-1, 1]
        linha = self.linha + self.direction
        for i in offset:
            coluna = self.coluna + i
            if tabuleiro.pode_mover(self, linha, coluna) and tabuleiro.get_piece(linha, coluna):
                moveset.append([linha, coluna])

        return moveset
