import pygame as pg
from Sprites.Entity import Entity


class Table(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "mesa.png", (80, 90))

class Table2(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "mesa2.png", (80, 90))
