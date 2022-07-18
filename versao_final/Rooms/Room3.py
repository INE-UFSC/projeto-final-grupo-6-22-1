import pygame as pg
from States.AbstractState import AbstractState
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Enemy import Enemy
from Sprites.Objects.Wardrobe import Wardrobe4
from Sprites.Objects.Door import Door
from Sprites.Objects.Bed import Bed
from Sprites.Objects.Piano import Piano
from Sprites.Objects.Table import Table
from Sprites.Wall import Wall

class Room3(AbstractRoom):
    def __init__(self):
        super().__init__()
        self.background = get_image('Telas', 'Tela.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))
        
    def draw_background(self, screen):
        #screen.fill((255, 255, 255))
        
        screen.blit(self.background, dest=(0, 0))

    def draw_art(self, screen):
        pass
    
    def load(self, entry_point):
        self.start_walls()

        self.entities['enemies'].append(Enemy((700, 500)))
        self.entities['enemies'].append(Enemy((800, 500)))
        self.entities['enemies'].append(Enemy((750, 570)))
        self.entities['enemies'].append(Enemy((700, 380)))
        self.entities['objects'].append(Wardrobe4((400, 310)))
        self.entities['objects'].append(Wardrobe4((330, 310)))
        self.entities['objects'].append(Bed((520, 350)))
        self.entities['objects'].append(Door((700, 287)))
        self.entities['objects'].append(Piano((820, 329)))
        self.entities['objects'].append(Table((802, 529)))
        
        
        return self.entities

    def start_walls(self):
        self.entities['walls'].append(Wall((174, 327), (940, 10))) #parede norte
        self.entities['walls'].append(Wall((164, 337), (10, 324))) #parede oeste
        self.entities['walls'].append(Wall((1115, 337), (10, 324))) #parede leste
        self.entities['walls'].append(Wall((174, 658), (940, 10))) #parede sul