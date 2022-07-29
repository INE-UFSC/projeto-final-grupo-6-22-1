import pygame as pg
from get_image import get_image
from Rooms.AbstractRoom import AbstractRoom
from Sprites.Enemies.Zombie import Zombie
from Sprites.Enemies.Skeleton import Skeleton
from Sprites.Enemies.Bat import Bat
from Sprites.Objects.Wardrobe import Wardrobe
from Sprites.Objects.Door import DoorBoss
from Sprites.Objects.Bed import Bed
from Sprites.Wall import Wall

class Room8(AbstractRoom):
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

        self.entities['enemies'].append(Zombie((700, 500)))
        self.entities['enemies'].append(Zombie((800, 500)))
        self.entities['enemies'].append(Zombie((750, 570)))
        self.entities['enemies'].append(Zombie((700, 380)))
        self.entities['enemies'].append(Skeleton((400, 310)))
        self.entities['enemies'].append(Skeleton((330, 310)))
        self.entities['enemies'].append(Bat((520, 350)))
        self.entities['enemies'].append(Bat((700, 387)))
        self.entities['objects'].append(Wardrobe((400, 310)))
        self.entities['objects'].append(Wardrobe((330, 310)))
        self.entities['objects'].append(Bed((820, 350)))
        self.entities['objects'].append(DoorBoss((500, 287), 8))
        
        
        return self.entities

    def start_walls(self):
        self.entities['walls'].append(Wall((174, 327), (940, 10))) #parede norte
        self.entities['walls'].append(Wall((164, 337), (10, 324))) #parede oeste
        self.entities['walls'].append(Wall((1115, 337), (10, 324))) #parede leste
        self.entities['walls'].append(Wall((174, 658), (940, 10))) #parede sul
