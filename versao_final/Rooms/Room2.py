import pygame as pg
from States.AbstractState import AbstractState
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Enemy import Enemy
from Sprites.Objects.Wardrobe import Wardrobe
from Sprites.Objects.Door import Door

class Room2(AbstractRoom):
    def __init__(self):
        super().__init__()

    def draw_background(self, screen):
        self.background = get_image('Telas', 'Tela.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))
        screen.blit(self.background, dest=(0, 0))

    def draw_art(self, screen):
        pass
    
    def load(self, entry_point):
        self.entities['enemies'].append(Enemy((600, 600)))
        self.entities['enemies'].append(Enemy((650, 600)))
        self.entities['objects'].append(Door((900, 287)))        
        self.entities['objects'].append(Wardrobe((700, 310)))
        self.entities['objects'].append(Wardrobe((600, 310)))
        self.entities['enemies'].append(Enemy((550, 400)))
        self.entities['enemies'].append(Enemy((660, 362)))
        return self.entities

    def start_walls(self):
        pass

