import pygame as pg
from math import atan2, cos, sin
from Sprites.Enemies.Enemy import Enemy

class Zombie(Enemy):
    def __init__(self, start_pos, image_folder="enemies", image_name="zumbi.png", image_size=(48, 78)):
        super().__init__(start_pos, image_folder, image_name, image_size)
        self.name = "Zombie"
        self.health = 4
        self.damage = 1

    def ai_move(self, player_coord):
        """
        Movimenta-se em direção do jogador
        """
        x_diff = player_coord[0] - self.rect.centerx
        y_diff = player_coord[1] - self.rect.centery
        angle = atan2(y_diff, x_diff)

        movement = (cos(angle) * 1.2, sin(angle) * 1.2)

        return movement

    def update(self):
        super().update()
        pass

