from tracemalloc import start
import pygame as pg
from copy import copy
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

        self.original_image = copy(self.image)
        self.hitbox = pg.Rect(start_pos, (30, 30))

        self.health = 2

        self.change_x = 0
        self.change_y = 0

        self.last_pos = start_pos

        self.in_cooldown = False
        self.last_shot_time = 0

        self.grace_period = 1000
        self.immune = False

        self.time_last_hit = False

    def update(self):
        """
        Atualiza a sprite
        """
        self.rect.center = self.hitbox.centerx, self.hitbox.centery - 28

        time = pg.time.get_ticks()
        if time - self.last_shot_time >= 800: #cooldown especifico arma
            self.in_cooldown = False

        if time - self.time_last_hit >= self.grace_period:
            self.image = copy(self.original_image)
            self.immune = False

    def change_tint(self, color):
        """
        Aplica na surface a color fornecida
        """
        self.image.fill(color, special_flags = pg.BLEND_RGBA_MULT)

    def attack(self, direct):
        """
        Ataca na direção informada e retorna ataque
        """
        attk = Attack(start_pos=self.rect.center, direction=direct, damage=1,damages_player=False, time_spawned=100)
        self.in_cooldown = True
        self.last_shot_time = pg.time.get_ticks()
        return attk

    def damage_taken(self, damage):
        """
        Recebe dano
        """
        if not self.immune:
            self.immune = True
            self.time_last_hit = pg.time.get_ticks()

            self.change_tint((255, 0, 0, 255))

            self.health = self.health - damage

        print(self.health)

    def move_back(self):
        """
        Move o jogador para a posição anterior
        """
        self.hitbox.center = self.last_pos
