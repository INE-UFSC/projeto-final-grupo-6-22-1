import pygame as pg
from Sprites.Entity import Entity

class Enemy(Entity):
    def __init__(self, start_pos, image_folder="enemies", image_name="zumbi.png", image_size=(48, 78)):
        super().__init__(start_pos, image_folder, image_name, image_size)

        self.health = 2


    def update(self):
        pass

    def damage_taken(self, damage):
        self.health = self.health - damage
        if self.health <= 0:
            self.kill()
            