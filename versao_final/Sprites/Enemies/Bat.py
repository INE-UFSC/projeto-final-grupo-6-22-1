import pygame as pg
from random import choice
from Sprites.Enemies.Enemy import Enemy

class Bat(Enemy):
    def __init__(self, start_pos, image_folder="enemies", image_name="quadrado.png", image_size=(30, 30)):
        super().__init__(start_pos, image_folder, image_name, image_size)
        self.name = "Bat"
        self.health = 2
        self.damage = 1
        self.direction = choice(((-1, 1), (-1, -1), (1, 1), (1, -1)))

    def update(self):
        super().update()
        pass

    def change_direction(self, wall_rect):
        """
        Quica na parede
        """
        # if self.rect.left <= 0 or self.rect.right >= pg.display.get_surface().get_width():
        #     self.direction = (-self.direction[0], self.direction[1])
        # if self.rect.top <= 0 or self.rect.bottom >= pg.display.get_surface().get_height():
        #     self.direction = (self.direction[0], -self.direction[1])
        if self.rect.left <= wall_rect.left or self.rect.right >= wall_rect.right:
            self.direction = (-self.direction[0], self.direction[1])
        if self.rect.top <= wall_rect.top or self.rect.bottom >= wall_rect.bottom:
            self.direction = (self.direction[0], -self.direction[1])
        
        

    def ai_move(self, player_coord):
        """
        Movimenta-se em diagonais
        """
        return self.direction[0]*2.5, self.direction[1]*2.5
