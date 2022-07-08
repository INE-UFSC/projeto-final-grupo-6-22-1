import pygame as pg
from get_image import get_image #temporario?
from Attack import Attack

TAMANHO_PERSONAGEM = (28, 78)

class Player(pg.sprite.Sprite):
    """
    Classe do jogador
    """

    def __init__(self, start_pos = (0, 0)):
        """
        Spawna um jogador na coordenada x,y
        """
        # Inicialização
        pg.sprite.Sprite.__init__(self)

        self.image = pg.transform.smoothscale(get_image("player", "quadrado.png"), TAMANHO_PERSONAGEM)

        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

        # Coordenadas iniciais
        self.rect.centerx, self.rect.centery = start_pos

        self.health = 300

        self.in_cooldown = False
        self.last_shot_time = 0

    def update(self):
        """
        Atualiza a sprite
        """
        if pg.time.get_ticks() - self.last_shot_time >= 800: #cooldown especifico arma
            self.in_cooldown = False

    def attack(self, direct):
        """
        Ataca na direção informada e retorna ataque
        """
        attk = Attack(attacker_pos=self.rect.center, direction=direct, format='triangular', damage=1,damages_player=False, time_spawned=300)
        self.in_cooldown = True
        self.last_shot_time = pg.time.get_ticks()
        return attk

    def damage_taken(self, damage):
        """
        Recebe dano
        """
        self.health = self.health - damage
        print(self.health)
