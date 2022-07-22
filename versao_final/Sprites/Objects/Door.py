import pygame as pg
from Sprites.Entity import Entity


class Door(Entity):


    def __init__(self, start_pos = (0, 0), room_id = 0):
        # Inicialização
        super().__init__(start_pos, "objeto", "door.png", (60, 100))
        self.room_id = room_id

    def interaction(self, player):
        return self.room_id
    