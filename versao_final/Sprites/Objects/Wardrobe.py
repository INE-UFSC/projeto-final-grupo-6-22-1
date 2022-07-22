import pygame as pg
from Sprites.Entity import Entity


class Wardrobe(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe.png", (78, 108))

    def interaction(self, player):
        player.health += 2
        #return 2

class Wardrobe2(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe2.png", (78, 108))

    def interaction(self, player):
        player.health -= 4

class Wardrobe3(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe3.png", (78, 108))

    def interaction(self, player):
        player.health += 2


class Wardrobe4(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe4.png", (78, 108))

    def interaction(self, player):
        player.health += 2
