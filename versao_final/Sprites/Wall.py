import pygame as pg

class Wall(pg.sprite.Sprite):
    def __init__(self, start_pos, wall_size):
        """
        Spawna uma entidade na coordenada x,y
        """
        # Inicialização
        pg.sprite.Sprite.__init__(self)

        self.rect = pg.Rect(0, 0, wall_size[0], wall_size[1])

        # Coordenadas iniciais
        self.rect.x, self.rect.y = start_pos


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
