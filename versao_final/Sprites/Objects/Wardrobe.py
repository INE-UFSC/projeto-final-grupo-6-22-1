import pygame as pg
from Sprites.Entity import Entity


class Wardrobe(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe.png", (78, 108))

    #colisão com o objeto
    def colidir(self, objeto):
        if pg.sprite.collide_mask(self, objeto):
            return True
        else:
            return False

class Wardrobe2(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe2.png", (78, 108))

class Wardrobe3(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe3.png", (78, 108))


class Wardrobe4(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe4.png", (78, 108))
