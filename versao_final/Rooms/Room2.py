import pygame as pg
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Enemy import Enemy

class Room2(AbstractRoom):
    def __init__(self):
        super().__init__()

    def draw_background(self, screen):
        screen.fill((0, 255, 0))

    def draw_art(self, screen):
        pass
    
    def load(self, entry_point):
        self.entities['enemies'].append(Enemy((600, 600)))
        self.entities['enemies'].append(Enemy((600, 650)))
        return self.entities

    def start_walls(self):
        pass

