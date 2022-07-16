import pygame as pg
from Sprites.Entity import Entity


class Door(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "door.png", (60, 100))

    #colisão com o objeto
    def colidir(self, objeto):
        if pg.sprite.collide_mask(self, objeto):
            return True
        else:
            return False

    def change_room(self, room):
        if self.colidir:
            self.next = room
            self.done = True
        self.room_controller.change_room(room)

    