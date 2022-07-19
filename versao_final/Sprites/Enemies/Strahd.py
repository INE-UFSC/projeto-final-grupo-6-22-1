import pygame as pg
from math import atan2, cos, sin
from Sprites.Enemies.Enemy import Enemy

class Strahd(Enemy):
    def __init__(self, start_pos, image_folder="enemies", image_name="zumbi.png", image_size=(150, 150)):
        super().__init__(start_pos, image_folder, image_name, image_size)
        self.name = "Strahd"
        self.health = 5
        self.damage = 1

    def ai_move(self, player_coord):
        """
        Movimenta-se em direção do jogador
        """
        x_diff = player_coord[0] - self.rect.centerx
        y_diff = player_coord[1] - self.rect.centery
        angle = atan2(y_diff, x_diff)

        movement = (cos(angle) * 1.5, sin(angle) * 1.5)

        return movement

    def update(self):
        super().update()
        pass

    def damage_taken(self, damage):
        super().damage_taken(damage)

        if self.health <= 0:
            pg.event.post(pg.event.Event(pg.USEREVENT+1, {'enemy_name': self.name}))

