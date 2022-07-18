import pygame as pg
from Sprites.Enemies.Enemy import Enemy

class Zombie(Enemy):
    def __init__(self, start_pos, image_folder="enemies", image_name="zumbi.png", image_size=(48, 78)):
        super().__init__(start_pos, image_folder, image_name, image_size)

        self.health = 2
        self.damage = 1

    def update(self):
        super().update()
        pass

