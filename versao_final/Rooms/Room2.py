import pygame as pg
from Rooms.AbstractRoom import AbstractRoom

class Room2(AbstractRoom):
    def __init__(self):
        super().__init__()

    def draw_background(self, screen):
        screen.fill((0, 255, 0))

    def draw_art(self, screen):
        pass
    
    def load(self, entry_point):
        pass

    def unload(self):
        pass

    def start_walls(self):
        pass

