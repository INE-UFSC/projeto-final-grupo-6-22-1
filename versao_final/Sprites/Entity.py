import pygame as pg
from get_image import get_image #image_folder, image_name, image_sizetemporario?

class Entity(pg.sprite.Sprite):
    def __init__(self, start_pos, image_folder, image_name, image_size):
        """
        Spawna uma entidade na coordenada x,y
        """
        # Inicialização
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.smoothscale(get_image(image_folder, image_name), image_size)

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        # Coordenadas iniciais
        self.rect.centerx, self.rect.centery = start_pos


    def update(self):
        """
        Atualiza a sprite
        """
        pass

    def damage_taken(self, damage):
        """
        Recebe dano
        """
        pass
