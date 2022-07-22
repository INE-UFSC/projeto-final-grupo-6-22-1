import pygame as pg
from Sprites.Entity import Entity


class Door(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "door.png", (60, 100))

    def interaction(self, player):
        return 2

    def change_room(self, room):
        if self.colidir:
            self.next = room
            self.done = True
        self.room_controller.change_room(room)

    