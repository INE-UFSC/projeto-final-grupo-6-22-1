import pygame as pg
from Sprites.Entity import Entity


class Bed(Entity):


    def __init__(self, start_pos = (0, 0)):
        # Inicialização
        super().__init__(start_pos, "objeto", "cama.png", (75, 100))

    def interaction(self, player):
        print("Você não pode dormir agora, há monstros por perto")