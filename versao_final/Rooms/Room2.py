import pygame as pg
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Zombie import Zombie
from Sprites.Objects.Wardrobe import Wardrobe
from Sprites.Objects.Door import Door
from Sprites.Objects.SideDoor import SideDoor
from Sprites.Wall import Wall
from Sprites.Enemies.Bat import Bat
from Sprites.Enemies.Skeleton import Skeleton

class Room2(AbstractRoom):
    def __init__(self):
        super().__init__()
        self.__background = get_image('Telas', 'Tela.png')
        self.__background = pg.transform.smoothscale(self.__background, (1280, 700))
        self.__art= get_image('maps', 'map2.png')
        self.__art = pg.transform.smoothscale(self.__art, (170, 170))
        self.__art2= get_image('picture', 'picture1.png')
        self.__art2 = pg.transform.smoothscale(self.__art2, (77, 82))

    def draw_background(self, screen):

        screen.blit(self.__background, dest=(0, 0))

    def draw_art(self, screen):
        screen.blit(self.__art, (10, 10))
        screen.blit(self.__art2, (300, 220))

    
    def load(self, entry_point):
        self.start_walls()

        self.entities['enemies'].append(Zombie((600, 600)))
        self.entities['enemies'].append(Zombie((650, 600)))
        #self.entities['objects'].append(Door((900, 287), 2))        
        self.entities['objects'].append(Wardrobe((700, 310)))
        self.entities['objects'].append(Wardrobe((600, 310)))
        self.entities['enemies'].append(Zombie((550, 400)))
        self.entities['enemies'].append(Zombie((660, 362)))
        self.entities['enemies'].append(Bat((800, 500)))
        self.entities['objects'].append(SideDoor((1150, 387), 2))
        return self.entities

    def start_walls(self):
        self.entities['walls'].append(Wall((174, 327), (940, 10))) #parede norte
        self.entities['walls'].append(Wall((164, 337), (10, 324))) #parede oeste
        self.entities['walls'].append(Wall((1115, 337), (10, 324))) #parede leste
        self.entities['walls'].append(Wall((174, 658), (940, 10))) #parede sul

