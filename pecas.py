import pygame

class Peca:
    def __init__(self, colour, name):
        self.colour = colour
        self.name = name
        self.image = pygame.image.load("./sprites/128h/" + colour + "_" + name + ".png")

class Rei(Peca):
    def __init__(self, colour):
        self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}
        super().__init__(colour, 'king')

class Rainha(Peca):
    def __init__(self, colour):
        self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 or y != 0}
        super().__init__(colour, 'queen')

class Torre(Peca):
    def __init__(self, colour):
        self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if (x == 0 or y == 0) and (x != 0 or y != 0)}
        super().__init__(colour, 'rook')

class Bispo(Peca):
    def __init__(self, colour):
        self.moveset = {(x, y) for x in range(-1, 2) for y in range(-1, 2) if x != 0 and y != 0}
        super().__init__(colour, 'bishop')

class Cavalo(Peca):
    def __init__(self, colour):
        self.moveset = {(x, y) for x in range(-2, 3) for y in range(-2, 3) if x != 0 and y != 0 and abs(x) != abs(y)}
        super().__init__(colour, 'knight')

class Peao(Peca):
    def __init__(self, colour):
        self.direction = -1 if colour == 'white' else 1
        self.moveset = {(0, y * self.direction) for y in range(1, 2)}
        super().__init__(colour, 'pawn')