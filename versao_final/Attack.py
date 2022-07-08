import pygame as pg
from get_image import get_image #temporario?

class Attack(pg.sprite.Sprite):
    def __init__(self, attacker_pos, direction, format, damage, damages_player, time_spawned):
        # Inicialização
        pg.sprite.Sprite.__init__(self)

        if direction == 'up':
            angle = 180
            attack_pos = (attacker_pos[0], attacker_pos[1]-80)
        
        elif direction == 'down':
            angle = 0
            attack_pos = (attacker_pos[0], attacker_pos[1]+80)

        elif direction == 'left':
            angle = 270
            attack_pos = (attacker_pos[0]-60, attacker_pos[1])

        elif direction == 'right':
            angle = 90
            attack_pos = (attacker_pos[0]+60, attacker_pos[1])


        if format=='vertical_pipe':
            self.image = pg.transform.smoothscale(get_image("attacks", "quadrado.png"), (40, 80))

        elif format=='triangular':
            self.image = pg.transform.smoothscale(get_image("attacks", "triangulo.png"), (300, 140))


        self.image = pg.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect()
        self.rect.center = attack_pos
        
        self.mask = pg.mask.from_surface(self.image)

        self.damages_player = damages_player
        self.damage = damage

        self.time_spawned = time_spawned
        self.time = pg.time.get_ticks()

    def update(self):
        if pg.time.get_ticks() - self.time >= self.time_spawned:
            self.kill()
