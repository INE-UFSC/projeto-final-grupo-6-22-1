import pygame as pg
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Skeleton import Skeleton
from Sprites.Objects.Wardrobe import Wardrobe3, Wardrobe2
from Sprites.Objects.SideDoor import SideDoor
from Sprites.Objects.Bed import Bed
from Sprites.Objects.Piano import Piano
from Sprites.Objects.Table import Table
from Sprites.Enemies.Bat import Bat
from Sprites.Wall import Wall

class Room4(AbstractRoom):
    def __init__(self):
        super().__init__()
        self.background = get_image('Telas', 'Tela.png')
        self.background = pg.transform.smoothscale(self.background, (1280, 700))
        self.art= get_image('maps', 'map4.png')
        self.art = pg.transform.smoothscale(self.art, (170, 170))
        self.art2= get_image('picture', 'picture2.png')
        self.art2 = pg.transform.smoothscale(self.art2, (100, 135))
        
    def draw_background(self, screen):
        #screen.fill((255, 255, 255))
        
        screen.blit(self.background, dest=(0, 0))

    def draw_art(self, screen):
        screen.blit(self.art, (10, 10))
        screen.blit(self.art2, (650, 205))
    
    def load(self, entry_point):
        self.start_walls()

        self.entities['enemies'].append(Skeleton((700, 500)))
        self.entities['enemies'].append(Skeleton((800, 500)))
        self.entities['enemies'].append(Skeleton((750, 570)))
        self.entities['enemies'].append(Skeleton((700, 380)))
        self.entities['objects'].append(Wardrobe3((400, 310)))
        self.entities['objects'].append(Wardrobe2((330, 310)))
        self.entities['enemies'].append(Bat((520, 350)))
        self.entities['enemies'].append(Bat((540, 410)))
        self.entities['enemies'].append(Bat((560, 430)))
        self.entities['enemies'].append(Bat((520, 450)))
        self.entities['enemies'].append(Bat((520, 390)))
        self.entities['objects'].append(SideDoor((135, 487), 4))
        self.entities['objects'].append(Piano((820, 329)))
        
        
        return self.entities

    def start_walls(self):
        self.entities['walls'].append(Wall((174, 327), (940, 10))) #parede norte
        self.entities['walls'].append(Wall((164, 337), (10, 324))) #parede oeste
        self.entities['walls'].append(Wall((1115, 337), (10, 324))) #parede leste
        self.entities['walls'].append(Wall((174, 658), (940, 10))) #parede sul
