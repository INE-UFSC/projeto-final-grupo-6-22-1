import pygame as pg

from Sprites.Entity import Entity
from Sprites.Attack import Attack

TAMANHO_PERSONAGEM = (48, 78)

class Player(Entity):
    """
    Classe do jogador
    """

    def __init__(self, start_pos = (0, 0), image_folder = "player", image_name = "Jogador.png", image_size = TAMANHO_PERSONAGEM):
        """
        Spawna um jogador na coordenada x,y
        """
        # Inicialização
        super().__init__(start_pos, image_folder, image_name, image_size)

        self.health = 2

        self.change_x = 0
        self.change_y = 0

        self.last_pos = start_pos

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
        attk = Attack(start_pos=self.rect.center, direction=direct, damage=1,damages_player=False, time_spawned=300)
        self.in_cooldown = True
        self.last_shot_time = pg.time.get_ticks()
        return attk

    def damage_taken(self, damage):
        """
        Recebe dano
        """
        self.health = self.health - damage
        print(self.health)

    def move_back(self):
        """
        Move o jogador para a posição anterior
        """
        self.rect.centerx, self.rect.centery = self.last_pos
