import pygame as pg
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Zombie import Zombie
from Sprites.Enemies.Bat import Bat
from Sprites.Objects.Wardrobe import Wardrobe3
from Sprites.Objects.SideDoor import SideDoor
from Sprites.Objects.Piano import Piano
from Sprites.Enemies.Ghost import Ghost
from Sprites.Wall import Wall

class Room7(AbstractRoom):
    def __init__(self):
        super().__init__()
        self.__background = get_image('Telas', 'Tela.png')
        self.__background = pg.transform.smoothscale(self.__background, (1280, 700))
        self.__art= get_image('maps', 'map7.png')
        self.__art = pg.transform.smoothscale(self.__art, (170, 170))
        self.__art2= get_image('picture', 'picture4.png')
        self.__art2 = pg.transform.smoothscale(self.__art2, (200,145))
        
    def draw_background(self, screen):
        #screen.fill((255, 255, 255))
        
        screen.blit(self.__background, dest=(0, 0))

    def draw_art(self, screen):
        screen.blit(self.__art, (10, 10))
        screen.blit(self.__art2, (550, 179))
    
    def load(self, entry_point):
        self.start_walls()

        self.entities['enemies'].append(Zombie((700, 500)))
        self.entities['enemies'].append(Zombie((800, 500)))
        self.entities['enemies'].append(Zombie((750, 570)))
        self.entities['enemies'].append(Ghost((700, 380)))
        self.entities['enemies'].append(Ghost((750, 380)))
        self.entities['enemies'].append(Ghost((340, 380)))
        self.entities['enemies'].append(Ghost((570, 380)))
        self.entities['enemies'].append(Ghost((660, 380)))
        self.entities['enemies'].append(Bat((700, 380)))
        self.entities['objects'].append(Wardrobe3((400, 310)))
        self.entities['objects'].append(Wardrobe3((330, 310)))
        self.entities['objects'].append(SideDoor((1150, 480), 7))
        self.entities['objects'].append(Piano((820, 329)))
        #self.entities['objects'].append(Table((702, 429)))
        
        
        return self.entities

    def start_walls(self):
        self.entities['walls'].append(Wall((174, 327), (940, 10))) #parede norte
        self.entities['walls'].append(Wall((164, 337), (10, 324))) #parede oeste
        self.entities['walls'].append(Wall((1115, 337), (10, 324))) #parede leste
        self.entities['walls'].append(Wall((174, 658), (940, 10))) #parede sul
