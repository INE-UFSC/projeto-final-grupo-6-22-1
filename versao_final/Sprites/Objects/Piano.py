import pygame as pg
from Sprites.Entity import Entity


class Piano(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "piano.png", (78, 108))
