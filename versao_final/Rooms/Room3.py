import pygame as pg
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Objects.Wardrobe import Wardrobe2
from Sprites.Objects.Door import Door
from Sprites.Objects.Piano import Piano
from Sprites.Wall import Wall
from Sprites.Enemies.Skeleton import Skeleton

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

        self.entities['objects'].append(Wardrobe2((450, 310)))
        self.entities['objects'].append(Wardrobe2((540, 310)))
        self.entities['objects'].append(Door((860, 287), 3))
        self.entities['objects'].append(Piano((720, 329)))
        self.entities['enemies'].append(Skeleton((600, 400)))
        self.entities['enemies'].append(Skeleton((650, 380)))
        self.entities['enemies'].append(Skeleton((550, 400)))
        self.entities['enemies'].append(Skeleton((660, 362)))
        
        
        return self.entities

    def start_walls(self):
        self.entities['walls'].append(Wall((174, 327), (940, 10))) #parede norte
        self.entities['walls'].append(Wall((164, 337), (10, 324))) #parede oeste
        self.entities['walls'].append(Wall((1115, 337), (10, 324))) #parede leste
        self.entities['walls'].append(Wall((174, 658), (940, 10))) #parede sul
