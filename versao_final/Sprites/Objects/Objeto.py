from xml.dom.minidom import Entity
import pygame as pg
from get_image import get_image
from Sprites.Entity import Entity
#from pygame.locals import *

TAMANHO_OBJETO = (68, 68)


class Objeto(Entity):


    def __init__(self, start_pos = (0, 0)):

        # Inicialização
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.smoothscale(get_image("objeto", "quadrilatero.png"), TAMANHO_OBJETO)

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        # Coordenadas iniciais
        self.rect.centerx, self.rect.centery = start_pos


    #colisão com o objeto
    def colidir(self, objeto):
        if pg.sprite.collide_mask(self, objeto):
            return True
        else:
            return False
    
