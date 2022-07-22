import pygame as pg
from Sprites.Entity import Entity


class Wardrobe(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe.png", (78, 108))

    def interaction(self, player):
        player.health += 2
        print("Você ganhou 2 de vida")
        #return 2

class Wardrobe2(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe2.png", (78, 108))

    def interaction(self, player):
        player.health -= 4
        print("Você interagiu com o armário 2, e perdeu 4 de vida")

class Wardrobe3(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe3.png", (78, 108))

    def interaction(self, player):
        player.health += 5
        print("Você ganhou 5 de vida")


class Wardrobe4(Entity):
    

    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "wardrobe4.png", (78, 108))

    def interaction(self, player):
        player.health -= 1
        print("Você perdeu 1 de vida")
