import pygame as pg
from Sprites.Entity import Entity


class SideDoor(Entity):


    def __init__(self, start_pos = (0, 0), room_id = 0):
        # Inicialização
        super().__init__(start_pos, "objeto", "sideDoor.png", (78, 78))
        self.room_id = room_id

    def interaction(self, player):
        return self.room_id
    