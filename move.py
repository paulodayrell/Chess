import pygame

class Move:
    def __init__(self, from_coord, to_coord, captured):
        self.from_coord = from_coord
        self.to_coord = to_coord
        self.captured = captured 
