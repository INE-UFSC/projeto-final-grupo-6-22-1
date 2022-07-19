import pygame as pg
from copy import copy
from Sprites.Entity import Entity

class Enemy(Entity):
    def __init__(self, start_pos, image_folder, image_name, image_size):
        super().__init__(start_pos, image_folder, image_name, image_size)

        self.original_image = copy(self.image)

        self.health = 2
        self.damage = 1

        self.grace_period = 110
        self.immune = False

        self.time_last_hit = False

    def update(self):

        if pg.time.get_ticks() - self.time_last_hit >= self.grace_period:
            self.image = copy(self.original_image)
            self.immune = False
    
    def ai_move(self, player_coord):
        pass
    
    def change_tint(self, color):
        """
        Aplica na surface a color fornecida
        """
        self.image.fill(color, special_flags = pg.BLEND_RGBA_MULT)

    def damage_taken(self, damage):
        if not self.immune:
            self.immune = True
            self.time_last_hit = pg.time.get_ticks()

            self.change_tint((255, 0, 0, 255))

            self.health = self.health - damage
            if self.health <= 0:
                self.kill()
            