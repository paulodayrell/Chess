from abc import ABCMeta, abstractmethod
import pygame


class Peca:
    def __init__(self, linha, coluna, colour, name, abc=ABCMeta):
        self.linha = linha
        self.coluna = coluna
        self.colour = colour
        self.name = name
        self.moved = False
        self.captured = False
        self.moves = 0
        self.image = pygame.image.load(
            "./sprites/128h/" + colour + "_" + name + ".png")

    def __str__(self):
        print("Nome: ", self.name)
        print("Linha: ", self.linha)
        print("Coluna: ", self.coluna)
        print("Cor: ", self.colour)

    @abstractmethod
    def get_movements(self):
        pass

    def pode(self, movimento):
        if movimento[0] >= 0 and movimento[0] < 8 and movimento[1] >= 0 and movimento[1] < 8:
            return True
        return False


class Rei(Peca):
    def __init__(self, linha, coluna, colour):
        self.moveset = {(coluna, linha) for coluna in range(-1, 2)
                        for linha in range(-1, 2) if coluna != 0 or linha != 0}
        super().__init__(linha, coluna, colour, 'king')

    def get_movements(self):
        moveset = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                movimento = [self.linha + i, self.coluna + j]
                if(self.pode(movimento)):
                    moveset.append(movimento)
        return moveset


class Rainha(Peca):
    def __init__(self, linha, coluna, colour):
        super().__init__(linha, coluna, colour, 'queen')

    def get_movements(self):
        moveset = []
        for i in range(8):
            if(self.linha != i):
                moveset.append([i, self.coluna])
            if(self.coluna != i):
                moveset.append([self.linha, i])

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]-1, move[1]-1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]+1, move[1]-1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]-1, move[1]+1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]+1, move[1]+1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        return moveset


class Torre(Peca):
    def __init__(self, linha, coluna, colour):
        super().__init__(linha, coluna, colour, 'rook')

    def get_movements(self):
        moveset = []
        for i in range(8):
            if(self.linha != i):
                moveset.append([i, self.coluna])
            if(self.coluna != i):
                moveset.append([self.linha, i])

        return moveset


class Bispo(Peca):
    def __init__(self, linha, coluna, colour):
        super().__init__(linha, coluna, colour, 'bishop')

    def get_movements(self):
        moveset = []

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]-1, move[1]-1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]+1, move[1]-1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]-1, move[1]+1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        move = [self.linha, self.coluna]
        while True:
            move = [move[0]+1, move[1]+1]
            if (not self.pode(move)):
                break
            moveset.append(move)

        return moveset


class Cavalo(Peca):
    def __init__(self, linha, coluna, colour):
        super().__init__(linha, coluna, colour, 'knight')

    def get_movements(self):
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

        return [m for m in moveset if self.pode(m)]


class Peao(Peca):
    def __init__(self, linha, coluna, colour):
        self.direction = -1 if colour == 'white' else 1
        self.moveset = {(linha * self.direction, 0) for linha in range(1, 2)}
        super().__init__(linha, coluna, colour, 'pawn')

    def get_movements(self):
        moveset = []

        direction = -1 if self.colour == 'white' else 1

        #TODO colocar diagonal

        if self.moves == 0:
            for i in range(1, 3):
                moveset.append([self.linha + i*direction, self.coluna])
        else:
            moveset.append([self.linha + direction, self.coluna])

        return moveset
